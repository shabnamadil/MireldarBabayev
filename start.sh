#!/bin/bash

echo "Applying migrations..."
python3 manage.py makemigrations user
python3 manage.py migrate

echo "Starting uWSGI..."
exec "$@"
