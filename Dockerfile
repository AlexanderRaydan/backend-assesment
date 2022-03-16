FROM python:3.8

ENV PYTHONUNBUFFERED 1
COPY . /app

COPY requirements.txt requirements.txt 
RUN pip3 install -r requirements.txt

COPY start.sh start.sh 
RUN chmod +x /start.sh

WORKDIR /app

EXPOSE 8000