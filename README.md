# 🚀 Advanced MLOps: Monitoring, Logging, and Modelling System for Insurance Data Prediction

## Project Overview

This repository showcases the implementation of a **comprehensive, production-ready Machine Learning Operations (MLOps) pipeline** specifically engineered for high-fidelity insurance data prediction. The project's core focus is on ensuring **operational stability, system observability, and model reproducibility** alongside achieving high predictive accuracy.

It encompasses the entire lifecycle: from advanced data engineering and robust model development to the deployment of a real-time monitoring infrastructure. **This project rigorously implements all Advanced Criteria requirements** set for the course, ensuring a scalable and production-ready solution.

> **Note:** This project serves as the final capstone deliverable for the Dicoding course, "Building Machine Learning Systems."

---

## 🌟 Achievement

**This Final Project successfully met all Advanced Criteria and was awarded the highest score: 5/5 Stars.**

---

## ✨ Key Features & Technical Scope

* **End-to-End ML Pipeline:** Structured workflow covering data preprocessing, feature engineering, and model deployment readiness.
* **Performance Optimization:** Systematic model development and exhaustive hyperparameter tuning to maximize predictive performance metrics (e.g., AUC, F1-Score).
* **Real-Time Observability (Advanced Criteria):** Seamless integration of the **Prometheus-Grafana stack** for continuous tracking of critical metrics:
    * Model Inference Latency and Throughput.
    * Operational Model Performance (monitoring for **model drift**).
    * System Health and Resource Utilization.
* **Proactive Alerting (Advanced Criteria):** Implementation of threshold-based alerting within Grafana for immediate notification of system anomalies or performance degradation.
* **Workflow Governance:** Detailed documentation of experiments and Continuous Integration (CI) workflows to guarantee full reproducibility.

---

## 📂 Repository Structure

The project is logically organized into modeling and MLOps components:

| Directory/File | Description |
| :--- | :--- |
| `ml_modeling/` | **Core Machine Learning scripts** for model building, tuning, and data preparation. |
| ├── `modelling.py` | Primary script for model training and saving. |
| ├── `modelling_tuning.py` | Scripts for hyperparameter optimization and evaluation. |
| ├── `requirements.txt` | Python dependencies required for model execution. |
| `monitoring_logging/` | **MLOps Configuration and Observability Evidence.** |
| ├── `prometheus.yml` | Configuration file for Prometheus server. |
| ├── `prometheus_exporter.py` | Custom Python script to expose model metrics to Prometheus. |
| ├── `inference.py` | Script simulating model inference/prediction with metric exposure. |
| `docs/` | Comprehensive documentation and evidence of the project. |
| ├── `Workflow-CI.txt` | Detailed documentation of Continuous Integration steps. |
| ├── `Experiment-Logs.txt` | Comprehensive logs and notes from the modeling experiments. |
| ├── `bukti_monitoring_prometheus/` | Screenshots/Evidence of metrics pulled by Prometheus. |
| ├── `bukti_monitoring_grafana/` | Visual evidence of Grafana performance dashboards. |
| ├── `bukti_alerting_grafana/` | Evidence demonstrating the automated alerting mechanism. |

---

## ⚙️ Quick Start

### Prerequisites
* Python 3.x
* Docker (Recommended for easier deployment of Prometheus/Grafana)

### Installation

1.  **Clone the repository:**
    ```bash
    git clone <your-repo-url>
    cd <your-repo-folder>
    ```

2.  **Install Python dependencies:**
    ```bash
    pip install -r "ml_modeling/requirements.txt"
    ```

3.  **Run Model Training:**
    Execute the training script to generate the model artifact:
    ```bash
    python "ml_modeling/modelling.py"
    ```

### Running the Monitoring Stack

1.  **Start the Inference Script & Exporter:**
    The `inference.py` script simulates production traffic and exposes real-time metrics via the custom exporter.
    ```bash
    python "monitoring_logging/inference.py"
    ```
    *(Ensure the script runs on the port configured in `prometheus.yml`)*

2.  **Launch Prometheus and Grafana:**
    Use Docker Compose (recommended) or launch Prometheus manually using the configuration file:
    ```bash
    # Example using Prometheus CLI (requires manual install)
    prometheus --config.file="monitoring_logging/prometheus.yml"
    ```

3.  **View Dashboard:**
    Access the configured Grafana URL and import the dashboards to visualize the metrics and observe alerts. Refer to the evidence in `docs/` for expected outputs.

---

## 🛑 Important Notes

* **Security:** This repository is intended for demonstration. In a production setting, ensure all API keys, sensitive configurations, and raw proprietary data are strictly excluded from public version control.
* **Versioning:** Consider adopting tools like **MLflow** or **DVC** for superior experiment tracking and data versioning in future iterations.

---

## 📝 License

This project is released under the **[MIT License](LICENSE.md)**