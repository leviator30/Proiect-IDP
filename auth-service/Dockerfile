# Folosim o imagine oficială de Python ușoară
FROM python:3.10-slim

# Setăm directorul de lucru în container
WORKDIR /app

# Copiem fișierul cu dependențe (îl vom crea la pasul următor)
COPY requirements.txt .

# Instalăm librăriile necesare
RUN pip install --no-cache-dir -r requirements.txt

# Copiem codul sursă al microserviciului
COPY auth_service.py .

# Expunem portul pe care rulează FastAPI (standard este 8000)
EXPOSE 8000

# Comanda de pornire a serviciului
CMD ["uvicorn", "auth_service:app", "--host", "0.0.0.0", "--port", "8000"]