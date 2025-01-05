FROM python:3.12.7-slim-bookworm

COPY requirements.txt /tmp/
RUN pip install --requirement /tmp/requirements.txt

COPY . /app
WORKDIR /app

EXPOSE 5000
CMD ["python", "app.py"]
