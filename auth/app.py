from fastapi import FastAPI, HTTPException
import time
import os
import uvicorn

app = FastAPI()

VERSION = os.environ["VERSION"]
POD_IP = os.environ.get("POD_IP", "unknown")

@app.get("/health")
def health():
    return {
        "status": "ok",
        "service": "auth",
        "version": VERSION,
        "pod_ip": POD_IP
    }

@app.post("/auth/login")
def login(username: str, password: str):
    time.sleep(0.2)

    if username == "admin" and password == "password":
        return {
            "token": "fake-jwt-token",
            "version": VERSION,
            "pod_ip": POD_IP
        }

    raise HTTPException(status_code=401, detail="Invalid credentials")

@app.get("/auth/validate")
def validate(token: str):
    if token != "fake-jwt-token":
        raise HTTPException(status_code=403, detail="Invalid token")

    return {
        "valid": True,
        "version": VERSION,
        "pod_ip": POD_IP
    }

if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8080)
