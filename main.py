import os

import discord

token = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    print(f"{client.user} has connected to Discord")

@client.event
async def on_message(message):
    if message.author.bot:
        return
    if message.content == 'つよばは':
        await message.channel.send('22時からです')

client.run(token)
