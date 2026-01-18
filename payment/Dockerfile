FROM python:3.11-slim

WORKDIR /app
COPY app.py .

RUN pip install fastapi uvicorn requests

# Document the application port
EXPOSE 8080

CMD ["python", "app.py"]
