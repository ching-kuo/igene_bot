# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
from configparser import ConfigParser
from urllib.request import urlopen, Request
from urllib.parse   import quote
import logging
import re
import requests
import urllib.parse
import flickrapi
import json

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

def google(bot, update):
    search = update.message.text
    search = re.sub(r'^(?i)google ','',search)
    logger.info("Google search" + search)
    header = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36'}
    url = 'https://www.google.com/search?q=' + quote(search)
    soup = BeautifulSoup(urlopen(Request(url, headers=header)), "html.parser")
    result = soup.find('h3', {'class': 'r'}).find('a').attrs['href']
    result = urllib.parse.unquote(result)
    if_http_start_regex = re.compile('^http')
    if_http_start = if_http_start_regex.match(str(result))
    if if_http_start is None:
        remove_url_q_re = re.compile('^\/url\?q=')
        remove_url_sa_re = re.compile('\&sa.+')
        result = re.sub(remove_url_q_re, '', result)
        result = re.sub(remove_url_sa_re, '', result)
        update.message.reply_text(result)
    else:
        update.message.reply_text(result)

def correct(bot, update):
    search = update.message.text
    user = update.message.from_user.username
    logger.info("Auto correct")
    headers = {'User-Agent': 'Mozilla/5.0'}
    r = requests.get('https://www.google.com/search?q='+ search, headers)
    soup = BeautifulSoup(r.text, "html.parser")
    result = soup.find('a',{'class': 'spell'})
    if not result is None:
        update.message.reply_text(user+' 的意思也許是\n'+result.text)

def g_image(bot, update):
    search = update.message.text
    search = re.sub(r'^(?i)google (?i)image ','',search)
    logger.info('Google image search ' + search)
    header = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36'}
    url = 'https://www.google.com.tw/search?q='+ quote(search) +'&source=lnms&tbm=isch'
    soup = BeautifulSoup(urlopen(Request(url, headers=header)),'html.parser')
    data = soup.find('div',{'class':'rg_meta'})
    link , Type =json.loads(data.text)["ou"]  ,json.loads(data.text)["ity"]
    logger.info('sent image '+link)
    update.message.reply_photo(link)
