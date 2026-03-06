#!/bin/bash
poetry run python manage.py collectstatic --noinput
poetry run python manage.py migrate

if [[ "$ENV_STATE" == "production" ]] || [[ "$ENV_STATE" == "staging" ]]; then
    poetry run gunicorn pause_empathique.wsgi:application --bind "0.0.0.0:${PORT:-8000}" --forwarded-allow-ips "*"
else
    poetry run python manage.py runserver 0.0.0.0:8000
fi