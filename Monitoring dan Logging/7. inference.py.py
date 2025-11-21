"""
Inference Test Script
Sends prediction requests to the model serving endpoint
Generates metrics data for Prometheus and Grafana
"""

import requests
import json
import time
import random

# Model serving endpoint
MODEL_URL = "http://localhost:5000/predict"

# Sample insurance data for testing
# Model expects 11 features (one-hot encoded: age, bmi, children, sex_male, smoker_yes, region_northeast, region_northwest, region_southeast, region_southwest, + 2 more)
# Using MLflow 2.0+ format with inputs wrapper
sample_data = [
    # Valid requests with 11 features each
    {"inputs": [[19, 27.9, 0, 1, 1, 0, 0, 0, 1, 0, 0]]},  # Young smoker, southwest
    {"inputs": [[33, 22.7, 0, 0, 0, 0, 0, 1, 0, 0, 0]]},  # Middle-age non-smoker, southeast  
    {"inputs": [[45, 28.3, 2, 1, 0, 0, 1, 0, 0, 0, 0]]},  # Middle-age with kids, northwest
    {"inputs": [[52, 34.5, 3, 0, 1, 1, 0, 0, 0, 0, 0]]},  # Older smoker with kids, northeast
    {"inputs": [[27, 19.6, 1, 1, 0, 0, 0, 0, 1, 0, 0]]},  # Young with child, southwest
]

def send_prediction(data, request_num):
    """Send a prediction request and track results"""
    try:
        start_time = time.time()
        response = requests.post(MODEL_URL, json=data, timeout=10)
        duration = time.time() - start_time
        
        if response.status_code == 200:
            result = response.json()
            print(f"✓ Request {request_num}: SUCCESS in {duration:.3f}s - Result: {result}")
            return True
        else:
            print(f"✗ Request {request_num}: ERROR {response.status_code} - {response.text}")
            return False
    except requests.exceptions.Timeout:
        print(f"✗ Request {request_num}: TIMEOUT")
        return False
    except requests.exceptions.ConnectionError:
        print(f"✗ Request {request_num}: CONNECTION ERROR")
        return False
    except Exception as e:
        print(f"✗ Request {request_num}: EXCEPTION - {str(e)}")
        return False

def generate_invalid_request():
    """Generate invalid request to test error handling"""
    invalid_types = [
        {},  # Empty request
        {"inputs": []},  # Empty data
        {"inputs": [[]]},  # Empty array
        {"inputs": [[1, 2, 3]]},  # Wrong number of features (only 3 instead of 11)
    ]
    return random.choice(invalid_types)

def main():
    print("=" * 70)
    print("INSURANCE MODEL INFERENCE TEST")
    print("=" * 70)
    print(f"Target: {MODEL_URL}")
    print(f"Starting test run with 60 requests (50 valid + 10 invalid)")
    print("=" * 70)
    print()
    
    success_count = 0
    error_count = 0
    total_requests = 60
    
    # Send valid requests
    print("Sending VALID requests...")
    for i in range(50):
        data = random.choice(sample_data)
        result = send_prediction(data, i + 1)
        if result:
            success_count += 1
        else:
            error_count += 1
        time.sleep(0.1)  # Small delay between requests
    
    print()
    print("Sending INVALID requests to test error handling...")
    # Send invalid requests to generate errors
    for i in range(10):
        invalid_data = generate_invalid_request()
        result = send_prediction(invalid_data, 50 + i + 1)
        if not result:
            error_count += 1
        time.sleep(0.1)
    
    print()
    print("=" * 70)
    print("TEST SUMMARY")
    print("=" * 70)
    print(f"Total Requests:     {total_requests}")
    print(f"Successful:         {success_count}")
    print(f"Errors:             {error_count}")
    print(f"Success Rate:       {(success_count/total_requests)*100:.1f}%")
    print("=" * 70)
    print()
    print("Metrics are now available at:")
    print("  - Prometheus: http://localhost:9090")
    print("  - Grafana:    http://localhost:3001")
    print()
    print("You can now take screenshots for submission!")
    print("=" * 70)

if __name__ == "__main__":
    main()
