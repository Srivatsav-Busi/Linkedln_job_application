FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py ./
COPY templates/ ./templates/

ENV APPLIED_JOBS_PATH="all excels/"
EXPOSE 5000

CMD ["python", "app.py"]
