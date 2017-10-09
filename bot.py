# -*- coding: utf-8 -*-

from telegram.ext import Updater
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters, RegexHandler,
                          ConversationHandler)
from bs4 import BeautifulSoup
from configparser import ConfigParser
from models import *
import logging
import re
import requests

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)


def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="I'm a bot, please talk to me!")

def main():
    cfg = ConfigParser()
    cfg.read('config')
    token = cfg.get('auth', 'token')
    updater = Updater(token)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(RegexHandler('^(?i)google .*', google))
    dp.add_handler(RegexHandler(u'.*女朋友.*', girlfriend))
    dp.add_handler(RegexHandler(u'.*妹妹.*', sister))
    dp.add_handler(RegexHandler(u'.*沒錢.*', no_money))
    dp.add_handler(RegexHandler(u'.*不行.*', i_think_no))
    dp.add_handler(RegexHandler(u'.*可以.*', i_think_ok))
    dp.add_handler(RegexHandler(u'.*(?i)python.*', python_better))
    dp.add_handler(RegexHandler(u'.*(?i)js.*', python_better))
    dp.add_handler(RegexHandler(u'.*(?i)javascript.*', python_better))
    dp.add_handler(RegexHandler('^(?i)image .*', images))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
