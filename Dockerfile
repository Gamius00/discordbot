FROM python:3.13

WORKDIR /bot

COPY /Bot .

RUN pip install -r requirements.txt


CMD ["python", "Discord.py"]
