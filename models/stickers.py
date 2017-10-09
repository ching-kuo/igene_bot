# -*- coding: utf-8 -*-
import logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

def no_money(bot, update):
    logger.info("no money called")
    update.message.reply_sticker(sticker='CAADBQADTgADVRXrCVFQ913jCk08Ag')

def i_think_no(bot, update):
    logger.info("nooooooo")
    update.message.reply_sticker(sticker='CAADBQADUAADVRXrCVXDWs7XUQUfAg')

def i_think_ok(bot, update):
    logger.info("okkkkkk")
    update.message.reply_sticker(sticker='CAADBQADTwADVRXrCc2qZPCSdFYqAg')
