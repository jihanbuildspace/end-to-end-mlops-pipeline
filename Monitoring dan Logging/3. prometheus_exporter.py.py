"""
Prometheus Exporter for MLflow Insurance Model
Wraps MLflow model predictions with Prometheus metrics
Exposes /metrics endpoint for Prometheus scraping
"""

from flask import Flask, request, jsonify
from prometheus_client import Counter, Histogram, Gauge, generate_latest, CONTENT_TYPE_LATEST
import requests
import time
import json
import logging

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Prometheus Metrics for MODEL INFERENCE (10+ metrics)
# 1. Total prediction requests
prediction_requests_total = Counter(
    'prediction_requests_total',
    'Total number of prediction requests',
    ['method', 'endpoint']
)

# 2. Prediction duration (histogram for percentiles P50, P95, P99)
prediction_duration_seconds = Histogram(
    'prediction_duration_seconds',
    'Time spent processing prediction request',
    buckets=[0.1, 0.25, 0.5, 0.75, 1.0, 2.5, 5.0, 7.5, 10.0]
)

# 3. Total prediction errors
prediction_errors_total = Counter(
    'prediction_errors_total',
    'Total number of prediction errors',
    ['error_type']
)

# 4. Active concurrent requests
active_requests = Gauge(
    'active_requests',
    'Number of active prediction requests being processed'
)

# 5. Successful predictions
successful_predictions = Counter(
    'successful_predictions',
    'Total number of successful predictions'
)

# 6. Failed predictions
failed_predictions = Counter(
    'failed_predictions',
    'Total number of failed predictions'
)

# 7. Input validation errors
input_validation_errors = Counter(
    'input_validation_errors',
    'Total number of input validation errors'
)

# 8. Model uptime
model_uptime_seconds = Gauge(
    'model_uptime_seconds',
    'Time since model service started'
)

# 9. Predictions by status (insurance specific)
predictions_by_status = Counter(
    'predictions_by_status',
    'Total predictions grouped by predicted status',
    ['status']
)

# 10. Request payload size
request_size_bytes = Histogram(
    'request_size_bytes',
    'Size of prediction request payload in bytes',
    buckets=[100, 500, 1000, 5000, 10000]
)

# Track service start time
SERVICE_START_TIME = time.time()

# MLflow model endpoint
MLFLOW_MODEL_URL = "http://mlflow-model:8080/invocations"

@app.route('/predict', methods=['POST'])
def predict():
    """
    Accept prediction request and forward to MLflow model
    Track metrics for model inference performance
    """
    active_requests.inc()
    start_time = time.time()
    
    try:
        # Get request data
        data = request.get_json()
        
        if not data:
            input_validation_errors.inc()
            prediction_errors_total.labels(error_type='invalid_input').inc()
            failed_predictions.inc()
            return jsonify({"error": "No input data provided"}), 400
        
        # Track request size
        request_size = len(json.dumps(data).encode('utf-8'))
        request_size_bytes.observe(request_size)
        
        # Count request
        prediction_requests_total.labels(method='POST', endpoint='/predict').inc()
        
        # Forward to MLflow model
        logger.info(f"Forwarding prediction request to {MLFLOW_MODEL_URL}")
        
        headers = {'Content-Type': 'application/json'}
        response = requests.post(
            MLFLOW_MODEL_URL,
            json=data,
            headers=headers,
            timeout=30
        )
        
        # Track duration
        duration = time.time() - start_time
        prediction_duration_seconds.observe(duration)
        
        if response.status_code == 200:
            result = response.json()
            successful_predictions.inc()
            
            # Track predictions by status if available
            if 'predictions' in result and len(result['predictions']) > 0:
                predicted_status = str(result['predictions'][0])
                predictions_by_status.labels(status=predicted_status).inc()
            
            logger.info(f"Prediction successful in {duration:.3f}s")
            return jsonify(result), 200
        else:
            failed_predictions.inc()
            prediction_errors_total.labels(error_type='model_error').inc()
            logger.error(f"Model returned error: {response.status_code}")
            return jsonify({"error": f"Model error: {response.text}"}), response.status_code
            
    except requests.exceptions.Timeout:
        failed_predictions.inc()
        prediction_errors_total.labels(error_type='timeout').inc()
        logger.error("Request to model timed out")
        return jsonify({"error": "Model request timeout"}), 504
        
    except requests.exceptions.ConnectionError:
        failed_predictions.inc()
        prediction_errors_total.labels(error_type='connection_error').inc()
        logger.error("Cannot connect to model")
        return jsonify({"error": "Cannot connect to model service"}), 503
        
    except Exception as e:
        failed_predictions.inc()
        prediction_errors_total.labels(error_type='unknown').inc()
        logger.error(f"Prediction error: {str(e)}")
        return jsonify({"error": str(e)}), 500
        
    finally:
        active_requests.dec()

@app.route('/metrics', methods=['GET'])
def metrics():
    """
    Expose Prometheus metrics endpoint
    This is scraped by Prometheus every 5 seconds
    """
    # Update uptime metric
    uptime = time.time() - SERVICE_START_TIME
    model_uptime_seconds.set(uptime)
    
    return generate_latest(), 200, {'Content-Type': CONTENT_TYPE_LATEST}

@app.route('/health', methods=['GET'])
def health():
    """Health check endpoint"""
    return jsonify({
        "status": "healthy",
        "uptime_seconds": time.time() - SERVICE_START_TIME
    }), 200

if __name__ == '__main__':
    logger.info("Starting Prometheus Exporter for MLflow Model")
    logger.info(f"Model endpoint: {MLFLOW_MODEL_URL}")
    logger.info("Metrics endpoint: /metrics")
    logger.info("Prediction endpoint: /predict")
    app.run(host='0.0.0.0', port=5000, debug=False)
