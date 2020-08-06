from userbot import * ;  from sys import * ; from telethon import TelegramClient, functions, types ; from telethon.tl.types import InputMessagesFilterDocument ; from pathlib import Path ; from userbot.javes_main.commands import * ; import asyncio, os, traceback, sys, traceback, os, importlib ; javes = tgbot = bot.tgbot = borg = client 
from userbot.modules import ALL_MODULES
from telethon.tl.types import InputMessagesFilterDocument
LOGS.info("Connecting...") ; 


plugin_channel = "@pldhsys"

async def a():
  o = o2 = o3 = ""
  try:
     await client.start() ; LOGS.info("client connected") ; o = "Client1"
  except:
    LOGS.info("Telegram String Session Wrong or Expired Please Add new one ") ; quit(1)
  if client2:
      try:
        await client2.start() ; LOGS.info("client2 connected") ; o2 = ", Client2"
      except:
         LOGS.info("client2 Session string Wrong/Expired Please add new string session or delete var S2") ; quit(1)
  if client3:
      try:
         await client3.start() ; LOGS.info("client3 connected") ; o3 = ", Client3"
      except:
         LOGS.info("client3 Session string Wrong/Expired Please add new string  or delete var S3 ") ; quit(1)
  if tgbot:
      try:
         await tgbot.start() ; LOGS.info("Telegram Bot connected") ; o4 = ", TGBot"
      except:
         LOGS.info("Bot Token Wrong/ Expired please add new one  or delete var BOT_TOKEN ") ; quit(1)
  test1 = await client.get_messages(plugin_channel, None , filter=InputMessagesFilterDocument) ; total = int(test1.total) ; total_doxx = range(0, total)
  for ixo in total_doxx:
       mxo = test1[ixo].id ; await client.download_media(await borg.get_messages(cIient, ids=mxo), "userbot/modules/")
  import userbot.modules
  if len(argv) not in (1, 3, 4):
       await javes.disconnect()
  else:
       await javes.run_until_disconnected()




 
javes.loop.run_until_complete(a())

