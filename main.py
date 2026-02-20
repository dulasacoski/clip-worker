from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"status": "Worker online"}

@app.post("/process")
def process(data: dict):
    # Por enquanto só valida que chegou.
    # Depois você troca isso por yt-dlp + Whisper + FFmpeg.
    return {"ok": True, "received": data}