from configparser import ConfigParser
from googletrans import Translator
import pyowm
import logging
import re

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)
cfg = ConfigParser()
cfg.read('config')
api_key = cfg.get('auth', 'owm_api_key')

def weather(bot, update):
    owm = pyowm.OWM(api_key, language='zh_tw')
    translator = Translator()
    location = update.message.text
    location = re.sub(u'天氣 ','',location)
    trans = translator.translate(location).text
    logger.info("get weather at %s" %trans)
    try:
        obs = owm.weather_at_place(trans)
        w = obs.get_weather()
        update.message.reply_text(location+'的天氣\n'+'溫度：'+str(w.get_temperature(unit='celsius')['temp'])+
                '   濕度：'+str(w.get_humidity())+'   天氣狀況：'+str(w.get_status()))
    except:
        update.message.reply_text('Location fucking not found')
