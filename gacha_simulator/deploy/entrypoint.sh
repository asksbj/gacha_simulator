#!/bin/bash -e

exec /usr/local/bin/gunicorn \
        --workers ${PYTHON_THREADS:-4}  \
        --pid /var/run/gunicorn.pid \
        --bind 0.0.0.0:80 \
        --keep-alive 5 \
        --limit-request-line 16384 \
        --limit-request-field_size 16384 \
        --timeout 300 \
        --log-level debug  \
        gacha_simulator.wsgi:application