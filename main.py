import os

import discord
from datetime import datetime
from discord.ext import tasks
import re

token = os.getenv('DISCORD_TOKEN')
channel_id = 629674683695890449
# 接続に必要なオブジェクトを生成
client = discord.Client()


#投稿する日時
DefensedateTimeList = [
'09:50',
'09:51',
'09:52',
'09:53',
'09:54',
'09:55',
'15:06'
]
FOdateTimeList = [
'15:08',
'07:00'
]
ProtCommndList = [
    "20時30分からつよばは連戦部屋建て&環境役をやります。参加予定の方は30分前までにスプシに自発予定とあわせて書きこんでおいてください。人数によっては部屋を分ける場合もあります。",
    "21時からつよばは連戦部屋建て&環境役をやります。参加予定の方は30分前までにスプシに自発予定とあわせて書きこんでおいてください。人数によっては部屋を分ける場合もあります。",
    "21時30分からつよばは連戦部屋建て&環境役をやります。参加予定の方は30分前までにスプシに自発予定とあわせて書きこんでおいてください。人数によっては部屋を分ける場合もあります。",
    "22時からつよばは連戦部屋建て&環境役をやります。参加予定の方は30分前までにスプシに自発予定とあわせて書きこんでおいてください。人数によっては部屋を分ける場合もあります。"
    "22時30分からつよばは連戦部屋建て&環境役をやります。参加予定の方は30分前までにスプシに自発予定とあわせて書きこんでおいてください。人数によっては部屋を分ける場合もあります。"
]
# 起動時に動作する処理
@client.event
async def on_ready():
    print('ready')
    
async def DSendMessage():
    channel = client.get_channel(channel_id)
    await channel.send('攻撃アビの時間だよ')
    await channel.send('防衛アビの時間だよ')
    await asyncio.sleep(35)
async def FOSendMessage():
    channel = client.get_channel(channel_id)
    await channel.send('副団アビの時間だよ')
    await asyncio.sleep(35)
# 30秒に一回ループ
@tasks.loop(seconds=0)
async def time_check():
    sleepTime = 0
    # 現在の時刻
    now = datetime.now().strftime('%H:%M')
    if now in DefensedateTimeList:
        await DSendMessage()
    if now in FOdateTimeList:
        await FOSendMessage()    
# メッセージ受信時に動作する処理
@client.event
async def on_message(message):
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return
    # 使用できるコマンド一覧
    if message.content == '!nowtime':
        now = datetime.now().strftime('%H:%M')
        await message.channel.send(now)
    if message.content != None:
        x = message.content
        m = re.search(r'!つよばは21時', x, flags=re.DOTALL)
        l = re.search(r'!つよばは22時', x, flags=re.DOTALL)
        o = re.search(r'!つよばは21時', x, flags=re.DOTALL)
        p = re.search(r'!つよばは22時', x, flags=re.DOTALL)
        q = re.search(r'!つよばは21時', x, flags=re.DOTALL)
        if m :
            await message.channel.send(CommndList[0])
        if l :
            await message.channel.send(CommndList[1])
        if o :
            await message.channel.send(CommndList[2])
        if p :
            await message.channel.send(CommndList[3])
        if q :
            await message.channel.send(CommndList[4])
#ループ処理
time_check.start()
# Botの起動とDiscordサーバーへの接続
client.run(token)
