
from sys import * ; from telethon import TelegramClient, functions, types ; from telethon.tl.types import InputMessagesFilterDocument ; from pathlib import Path; import asyncio, os, traceback, sys, traceback, os, importlib, glob
from telethon.tl.types import InputMessagesFilterDocument
from importlib import import_module
from sys import version_info
from logging import basicConfig, getLogger, INFO, DEBUG, WARNING
from distutils.util import strtobool as sb
from pylast import LastFMNetwork, md5
from pySmartDL import SmartDL
from dotenv import load_dotenv
from requests import get
from telethon import TelegramClient
from telethon.sessions import StringSession
from var import Var
load_dotenv("config.env")
from userbot.javes_main.heroku_var import config

CONSOLE_LOGGER_VERBOSE = config.CONSOLE_LOGGER_VERBOSE
basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=INFO)
LOGS = getLogger(__name__)
ENV = config.ENV
API_KEY = config.API_KEY
API_HASH = config.API_HASH
STRING_SESSION = config.STRING_SESSION
BOTLOG_CHATID = config.BOTLOG_CHATID
BOTLOG = config.BOTLOG
LOGSPAMMER = config.LOGSPAMMER
GENIUS = config.GENIUS
GENIUS_API_TOKEN = config.GENIUS_API_TOKEN
PM_AUTO_BAN = config.PM_AUTO_BAN
HEROKU_APPNAME = config.HEROKU_APPNAME
HEROKU_APP_NAME = config.HEROKU_APP_NAME
HEROKU_APIKEY = config.HEROKU_APIKEY
HEROKU_API_KEY = config.HEROKU_API_KEY
UPSTREAM_REPO_URL = config.UPSTREAM_REPO_URL
TELEGRAPH_SHORT_NAME = config.TELEGRAPH_SHORT_NAME
CONSOLE_LOGGER_VERBOSE = config.CONSOLE_LOGGER_VERBOSE
DB_URI = config.DB_URI
OCR_SPACE_API_KEY = config.OCR_SPACE_API_KEY
REM_BG_API_KEY = config.REM_BG_API_KEY
CHROME_DRIVER = config.CHROME_DRIVER
GOOGLE_CHROME_BIN = config.GOOGLE_CHROME_BIN
OPEN_WEATHER_MAP_APPID = config.OPEN_WEATHER_MAP_APPID
WEATHER_DEFCITY = config.WEATHER_DEFCITY
LYDIA_API_KEY = config.LYDIA_API_KEY
PM_MESSAGE = config.PM_MESSAGE
JAVES_NAME = config.JAVES_NAME
ANTI_SPAMBOT = config.ANTI_SPAMBOT
ANTI_SPAMBOT_SHOUT = config.ANTI_SPAMBOT_SHOUT
YOUTUBE_API_KEY = config.YOUTUBE_API_KEY
ALIVE_NAME = config.ALIVE_NAME
BLOCK_MESSAGE = config.BLOCK_MESSAGE
AFK_MESSAGE = config.AFK_MESSAGE
ALIVE_S_MESSAGE = config.ALIVE_S_MESSAGE
BIO_MESSAGE = config.BIO_MESSAGE
ALIVE_E_MESSAGE = config.ALIVE_E_MESSAGE
COUNTRY = config.COUNTRY
TZ_NUMBER = config.TZ_NUMBER
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
CLEAN_WELCOME = config.CLEAN_WELCOME
BIO_PREFIX = config.BIO_PREFIX
DEFAULT_BIO = config.DEFAULT_BIO
LASTFM_API = config.LASTFM_API
LASTFM_SECRET = config.LASTFM_SECRET
LASTFM_USERNAME = config.LASTFM_USERNAME
LASTFM_PASSWORD_PLAIN = config.LASTFM_PASSWORD_PLAIN
LASTFM_PASS = config.LASTFM_PASS
G_DRIVE_CLIENT_ID = config.G_DRIVE_CLIENT_ID
G_DRIVE_CLIENT_SECRET = config.G_DRIVE_CLIENT_SECRET
G_DRIVE_AUTH_TOKEN_DATA = config.G_DRIVE_AUTH_TOKEN_DATA
GDRIVE_FOLDER_ID = config.GDRIVE_FOLDER_ID
TEMP_DOWNLOAD_DIRECTORY = config.TEMP_DOWNLOAD_DIRECTORY



if LASTFM_API and LASTFM_SECRET and LASTFM_USERNAME and LASTFM_PASS:
    lastfm = LastFMNetwork(api_key=LASTFM_API,api_secret=LASTFM_SECRET,username=LASTFM_USERNAME,password_hash=LASTFM_PASS)
else:
    lastfm = None
    
