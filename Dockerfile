FROM --platform=linux/amd64 python:3.10-slim

WORKDIR /app

ADD . /app

RUN pip install -r requirements.txt

CMD ["python3", "app.py"]