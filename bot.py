# -*- coding: utf-8 -*-
import logging
from configparser import ConfigParser
from telegram.ext import (Updater, CommandHandler, RegexHandler)
from models import *

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', \
        level=logging.INFO)
logger = logging.getLogger(__name__)
cfg = ConfigParser()

def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="I'm a bot, please talk to me!")

"""
All handlers added in main
"""


def main():
    cfg.read('/etc/igene_bot/config')
    token = cfg.get('auth', 'token')
    updater = Updater(token)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(RegexHandler(u'(?i)google (?i)image .*', g_image))
    dp.add_handler(RegexHandler('^(?i)google .*', google))
    dp.add_handler(RegexHandler('^(?i)speak .*', tts))
    dp.add_handler(RegexHandler(u'.*女朋友.*', girlfriend))
    dp.add_handler(RegexHandler(u'.*妹妹.*', sister))
    dp.add_handler(RegexHandler(u'.*沒錢.*', no_money))
    dp.add_handler(RegexHandler(u'.*我覺得.*不行.*', i_think_no))
    dp.add_handler(RegexHandler(u'天氣 .*', weather))
    dp.add_handler(RegexHandler(u'.*我覺得.*可以.*', i_think_ok))
    dp.add_handler(RegexHandler(u'.*是我啦.*', wuyiulin))
    dp.add_handler(RegexHandler('^(?i)image .*', images))
    dp.add_handler(RegexHandler('.*', correct))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
