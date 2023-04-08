FROM python:latest

WORKDIR /bot

COPY . .

RUN pip install discord asyncio datetime python-dotenv

CMD ["python", "./Bot/Discord.py"]
