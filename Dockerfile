FROM python:3.6.5-slim

COPY . igene_bot/
RUN pip install -r igene_bot/requirements.txt
CMD [ "python", "igene_bot/bot.py" ]
