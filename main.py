from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from openai import OpenAI
import os

app = FastAPI()

# CORS
origins = [
    "https://ibrahimkayral.com",
    "https://www.ibrahimkayral.com",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

class ChatRequest(BaseModel):
    message: str

SYSTEM_PROMPT = """
Sen, Doç. Dr. İbrahim H. Kayral’ın asistanısın.
Uzmanlık alanların: sağlık yönetimi, hasta güvenliği, kalite, akreditasyon,
liderlik, motivasyon, strateji ve girişimciliktir.
Yanıtlarında:
- Bilimsel ve güncel kal,
- Türkçe’yi düzgün ve anlaşılır kullan,
- Klinik tanı ve tedavi önermeden, sistem ve yönetim odaklı yanıt ver.
"""

@app.get("/")
def read_root():
    return {"message": "Kayral AI Backend çalışıyor hocam!"}

@app.post("/ask")
async def ask(req: ChatRequest):
    try:
        response = client.responses.create(
            model="gpt-4o-mini",
            input=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": req.message},
            ],
        )
        answer = response.output_text
        return {"answer": answer}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
