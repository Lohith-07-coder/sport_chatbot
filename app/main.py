from fastapi import FastAPI, HTTPException
from .models import ChatRequest, ChatResponse, Message
from .logic import generate_bot_response
from .memory import conversations
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

app = FastAPI(title="Sports Chatbot")

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
def serve_frontend():
    return FileResponse("static/index.html")

@app.get("/ping")
def ping():
    return {"status": "ok", "message": "Chatbot is online!"}

@app.post("/chat", response_model=ChatResponse)
def chat(req: ChatRequest):
    user_id = req.user_id
    user_msg = Message(role="user", content=req.message)
    bot_reply = generate_bot_response(req.message)
    bot_msg = Message(role="bot", content=bot_reply)

    conversations.setdefault(user_id, []).extend([user_msg, bot_msg])
    return ChatResponse(response=bot_reply, conversation_history=conversations[user_id])

@app.get("/history/{user_id}", response_model=list[Message])
def get_history(user_id: str):
    if user_id not in conversations:
        raise HTTPException(status_code=404, detail="User not found")
    return conversations[user_id]

@app.delete("/reset/{user_id}")
def reset(user_id: str):
    conversations[user_id] = []
    return {"message": f"Conversation with '{user_id}' has been reset."}

@app.get("/")
def root():
    return {"message": "Welcome to the Sports Chatbot API. Visit /docs to explore the API."}
