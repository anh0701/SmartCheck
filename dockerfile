FROM python:3.11.2

WORKDIR /app

# COPY src/ /app
# COPY models/ /app/models

COPY requirements.txt /app/
RUN apt-get update && \
    apt-get install -y libgl1 libglib2.0-0 && \
    pip install -r requirements.txt


CMD ["python", "app.py"]