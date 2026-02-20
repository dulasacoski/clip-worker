from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class ProcessRequest(BaseModel):
    youtube_url: str

@app.get("/")
def root():
    return {"status": "Worker online"}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/process")
def process(req: ProcessRequest):
    # Aqui depois entra yt-dlp + transcrição + ffmpeg
    return {
        "message": "Processamento iniciado",
        "youtube_url": req.youtube_url
    }