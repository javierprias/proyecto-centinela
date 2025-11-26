FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY ./app ./app
# Bandit (seguridad) se quejará si corremos esto como root, pero por ahora está bien
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]