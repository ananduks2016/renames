#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Shrimadhav U K

# the logging things
import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

import os
import sqlite3


from sample_config import Config

# the Strings used for this "thing"
from translation import Translation

import pyrogram
logging.getLogger("pyrogram").setLevel(logging.WARNING)

from helper_funcs.display_progress import userids

def GetExpiryDate(chat_id):
    expires_at = (str(chat_id))
    return expires_at
    
@pyrogram.Client.on_message(pyrogram.filters.command(["help", "about"]))
async def help_user(bot, update):
    # logger.info(update)
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.NO_COD
    )

@pyrogram.Client.on_message(pyrogram.filters.command(["showthumb"]))
async def view_thumbnail(bot, update):
    photopath = Config.DOWNLOAD_LOCATION + "/" + str(update.from_user.id) + ".jpg"
    if os.path.exists(photopath):
       await bot.send_photo(
           chat_id=update.chat.id,
           caption = "default thumbnail",
           photo= Config.DOWNLOAD_LOCATION + "/" + str(update.from_user.id) + ".jpg",
           parse_mode="html",
           ttl_seconds=10
       )
    else:
    	await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.NO_CUSTOM_THUMB_NAIL_FOUND,
    )
@pyrogram.Client.on_message(pyrogram.filters.command(["version"]))
async def start(bot, update):
    # logger.info(update)
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.VER_TX,
    )      
      
@pyrogram.Client.on_message(pyrogram.filters.command(["cancel"]))
async def cancel(bot, update):
    # logger.info(update)
    await bot.send_message(
        chat_id=update.chat.id,
        text="**Canceling**",
    )
    userids.append(update.chat.id)
