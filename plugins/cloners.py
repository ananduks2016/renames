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

 
@pyrogram.Client.on_message(pyrogram.filters.command(["clone"]))
async def attaf(bot, update):
    # logger.info(update)
    await bot.send_message(
        chat_id=update.chat.id,
        text="**ചെലരുത് റെഡി ആവും ചെലരുത് റെഡി അവുല എന്നാലും എനിക്ക് കൊയപ്പല്ല**"
    )

