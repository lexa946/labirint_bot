FROM python:3.12-slim
LABEL authors="pozhar"

ENTRYPOINT ["top", "-b"]

COPY . .


RUN pip install -r requirements.txt

CMD ["python3", "start_bot.py"]