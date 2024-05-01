FROM python:3.7-slim

LABEL maintainer="https://suk.kr"

WORKDIR /app

RUN pip install flask

COPY app.py /app/app.py

CMD ["python", "/app/app.py"]