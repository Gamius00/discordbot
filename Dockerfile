FROM python:3.9

WORKDIR /bot

COPY /Bot .

RUN pip install -r requirements.txt


CMD ["python", "Discord.py"]
