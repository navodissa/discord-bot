# -*- coding: utf-8 -*-
# @Author: Your name
# @Date:   2021-09-07 21:46:55
# @Last Modified by:   Your name
# @Last Modified time: 2021-09-07 23:15:57
from discord.ext import commands
from dotenv import load_dotenv
import discord
import os
import pytest

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
bot = commands.Bot(command_prefix='?/')
target_id = "navoda-test"
channel_id = "general"

# @bot.command(name="ping") #if name did not entered, function name will be the command name
# async def test_ping(ctx): #Every command takes context object as first parameter
#     correct_response = 'Pong!'
#     print(correct_response)
#     # channel = await bot.fetch_channel(channel_id)
#     # print(channel)
#     await ctx.target_id.send("ping")

#     def check(m):
#         return m.content == correct_response and m.author.id == target_id

#     response = await bot.wait_for('message', check=check)
#     print(response)
#     assert (response.content == correct_response)

@bot.command(name="ping")
async def DM(ctx, user: discord.User, *, message=None):
    message = message or "This Message is sent via DM"
    await user.send(message)

bot.run(TOKEN)
