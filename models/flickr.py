from configparser import ConfigParser
import logging
import re
import requests
import flickrapi
import json
import random

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

def images(bot, update):
    cfg = ConfigParser()
    cfg.read('config')
    api_key = cfg.get('auth', 'flickr_api_key')
    secret = cfg.get('auth', 'flickr_secret')
    search = update.message.text
    search = re.sub(r'%(?i)image ','',search)
    logger.info("Flickr image search %s" %search)
    flickr = flickrapi.FlickrAPI(api_key, secret)
    photos = json.loads(flickr.photos.search(text=search, per_page="50", page="1", format="json").decode('utf8'))
    selected_image_num = random.randint(0, len(photos['photos']['photo']))

    if not photos['photos']['photo']:
        update.message.reply_text('Flickr找不到啦，幹！')
    else:
        photo = photos['photos']['photo'][selected_image_num]
        image = 'https://farm{}.staticflickr.com/{}/{}_{}.jpg'.format(photo['farm'], photo['server'], photo['id'], photo['secret'])
        update.message.reply_photo(image)
