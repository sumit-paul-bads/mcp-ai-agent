from fastapi import FastAPI
from agent import agent_response

app = FastAPI()

@app.get("/")
def home():
    return {"message": "AI Agent is running"}

@app.get("/query")
def query(q: str):
    response = agent_response(q)
    return {"response": response}