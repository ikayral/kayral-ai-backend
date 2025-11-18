from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class ChatRequest(BaseModel):
    message: str

@app.get("/")
def read_root():
    return {"message": "Kayral AI Backend çalışıyor hocam!"}

@app.post("/ask")
async def ask(req: ChatRequest):
    # Şimdilik sadece gelen mesajı geri döndürüyoruz
    return {"answer": f"Gelen mesaj: {req.message}"}
