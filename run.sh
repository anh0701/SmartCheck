#!/bin/bash

source venv/bin/activate
python src/app.py

# podman-compose up --build
# podman-compose build flask-api
# podman restart smart-check-api