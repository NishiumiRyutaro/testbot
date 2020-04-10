import os
import discord
import random
import tabelog

channel_id = 644386726961217539
client = discord.Client()
token = os.getenv('DISCORD_TOKEN')

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    if  message.content.startswith("ランチ"):
        channel = client.get_channel(channel_id)
        if client.user != message.author:
            say = message.content
            words = say.split("、")
            lunch = tabelog.get_shop_list(words[1], words[2])    
            await channel.send(lunch)
            
client.run(token)
