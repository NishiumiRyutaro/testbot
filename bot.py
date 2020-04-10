import discord
import random
import tabelog

channel_id = 644386726961217539
client = discord.Client()

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
            

client.run("NjI5Njk3ODExODA5ODI4ODk0.Xct9Zw.8ZhaXrNi2vPD2VK7QP8p7dwL3sU")
