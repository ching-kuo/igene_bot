# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import logging
import re
import requests
try:
    import urlparse as parse
except ImportError:
    from urllib import parse


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

def google(bot, update):
    search = update.message.text
    search = re.sub(r'^(?i)google ','',search)
    logger.info("Google %s" %search)
    r = requests.get('https://www.google.com/search?q='+ search)
    soup = BeautifulSoup(r.text, "html.parser")
    result = soup.find('h3', {'class': 'r'}).find('a').attrs['href']
    if result.startswith('/'):
        result = parse.parse_qs(parse.urlparse(result).query)['url'][0]
    update.message.reply_text(result)
