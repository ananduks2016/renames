#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) king legend

# the logging things
import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

import os
import sqlite3

# the secret configuration specific things
from sample_config import Config

# the Strings used for this "thing"
from translation import Translation

import pyrogram
from pyrogram import filters
logging.getLogger("pyrogram").setLevel(logging.WARNING)



@pyrogram.Client.on_message(pyrogram.filters.document | filters.video)
async def getchat(bot, update):
    out = await bot.get_messages(chat_id=update.chat.id, message_ids=update.message_id)
    print(out)
    n = out.document.file_size
    lice =' {:,} MB'.format(int(n/1024**2)).replace(',', ' ')
    await bot.send_message(
      text=Translation.USER_TXT.format(out.document.file_name, lice, out.document.mime_type),
      chat_id=update.chat.id
    )
