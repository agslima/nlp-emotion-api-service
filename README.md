# AI Emotion Detector Web App

![CD/CD Status](https://github.com/agslima/nlp-emotion-api-service/actions/workflows/ci-cd.yml/badge.svg)
[![Python 3.10](https://img.shields.io/badge/Python-3.10-blue.svg)](https://python.org)
[![Flask](https://img.shields.io/badge/Backend-Flask-lightgrey.svg)](https://flask.palletsprojects.com/)
[![Docker](https://img.shields.io/badge/Deployment-Docker-blue.svg)](https://docker.com)
[![IBM Watson](https://img.shields.io/badge/AI-IBM%20Watson-052FAD.svg)](https://www.ibm.com/watson)
[![License](https://img.shields.io/badge/License-Apache%202.0-lightgrey.svg)](https://opensource.org/licenses/Apache-2.0)

## Introduction

This project is a **Full-Stack AI Application** that detects and quantifies emotions from text input. 

Leveraging **IBM Watson's Embeddable AI** libraries, it goes beyond simple sentiment analysis (positive/negative) to identify fine-grained emotional states. The application is containerized with Docker, ensuring consistency across development and production environments.

**Key Capabilities:**
* **Fine-Grained Analysis:** Detects specific emotions: 😊 Joy, 😢 Sadness, 😡 Anger, 😨 Fear, and 🤢 Disgust.
* **Microservice Architecture:** Decoupled backend (Flask) and frontend logic.
* **Production Ready:** Fully containerized using Docker and orchestrated via Docker Compose.

### Use Cases 📉
Such emotion-aware systems are critical for:
* **Customer Experience:** Automated triage of angry support tickets.
* **Market Research:** Analyzing product reviews for specific pain points.
* **Mental Health:** Early detection of distress signals in text.

## Technologies & Architecture

| Component | Technology | Description |
|-----------|------------|-------------|
| **AI Engine** | **IBM Watson NLP** | Library for emotion extraction logic. |
| **Backend** | **Flask (Python)** | REST API handling requests and logic. |
| **Frontend** | **HTML/JS/AJAX** | Asynchronous UI for real-time results. |
| **Container** | **Docker** | Ensures portability and easy deployment. |
| **Testing** | **Unittest** | Python's built-in framework for logic validation. |



## Project Structure

The project follows a modular structure suitable for microservices:

```text
final-project-emb-ai/
├── backend/
│   ├── EmotionDetection/   <- AI Logic Package
│   │   ├── __init__.py
│   │   └── emotion_detection.py
│   ├── server.py           <- Flask Application Entrypoint
│   ├── requirements.txt    <- Python Dependencies
│   └── Dockerfile          <- Container Definition
├── frontend/
│   ├── index.html          <- User Interface
│   └── static/             <- Client-side Assets
│       └── mywebscript.js
└── docker-compose.yml      <- Orchestration Config
```

---

### How to Run 🚀
​
**Prerequisites**

​Docker & Docker Compose installed.
​An active IBM Watson library or API Mock (as configured in the course).

**​1. Clone the Repository**

```bash
git clone [https://github.com/your-username/final-project-emb-ai.git](https://github.com/your-username/final-project-emb-ai.git)
cd final-project-emb-ai
```

**2. Deployment with Docker**

​The easiest way to run the application is to use Docker Compose, which automatically builds the image and maps the ports.

```bash
docker-compose up --build
```

**3. Access the Application**
​Once the container is running, open your browser:
👉 http://localhost:5000

---

### Testing​ 🧪

​Unit tests are included to ensure the reliability of the emotion detection logic. To run tests inside the container (or locally):

```bash
# If running locally with python installed
python3 -m unittest backend/tests/test_emotion_detection.py

# OR via Docker (if configured)
docker exec -it <container_id> python3 -m unittest discover
```

---

### Example Output 📊

​Input Text:
​"I am really mad about this service!"
**​System Response:**

```json
{
  "anger": 0.85,
  "disgust": 0.05,
  "fear": 0.03,
  "joy": 0.01,
  "sadness": 0.06,
  "dominant_emotion": "anger"
}
```
<br>
<p align="center">
  <img src=".files/app_img.png" alt="NPL Response" width="600"/>
</p>
<br>

<!--
**GIF Demonstration:**

![GIF placeholder](https://via.placeholder.com/800x400?text=App+Interaction+GIF)
-->

---

### License⚖️

This project is licensed under the Apache 2.0 License.
Based on the curriculum for the IBM DevOps and Software Engineering Professional Certificate.
