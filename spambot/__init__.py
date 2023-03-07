import logging
import os
import sys
from inspect import getfullargspec
from os import getenv
from decouple import config
import time
from datetime import datetime
from telethon import TelegramClient
from telethon.sessions import StringSession

import configparser

StartTime = time.time()

# logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

config = configparser.ConfigParser()
config.read('config.ini')

api_id = config.get('default','api_id')
api_hash = config.get('default','api_hash')
BOT_TOKEN = config.get('default','BOT_TOKEN')
OWNER_ID = config.get('default','OWNER_ID') 
OWNER_NAME = config.get('default','OWNER_NAME') 
BOT_ID = config.get('default','BOT_ID') 
DEV_USERS = config.get('default','DEV_USERS') 
SUDO_USERS = config.get('default','SUDO_USERS') 

SUDO_USERS = SUDO_USERS.split(',')
# SUDO_USERS = list(SUDO_USERS)
SUDO_USERS = list(map(int, SUDO_USERS))

# list(map(int, "42 0".split()))

# DEV_USERS = SUDO_USERS.split(',')
# DEV_USERS = list(DEV_USERS)

print("SUDO USERS: ", SUDO_USERS)
print("DEV: ", DEV_USERS)

# API_ID = config("API_ID", default=None, cast=int)
# API_HASH = config("API_HASH", default=None)
# OWNER_ID = config("OWNER_ID", cast=int)
# BOT_ID = config("BOT_ID", cast=int)
# OWNER_NAME = config("OWNER_NAME")
# HEROKU_API_KEY = config("HEROKU_API_KEY", default=None)
# HEROKU_APP_NAME  = config("HEROKU_APP_NAME", default=None)
# Bot_Token = config("Bot_Token", default=None)
# SUDO_USERS = list(map(int, config("SUDO_USERS").split()))
# DEV_USERS = list(map(int, config("DEV_USERS").split()))

# SUDO_USERS.append(OWNER_ID)
# DEV_USERS.append(OWNER_ID)
# SUDO_USERS = list(SUDO_USERS)
# DEV_USERS = list(DEV_USERS)


print("[INFO]: STARTING TELETHON BOT")
gladiator = TelegramClient('Bot', api_id, api_hash).start(bot_token=BOT_TOKEN)
# gladiator = TelegramClient('sessions/session_master', api_id, api_hash).start(bot_token=BOT_TOKEN)
# gladiator = TelegramClient('sessions/session_master', api_id, api_hash).start(bot_token=BOT_TOKEN)
