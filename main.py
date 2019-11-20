import os

import discord
from datetime import datetime
from discord.ext import tasks
import re
import asyncio
from foo import ProtCommndList
from foo import AruCommndList
from foo import RushiCommndList

token = os.getenv('DISCORD_TOKEN')
channel_id = 644583189331050537
# 接続に必要なオブジェクトを生成
client = discord.Client()


#投稿する日時
readydateTimeList = [
 '06:55:00'
 ]

# 起動時に動作する処理
@client.event
async def on_ready():
    print('ready')


async def readySendMessage():
    channel = client.get_channel(channel_id)
    await channel.send('SPバトルだよ')
    await asyncio.sleep(35)
# 30秒に一回ループ
@tasks.loop(seconds=0)
async def time_check():
    # 現在の時刻
    now = datetime.now().strftime('%H:%M:%S')

    if now in readydateTimeList:
        await readySendMessage()  
    
# メッセージ受信時に動作する処理
@client.event
async def on_message(message):
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return
    # 使用できるコマンド一覧
    if message.content == '!nowtime':
        now = datetime.now().strftime('%H:%M:%S')
        await message.channel.send(now)
    if message.content == '!nowtime':
        await message.channel.send('SPバトルだよ')
    if message.content != None:
        x = message.content
        if x.find('!') == 0:
            await message.delete()
        m = re.search(r'!つよばは20時30分', x, flags=re.DOTALL)
        l = re.search(r'!つよばは21時', x, flags=re.DOTALL)
        o = re.search(r'!つよばは21時30分', x, flags=re.DOTALL)
        p = re.search(r'!つよばは22時', x, flags=re.DOTALL)
        q = re.search(r'!つよばは22時30分', x, flags=re.DOTALL)
        arubaha = re.search(r'!あるばは21時', x, flags=re.DOTALL)
        if m :
            await message.channel.send(ProtCommndList[0])
        if l :
            await message.channel.send(ProtCommndList[1])
        if o :
            await message.channel.send(ProtCommndList[2])
        if p :
            await message.channel.send(ProtCommndList[3])
        if q :
            await message.channel.send(ProtCommndList[4])        
        if arubaha :
            await message.channel.send(AruCommndList[0])
#ループ処理
time_check.start()
# Botの起動とDiscordサーバーへの接続
client.run(token)
