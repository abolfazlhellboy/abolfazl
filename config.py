## What's up Kangers
## Don't Kang without Creadits else I will rape your mom

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
if str(getenv("SESSION_NAME")).strip() == "BABB2aVm1EL57g_WVeIxUR59uWk76l1p072DYK3WRWcdBY1iaUv7kIhbDwxu4j5FeoI523jHO07lfHxdoQzZiqEnqC8N5p4r0PjLkLCH87xMYmC1YFJy5_X8KYJJaIafAKIFabPX0cCUJvSYN_okXbAWH__nqqjY-xjvwf1bLw_n_gIjNVlngJ9IhMrVfA_JlqNO1V5BAwNIg0rFc4fOq9if65qsj156aITDvESW1MaCcxyjCYQHVAYYwIxuxv6r4l5BpzKx6-6nXRGJ5a0GpQtD4mPNU1ZeHt4gOS5KS4qEs9aUJYzahU9bFvvq3ueGQFhGT2jnnrqvU5Y97QnYSqy_LUO8TgA":
    SESSION_NAME = str(None)
else:
    SESSION_NAME = str(getenv("SESSION_NAME"))

if str(getenv("STRING_SESSION2")).strip() == "":
    SESSION2 = str(None)
else:
    SESSION2 = str(getenv("STRING_SESSION2"))

if str(getenv("STRING_SESSION3")).strip() == "":
    SESSION3 = str(None)
else:
    SESSION3 = str(getenv("STRING_SESSION3"))

if str(getenv("STRING_SESSION4")).strip() == "":
    SESSION4 = str(None)
else:
    SESSION4 = str(getenv("STRING_SESSION4"))

if str(getenv("STRING_SESSION5")).strip() == "":
    SESSION5 = str(None)
else:
    SESSION5 = str(getenv("STRING_SESSION5"))

BOT_TOKEN = getenv("BOT_TOKEN", "5438062764:AAE0phcQy4IpZBi8PxwVXRBhUpYdXWMOCQg")
BOT_NAME = getenv("BOT_NAME", "hellboy")

API_ID = int(getenv("API_ID", "18599862"))
API_HASH = getenv("API_HASH", "db2e91d3112917b60ebc9225590a2751")
MONGO_DB_URL = getenv("MONGO_DB_URL", "mongodb+srv://hellboy1909:hellboy1379@cluster0.29wscea.mongodb.net/test?retryWrites=true&w=majority")
OWNER_NAME = getenv("OWNER_NAME", "hellboy")
OWNER_USERNAME = getenv("OWNER_USERNAME", "Hegklg")
ALIVE_NAME = getenv("ALIVE_NAME", "Zaid")
BOT_USERNAME = getenv("BOT_USERNAME", "hell1379_music_bot")
OWNER_ID = getenv("OWNER_ID", "759413838")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "hellboy1379")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "metingbahala")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "metingbahala")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("UPDATES_CHANNEL", "HEROKU_API_KEY")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "759413838").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/fc9d87ffd1c6f828eb7fc.png")
START_PIC = getenv("START_PIC", "https://telegra.ph/file/a414e2cdfeaa7d4414b89.png")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/ITZ-ZAID/Zaid-Vc-Player")
PLAY_IMG = getenv("PLAY_IMG", "https://telegra.ph/file/10b1f781170b1e1867f68.png")
QUE_IMG = getenv("QUE_IMG", "https://telegra.ph/file/b95c13eef1ebd14dbb458.png")
CMD_IMG = getenv("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
VIDEO_IMG = getenv("VIDEO_IMG", "https://telegra.ph/file/6213d2673486beca02967.png")
SKIP_IMG = getenv("SKIP_IMG", "https://telegra.ph/file/f02efde766160d3ff52d6.png")
NEXT_IMG = getenv("NEXT_IMG", "https://telegra.ph/file/f02efde766160d3ff52d6.png")
