FROM python:latest

WORKDIR /bot

COPY /Bot .

RUN pip install -r requirements.txt --no-index


CMD ["python", "Discord.py"]
