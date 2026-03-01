from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from agent_service import agent

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Message(BaseModel):
    message: str

@app.post("/chat")
async def chat(msg: Message):
    """נקודת קצה לשליחת הודעות ל-agent"""
    try:
        response = agent(msg.message)
        return {"response": response}
    except Exception as e:
        return {"response": f"שגיאה: {str(e)}"}


@app.get("/")
async def root():
    return {"message": "Task Manager Agent API 🤖"}
