FROM python:3.10-slim-buster

# Install system dependencies needed for psycopg2
RUN apt-get update && apt-get install -y \
    libpq-dev gcc && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . .
EXPOSE 5000
CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]
 