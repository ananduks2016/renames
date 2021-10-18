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



@pyrogram.Client.on_message(pyrogram.filters.command(["cast"]))
async def getchat(bot, update):
    cmd, file_targ = update.text.split(" ", 1)
    await bot.send_chat_action(chat_id=file_targ, action="typing")
    await bot.send_chat_action(chat_id=file_targ, action="typing")
    await bot.send_chat_action(chat_id=file_targ, action="typing")
    await bot.send_chat_action(chat_id=file_targ, action="typing")
    await bot.send_chat_action(chat_id=file_targ, action="typing")
    await bot.send_chat_action(chat_id=file_targ, action="typing")
    out = await bot.forward_messages(chat_id=file_targ, from_chat_id=update.chat.id, message_ids=update.reply_to_message.message_id, as_copy=True)
    print(out) 
    await bot.send_message(
      text="success",
      chat_id=update.chat.id
    )
