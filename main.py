import os

import discord
import re

token = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    print(f"{client.user} has connected to Discord")

@client.event
async def on_message(message):
    if message.author.bot:
        return
    if message.content == '/hello':
        await message.channel.send('はろー')
    elif message.content == '/evening':
        await message.channel.send('こんばんは')

client.run("token")
