#!/bin/sh

echo "Waiting for database..."
while ! nc -z db 5432; do
  sleep 0.1
done
echo "Database started"

echo "Applying migrations..."
python manage.py makemigrations --noinput
python manage.py migrate --noinput

echo "Starting server..."
exec "$@"