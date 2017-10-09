# -*- coding: utf-8 -*-
import logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

def girlfriend(bot, update):
    logger.info("girlfriend called")
    update.message.reply_text(u"醒醒吧你沒有女友")

def sister(bot, update):
    logger.info("sister called")
    update.message.reply_text(u"醒醒吧你沒有妹妹")
