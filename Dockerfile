FROM python:3.12-slim-bookworm

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Копируем папку src (где manage.py) в /app
COPY src /app

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]