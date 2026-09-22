# 🚀 End-to-End MLOps Pipeline for Insurance Data Prediction

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Machine Learning](https://img.shields.io/badge/Machine%20Learning-AI-orange)
![MLOps](https://img.shields.io/badge/MLOps-Prometheus%20%7C%20Grafana-green)

## Project Overview

This repository showcases an end-to-end Machine Learning Operations (MLOps) pipeline developed for insurance data prediction.

The project covers the complete machine learning lifecycle, including data preparation, model development, model optimization, inference workflow, monitoring, and system observability.

The main objective is to build a reliable and maintainable machine learning system by integrating machine learning development practices with monitoring and operational workflows.

> This project was developed as the final capstone project for the Dicoding course **"Building Machine Learning Systems"**.

---

## 🏆 Achievement

This final project successfully achieved all Advanced Criteria requirements and received the highest score:

**⭐ 5/5 Stars**

<img width="1154" height="644" alt="Project Achievement" src="https://github.com/user-attachments/assets/169f41ee-b4fc-408b-84db-9d69cf2d8a91" />

---

## 🌟 Project Highlights

- End-to-end machine learning lifecycle implementation.
- Data preprocessing and feature preparation workflow.
- Machine learning model development and optimization.
- Hyperparameter tuning process.
- Model inference workflow simulation.
- Prometheus and Grafana monitoring integration.
- System metrics visualization and observability.
- Threshold-based alerting mechanism.
- Continuous Integration (CI) workflow documentation.

---

# ✨ Key Features & Technical Scope

## 🧠 End-to-End Machine Learning Pipeline

The project implements a structured workflow covering:

- Data preparation
- Data preprocessing
- Feature engineering
- Model development
- Model optimization
- Model inference


## ⚙️ Model Development & Optimization

The machine learning development process includes:

- Model training
- Model experimentation
- Hyperparameter tuning
- Model evaluation
- Model artifact generation


## 🚀 Model Inference Workflow

Implemented inference workflow to simulate machine learning prediction services.

The inference system allows the trained model to be executed and monitored through an operational workflow.


## 📊 Monitoring & Logging System

Integrated monitoring infrastructure using:

- Prometheus
- Grafana


The monitoring system tracks:

- Model inference activity
- Application performance metrics
- System health indicators
- Operational behavior


## 🔔 Alerting Mechanism

Implemented threshold-based alerting using Grafana to identify:

- Performance degradation
- System anomalies
- Operational issues


## 🔄 Workflow Governance

The project includes workflow documentation to support:

- Experiment reproducibility
- Continuous Integration (CI)
- Structured development process

---

# 🛠️ Technology Stack

## Programming Language

- Python


## Machine Learning

- Scikit-learn
- Pandas
- NumPy


## MLOps & Monitoring

- Prometheus
- Grafana


## Engineering Tools

- Git
- Continuous Integration Workflow
- Docker (Monitoring Environment)

---

# 📂 Repository Structure

```

SMSML_JihanKusumawardhani/

│
├── Membangun Model/
│   │
│   ├── modelling.py
│   ├── modelling_tuning.py
│   ├── requirements.txt
│   └── preprocessing/
│
├── Monitoring dan Logging/
│   │
│   ├── inference.py
│   ├── prometheus_exporter.py
│   ├── prometheus.yml
│   ├── monitoring_prometheus/
│   ├── monitoring_grafana/
│   └── alerting_grafana/
│
├── Workflow-CI.txt
│
└── README.md

````

---

# ⚙️ Installation & Setup

## Prerequisites

Before running this project, ensure the following requirements are installed:

- Python 3.x
- Docker (recommended for monitoring environment)
- Git


---

## Clone Repository

```bash
git clone <repository-url>

cd SMSML_JihanKusumawardhani
````

---

## Install Dependencies

```bash
pip install -r "Membangun Model/requirements.txt"
```

---

# 🚀 Running Project

## 1. Model Development

Run the model development script:

```bash
python "Membangun Model/modelling.py"
```

The process will perform:

* Data preparation
* Model training
* Model saving

---

## 2. Model Optimization

Run hyperparameter tuning:

```bash
python "Membangun Model/modelling_tuning.py"
```

This process evaluates model configurations to improve performance.

---

## 3. Run Inference Service

Start the inference workflow:

```bash
python "Monitoring dan Logging/inference.py"
```

The inference process simulates prediction requests and exposes metrics for monitoring.

---

## 4. Monitoring System

Launch monitoring services using:

* Prometheus
* Grafana

Prometheus configuration:

```
Monitoring dan Logging/prometheus.yml
```

The monitoring dashboard provides visualization of:

* Application metrics
* Inference performance
* Operational monitoring data

---

# 📷 Project Documentation

The repository contains documentation and evidence including:

* Model development results
* Model evaluation results
* Prometheus monitoring visualization
* Grafana dashboard visualization
* Alerting configuration evidence

---

# 📚 Learning Outcomes

Through this project, I gained experience in:

* Building end-to-end machine learning workflows.
* Developing and optimizing predictive models.
* Implementing machine learning inference systems.
* Applying MLOps concepts for monitoring and observability.
* Understanding machine learning lifecycle management.
* Implementing engineering practices for reliable AI systems.

---

# 🔐 Security Notes

This repository is intended for demonstration and learning purposes.

Sensitive information such as:

* API keys
* Credentials
* Private configuration files
* Proprietary datasets

should not be included in public repositories.

---

# 📝 License

This project is released under the MIT License.

---

# 👨‍💻 Author

**Jihan Kusumawardhani**

Informatics Engineering Graduate

Interested in:

* Web Development
* Artificial Intelligence
* Machine Learning
* MLOps
* Data-driven Application Development

GitHub:

[https://github.com/jihanbuildspace](https://github.com/jihanbuildspace)

```
```
