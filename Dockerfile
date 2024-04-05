FROM python:3.12

WORKDIR /app

COPY . .

RUN python -m pip install --no-cache-dir -r ./requirements.txt --verbose

EXPOSE 8000

CMD ["gunicorn", "app:app", "--workers", "4", "--worker-class", "uvicorn.workers.UvicornWorker", "--bind", "0.0.0.0:8000"]