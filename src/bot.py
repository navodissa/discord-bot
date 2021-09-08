# -*- coding: utf-8 -*-
# @Author: Your name
# @Date:   2021-09-07 20:40:44
# @Last Modified by:   Your name
# @Last Modified time: 2021-09-08 20:34:01
# bot.py
import os
import random

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    brooklyn_99_quotes = [
        'I\'m the human form of the 💯 emoji.',
        'Bingpot!',
        (
            'Cool. Cool cool cool cool cool cool cool, '
            'no doubt no doubt no doubt no doubt at all.'
        ),
    ]

    if message.content == '99!':
        response = random.choice(brooklyn_99_quotes)
        await message.channel.send(response)
    if message.content == 'ping':
        await message.channel.send('pong')

client.run(TOKEN)
