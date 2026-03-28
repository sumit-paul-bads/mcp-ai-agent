# AI Text Summarization Agent
A serverless Python microservice deployed on **Google Cloud Run** using **FastAPI** and **Google Gemini 1.5/2.0 Flash**.

## 🚀 Features
- **Containerized**: Fully Dockerized for consistent deployment.
- **Serverless**: Hosted on Google Cloud Run (scales to zero).
- **AI-Powered**: Uses Google's Generative AI for high-quality text summarization.

## 🛠️ Tech Stack
- **Language**: Python 3.11
- **Framework**: FastAPI & Uvicorn
- **Infrastructure**: Google Cloud Platform (GCP), Artifact Registry
- **DevOps**: Docker, Cloud Build

## 📖 How to Use
Send a POST request to the endpoint:
```bash
curl -X POST "https://YOUR_CLOUD_RUN_URL/ask" \
-H "Content-Type: application/json" \
-d '{"text": "Your long text here..."}'
```
