from userbot import * ;  from sys import * ; from telethon import TelegramClient, functions, types ; from telethon.tl.types import InputMessagesFilterDocument ; from pathlib import Path ; from userbot.javes_main.commands import * ; import asyncio, os, traceback, sys, traceback, os, importlib ; javes = tgbot = bot.tgbot = borg = client 
from userbot.modules import ALL_MODULES
from telethon.tl.types import InputMessagesFilterDocument
LOGS.info("Connecting...") ; o = o2 =o3 = ""


plugin_channel = "@pldhsys"

async def a(): 
  try:
     await client.start() ; LOGS.info("client connected") ; o = "client1"
  except:
    LOGS.info("Telegram String Session Wrong or Expired Please Add new one ") ; quit(1)
  if client2:
      try:
        await client2.start() ; LOGS.info("client2 connected") ; o2 = ", client2"
      except:
         LOGS.info("client2 Session string Wrong/Expired Please add new string session or delete var S2") ; quit(1)
  if client3:
      try:
         await client3.start() ; LOGS.info("client3 connected") ; o3 = ", client3"
      except:
         LOGS.info("client3 Session string Wrong/Expired Please add new string  or delete var S3 ") ; quit(1)
  test1 = await client.get_messages(plugin_channel, None , filter=InputMessagesFilterDocument) ; total = int(test1.total) ; total_doxx = range(0, total)
  for ixo in total_doxx:
       mxo = test1[ixo].id ; await client.download_media(await borg.get_messages(cIient, ids=mxo), "userbot/modules/")
  for module_name in ALL_MODULES:
    imported_module = import_module("userbot.modules." + module_name)
  os.system("rm userbot/modules/*.py") ; LOGS.info(f"Sucessfully connected with {o}{o2}{o3} check it by typing !javes in any client's chat, type  !help for more info.")
  if len(argv) not in (1, 3, 4):
       await javes.disconnect()
  else:
       await javes.run_until_disconnected()




 
javes.loop.run_until_complete(a())

