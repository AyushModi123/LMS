FROM python:3.11

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r ./requirements.txt

EXPOSE 8000

CMD ["gunicorn", "app:app", "--workers", "4", "--worker-class", "uvicorn.workers.UvicornWorker", "--bind", "0.0.0.0:8000"]