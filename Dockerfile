FROM python:latest

WORKDIR /bot

COPY .env .env

COPY /Bot .

RUN pip install -r requirements.txt


CMD ["python", "Discord.py"]
