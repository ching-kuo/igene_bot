# -*- coding: utf-8 -*-
"""Handle all task triggered by strings"""
import logging
import random
import os


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', \
        level=logging.INFO)
logger = logging.getLogger(__name__)



def girlfriend(bot, update):
    """Triggered when girlfriend was sent"""
    logger.info("girlfriend called")
    pic = random.choice(os.listdir('photo'))
    photo = open('photo/'+pic, 'rb')
    update.message.reply_text("這是我女友 沒看過的話讓你看看")
    update.message.reply_photo(photo)


def sister(bot, update):
    """Triggered when sister was sent"""
    logger.info("sister called")
    update.message.reply_text(u"醒醒吧你沒有妹妹")


def wuyiulin(bot, update):
    """Triggered when wuyiulin is tagged"""
    logger.info("wuyiulin is tagged")
    update.message.reply_text("時薪133的元智亞泥魚池龍破壞包莖劍士肥宅管理員")
