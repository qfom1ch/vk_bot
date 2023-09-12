FROM python:3.10

RUN mkdir /vk_bot

WORKDIR /vk_bot

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD python bot.py
