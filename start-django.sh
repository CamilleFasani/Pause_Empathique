#!/bin/bash
poetry run python manage.py collectstatic --noinput
poetry run python manage.py migrate

if [[ "$ENV_STATE" == "production" ]]; then
    poetry run gunicorn pause_empathique.wsgi --workers $GUNICORN_WORKERS --forwarded-allow-ips -"*"
else
    poetry run python manage.py runserver 0.0.0.0:8000
fi