from userbot import ALIVE_NAME
from userbot import DEFAULTUSER
JAVES_MSG = (f"Javes ")
ORI_MSG = (f"Hello Sir, I can't allow you to {ALIVE_NAME}'s PM without his permissions please be patient, Thankyou ")
BLOCK_MSG = (f"I am not going to allow you to spam {DEFAULTUSER}'s PM, You have been blocked ")
JAVES_NNAME = str(JAVES_NAME) if JAVES_NAME else str(JAVES_MSG)
AFK_MSG = (f"Hello Sir, {DEFAULTUSER} is offline Just leave Your message, Thankyou!")
BIO_MSG = (f"")
ALIVE_S_MSG = (f"Iam Alive!")
ALIVE_E_MSG = (f"Databases functioning normally!! ")

if not os.path.exists('bin'):
    os.mkdir('bin')

binaries = {"https://raw.githubusercontent.com/yshalsager/megadown/master/megadown":"bin/megadown","https://raw.githubusercontent.com/yshalsager/cmrudl.py/master/cmrudl.py":"bin/cmrudl"}

for binary, path in binaries.items():
    downloader = SmartDL(binary, path, progress_bar=False)
    downloader.start()
    os.chmod(path, 0o755)

S2 = os.environ.get("S2", None)
S3 = os.environ.get("S3", None)
BOT_TOKEN = os.environ.get("BOT_TOKEN", None)

client2 = client3 = tebot = None
if STRING_SESSION:
    client = TelegramClient(StringSession(STRING_SESSION),API_KEY,API_HASH,connection_retries=None,auto_reconnect=False,lang_code='en')
else:
     quit(1)
if S2:
    client2 = TelegramClient(StringSession(S2),API_KEY,API_HASH,connection_retries=None,auto_reconnect=False,lang_code='en')
if S3:
    client3 = TelegramClient(StringSession(S3),API_KEY,API_HASH,connection_retries=None,auto_reconnect=False,lang_code='en')
if BOT_TOKEN:    
    tebot = TelegramClient("bot", API_KEY, API_HASH).start(bot_token=BOT_TOKEN)



owner = owner2 = owner3 = owner4 = None
borg = bot = javes = client



#####################################
plugin_channel = "@pldhsys"  #this is official plugin channel for javes 
#####################################


async def a():
  LOGS.info("Connecting...") ; 
  o = o2 = o3 = o4 = ""
  la = 0
  try:
     await client.start() ; LOGS.info("client connected") ; o = "Client1" ; owner = await client.get_me()
  except:
    LOGS.info("Telegram String Session Wrong or Expired Please Add new one ") ; quit(1)
  if client2:
      try:
        await client2.start() ; LOGS.info("client2 connected") ; o2 = ", Client2" ; owner2 = await client2.get_me()
      except:
         LOGS.info("client2 Session string Wrong/Expired Please add new string session or delete var S2") ; quit(1)
  if client3:
      try:
         await client3.start() ; LOGS.info("client3 connected") ; o3 = ", Client3" ; owner3 = await client3.get_me()
      except:
         LOGS.info("client3 Session string Wrong/Expired Please add new string  or delete var S3 ") ; quit(1)
  if tebot:
      try:
         await tebot.start() ; LOGS.info("Telegram Bot connected") ; o4 = ", TGBot" ; owner4 = await tebot.get_me()
      except:
         LOGS.info("Bot Token Wrong/ Expired please add new one  or delete var BOT_TOKEN ") ; quit(1)
  test1 = await client.get_messages(plugin_channel, None , filter=InputMessagesFilterDocument) ; total = int(test1.total) ; total_doxx = range(0, total)
  for ixo in total_doxx:
       mxo = test1[ixo].id ; await client.download_media(await client.get_messages(cIient, ids=mxo), "userbot/modules/")
  ar = glob.glob("userbot/modules/*.py")
  f = len(ar)
  LOGS.info(f" loading {f} modules it may take 1 minute please wait")
  for i in ar:
     br = os.path.basename(i)
     cr = (os.path.splitext(br)[0])
     import_module(f"userbot.modules.{cr}")
     la += 1
     LOGS.info(f" loaded {la}/{f} modules")  
  os.system("rm userbot/modules/*.py") ; LOGS.info(f"Sucessfully connected with {o}{o2}{o3}{o4} check it by typing !javes in any client's chat, type  !help for more info.")
  if len(argv) not in (1, 3, 4):
       await javes.disconnect()
  else:
       await javes.run_until_disconnected()
       





COUNT_MSG = 0
USERS = {}
COUNT_PM = {}
LASTMSG = {}
CMD_HELP = {}
CMD_LIST = {}
LOAD_PLUG = {}
ISAFK = None
AFKREASON = None
INT_PLUG = ""


