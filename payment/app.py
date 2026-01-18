from fastapi import FastAPI, HTTPException
import requests
import time
import random
import os
import uvicorn

app = FastAPI()

VERSION = os.environ["VERSION"]
POD_IP = os.environ.get("POD_IP", "unknown")

AUTH_SERVICE_URL = "http://auth:8080"

@app.get("/health")
def health():
    return {
        "status": "ok",
        "service": "payment",
        "version": VERSION,
        "pod_ip": POD_IP
    }

@app.post("/payment/process")
def process_payment(token: str, amount: float):
    try:
        resp = requests.get(
            f"{AUTH_SERVICE_URL}/auth/validate",
            params={"token": token},
            timeout=1
        )
    except requests.RequestException:
        raise HTTPException(status_code=503, detail="Auth service unavailable")

    if resp.status_code != 200:
        raise HTTPException(status_code=403, detail="Unauthorized")

    time.sleep(0.3)

    if VERSION == "v2" and random.random() < 0.3:
        raise HTTPException(status_code=500, detail="Random payment failure (canary)")

    return {
        "status": "payment_success",
        "amount": amount,
        "version": VERSION,
        "pod_ip": POD_IP
    }

if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8080)
