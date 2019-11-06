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
    if message.content != None:
        x = message.content
        m = re.search(r'つよばは21時', x, flags=re.DOTALL)
        if m :
            await message.channel.send('21時からつよばは連戦部屋建て&環境役をやります。参加予定の方は30分前までにスプシに自発予定とあわせて書きこんでおいてください。人数によっては部屋を分ける場合もあります。')
    await message.delete()            
    await message.channel.send('削除しました')
        #y = m.group(0) if m else None
        #await message.channel.send(repr(y))
    #if message.content == '/hello':
    #    await message.channel.send('はろー')
    #elif message.content == '/evening':
    #    await message.channel.send('こんばんは')

client.run("token")
