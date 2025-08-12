#!/bin/sh
set -e
python manage.py migrate
python manage.py create_default_superuser