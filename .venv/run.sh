#!/bin/sh
set -e
gunicorn projct.wsgi --log-file - 