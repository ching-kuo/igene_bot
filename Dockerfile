FROM python:3

RUN git clone https://github.com/iGene/igene_bot
RUN pip install -r igene_bot/requirements.txt
CMD [ "python", "igene_bot/bot.py" ]
