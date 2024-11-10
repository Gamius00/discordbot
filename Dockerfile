FROM python:latest

WORKDIR /bot

COPY /Bot .

RUN pip install discord asyncio datetime python-dotenv audioop


CMD ["python", "Discord.py"]
