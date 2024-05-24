# Dockerfile para el Contenedor 2 (Servicio de Autenticación)
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "auth_service.py"]
