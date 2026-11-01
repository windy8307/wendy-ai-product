import os
from fastapi import FastAPI, Request, HTTPException
from linebot.v3.webhook import WebhookParser
from linebot.v3.exceptions import InvalidSignatureError

app = FastAPI(title="WENDY LINE System")

@app.get("/")
def home():
    return {"service": "WENDY LINE System", "status": "running"}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/callback")
async def callback(request: Request):
    secret = os.getenv("LINE_CHANNEL_SECRET")
    if not secret:
        raise HTTPException(status_code=503, detail="LINE secret not configured")
    signature = request.headers.get("x-line-signature", "")
    body = (await request.body()).decode("utf-8")
    try:
        WebhookParser(secret).parse(body, signature)
    except InvalidSignatureError:
        raise HTTPException(status_code=400, detail="Invalid signature")
    return {"status": "ok"}
