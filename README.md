# 🚀 MCP AI Agent — Cloud Run Deployment

## 📌 Overview

This project demonstrates the end-to-end development and deployment of an AI-powered agent capable of processing natural language queries and returning real-time responses.

The application is containerized using Docker and deployed on Google Cloud Run, ensuring scalability, availability, and production-grade execution.

The agent currently handles queries such as weather-related questions and returns structured JSON responses via API endpoints.

---

## 🎯 Problem Statement

Modern applications require intelligent systems that can:

- Interpret user queries dynamically
- Fetch real-time data
- Scale seamlessly without infrastructure overhead

This project addresses these needs by building a lightweight AI agent and deploying it using serverless architecture.

---

## 🧠 Solution

- Built a Python-based AI agent using FastAPI
- Designed API endpoints to process natural language queries
- Integrated real-time response generation (weather-based queries)
- Containerized the application using Docker
- Deployed using Google Cloud Run (fully managed serverless platform)

---

## ⚙️ Tech Stack

- Backend: Python, FastAPI
- Deployment: Google Cloud Run
- Containerization: Docker
- Cloud Services: Cloud Build, Artifact Registry, IAM
- Version Control: Git, GitHub

---

## 🏗️ Architecture

User Query → FastAPI Endpoint → AI Logic Processing → External Data Handling → JSON Response → Cloud Run Deployment

---

## 🚀 Features

- Real-time query processing
- REST API-based interaction
- Scalable serverless deployment
- Lightweight and modular code structure
- Dockerized for portability

---

## 📂 Project Structure

.
├── main.py              # FastAPI entry point
├── agent.py             # Core AI agent logic
├── tool.py              # Utility functions
├── requirements.txt     # Dependencies
├── Dockerfile           # Container setup
├── README.md            # Documentation
└── error_log.txt        # Logs

---

## 🔧 Installation & Setup (Local)

1. Clone the repository

git clone https://github.com/sumit-paul-bads/mcp-ai-agent.git
cd mcp-ai-agent

2. Create virtual environment

python -m venv venv
source venv/bin/activate

3. Install dependencies

pip install -r requirements.txt

4. Run locally

uvicorn main:app --reload --port 8080

---

## 🌐 API Usage

Base URL (Cloud Run)

https://mcp-agent-1071353792038.asia-south1.run.app

Example Endpoint

/query?q=weather in Kolkata

Sample Response

{
  "response": "Weather in Kolkata is 24.97°C with haze."
}

---

## ☁️ Deployment (Google Cloud Run)

Steps:

1. Enable required APIs:
   
   - Cloud Run
   - Cloud Build
   - Artifact Registry

2. Deploy using:

gcloud run deploy mcp-agent \
--source . \
--platform managed \
--region asia-south1 \
--allow-unauthenticated

3. Access service via generated URL

---

## ⚠️ Challenges Faced

- IAM permission errors during deployment
- Cloud Build service account authorization issues
- GitHub authentication (token-based login instead of password)
- Handling secure credential input in terminal

---

## 📊 Key Learnings

- Hands-on experience with serverless deployment
- Understanding IAM roles and permissions in GCP
- Containerizing applications using Docker
- Managing GitHub authentication securely
- Debugging real-world deployment issues

---

## 📸 Screenshots

(Add your 5 images here)

- Cloud Run Deployment
- Terminal Logs
- API Output
- GitHub Repository
- Local Testing

---

## 🔮 Future Improvements

- Add more AI capabilities (NLP models, LLM integration)
- Improve response accuracy
- Add authentication layer
- Build frontend UI
- Logging and monitoring integration

---

## 👤 Author

Sumit Paul
GitHub: https://github.com/sumit-paul-bads

---

⭐ If you found this useful

Give this repo a ⭐ and connect with me!
