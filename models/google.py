# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import logging
import re
import requests
import urllib.parse

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

def google(bot, update):
    search = update.message.text
    search = re.sub(r'^(?i)google ','',search)
    logger.info("Google %s" %search)
    headers = {'User-Agent': 'Mozilla/5.0'}
    r = requests.get('https://www.google.com/search?q='+ search, headers)
    soup = BeautifulSoup(r.text, "html.parser")
    result = soup.find('h3', {'class': 'r'}).find('a').attrs['href']
    result = urllib.parse.unquote(result)
    if_http_start_regex = re.compile('^http')
    if_http_start = if_http_start_regex.match(str(result))
    if if_http_start == None:
        remove_url_q_re = re.compile('^\/url\?q=')
        remove_url_sa_re = re.compile('\&sa.+')
        result = re.sub(remove_url_q_re, '', result)
        result = re.sub(remove_url_sa_re, '', result)
        update.message.reply_text(result)
    else:
        update.message.reply_text(result)

def images(bot, update):
    search = update.message.text
    search = re.sub(r'%(?i)image ','',search)
    logger.info("Google image search %s" %search)
    headers = {'User-Agent': 'Mozilla/5.0'}
    r = requests.get('https://www.google.com/search?tbm=isch&q='+ search, headers)
    soup = BeautifulSoup(r.text, "html.parser")
    images = [a['src'] for a in soup.find_all("img", {"src": re.compile("gstatic.com")})]
    update.message.reply_text(images)
