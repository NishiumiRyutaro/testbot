import os

import discord
from datetime import datetime
from discord.ext import tasks
import re
import asyncio
from foo import ProtCommndList
from foo import AruCommndList
from foo import RushiCommndList
from foo import allcmdlist
from foo import MarisuCommndList

token = os.getenv('DISCORD_TOKEN')
channel_id = 644583189331050537
# 接続に必要なオブジェクトを生成
client = discord.Client()

# 起動時に動作する処理
@client.event
async def on_ready():
    print('ready')
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
    if message.author.bot:
        return
    # 使用できるコマンド一覧
    if message.content == '!specification':
        await message.channel.send('normal')
    if message.content == '!nowtime':
        now = datetime.now().strftime('%H:%M:%S')
        await message.channel.send(now)
    if message.content == 'list':
        testcmd = ",".join(allcmdlist)                              # コマンドリスト関連
        testcmd_new = testcmd.replace(',', '\n')                    #
        allcmdlist_new =  testcmd_new.split(",")                    #
        await message.channel.send(testcmd_new.replace('"', '\n'))  #
    if message.content != None:
        x = message.content
        a = re.search(r',.*', x, flags=re.DOTALL)
        #b = re.search(r'@.*', x, flags=re.DOTALL)
        if re.findall('^!', x, flags=re.IGNORECASE):
            tm = re.search(r'つよばは2030', x, flags=re.DOTALL)
            tl = re.search(r'つよばは2100', x, flags=re.DOTALL)
            tn = re.search(r'つよばは2130', x, flags=re.DOTALL)
            to = re.search(r'つよばは2200', x, flags=re.DOTALL)
            tp = re.search(r'つよばは2230', x, flags=re.DOTALL)
            mm = re.search(r'まりす2030', x, flags=re.DOTALL)
            ml = re.search(r'まりす2100', x, flags=re.DOTALL)
            mn = re.search(r'まりす2130', x, flags=re.DOTALL)
            mo = re.search(r'まりす2200', x, flags=re.DOTALL)
            mp = re.search(r'まりす2230', x, flags=re.DOTALL)
            am = re.search(r'!あるばは2030', x, flags=re.DOTALL)
            al = re.search(r'!あるばは2100', x, flags=re.DOTALL)
            an = re.search(r'!あるばは2130', x, flags=re.DOTALL)
            ao = re.search(r'!あるばは2200', x, flags=re.DOTALL)
            ap = re.search(r'!あるばは2230', x, flags=re.DOTALL)
            rm = re.search(r'るし2100', x, flags=re.DOTALL)
            rl = re.search(r'るし2130', x, flags=re.DOTALL)
            rn = re.search(r'るし2200', x, flags=re.DOTALL)
            ro = re.search(r'るし2230', x, flags=re.DOTALL)
            rp = re.search(r'るし2300', x, flags=re.DOTALL)            
        if a != None :            
            a = a.group(0).replace(',', '')             
            if tm:
                await message.channel.send(a+'日'+ProtCommndList[0])
            if tl:
                await message.channel.send(a+'日'+ProtCommndList[1])
            if tn:
                await message.channel.send(a+'日'+ProtCommndList[2])
            if to:
                await message.channel.send(a+'日'+ProtCommndList[3])
            if tp:
                await message.channel.send(a+'日'+ProtCommndList[4])
            if mm:
                await message.channel.send(a+'日'+MarisuCommndList[0])
            if ml:
                await message.channel.send(a+'日'+MarisuCommndList[1])
            if mn:
                await message.channel.send(a+'日'+MarisuCommndList[2])
            if mo:
                await message.channel.send(a+'日'+MarisuCommndList[3])
            if mp:
                await message.channel.send(a+'日'+MarisuCommndList[4])
            if am:
                await message.channel.send(a+'日'+AruCommndList[0])
            if al:
                await message.channel.send(a+'日'+AruCommndList[1])
            if an:
                await message.channel.send(a+'日'+AruCommndList[2])
            if ao:
                await message.channel.send(a+'日'+AruCommndList[3])
            if ap:
                await message.channel.send(a+'日'+AruCommndList[4])
            if rm: 
                await message.channel.send(a+'日'+RushiCommndList[0])
            if rl: 
                await message.channel.send(a+'日'+RushiCommndList[1])
            if rn: 
                await message.channel.send(a+'日'+RushiCommndList[2])
            if ro: 
                await message.channel.send(a+'日'+RushiCommndList[3])
            if rp: 
                await message.channel.send(a+'日'+RushiCommndList[4])
        elif a == None:
            if tm:
                await message.channel.send(ProtCommndList[0])
            if tl:
                await message.channel.send(ProtCommndList[1])
            if tn:
                await message.channel.send(ProtCommndList[2])
            if to:
                await message.channel.send(ProtCommndList[3])
            if tp:
                await message.channel.send(ProtCommndList[4])
            if mm:
                await message.channel.send(MarisuCommndList[0])
            if ml:
                await message.channel.send(MarisuCommndList[1])
            if mn:
                await message.channel.send(MarisuCommndList[2])
            if mo:
                await message.channel.send(MarisuCommndList[3])
            if mp:
                await message.channel.send(MarisuCommndList[4])
            if am:
                await message.channel.send(AruCommndList[0])
            if al:
                await message.channel.send(AruCommndList[1])
            if an:
                await message.channel.send(AruCommndList[2])
            if ao:
                await message.channel.send(AruCommndList[3])
            if ap:
                await message.channel.send(AruCommndList[4])
            if rm: 
                await message.channel.send(RushiCommndList[0])
            if rl: 
                await message.channel.send(RushiCommndList[1])
            if rn: 
                await message.channel.send(RushiCommndList[2])
            if ro: 
                await message.channel.send(RushiCommndList[3])
            if rp: 
                await message.channel.send(RushiCommndList[4])
#ループ処理
time_check.start()
# Botの起動とDiscordサーバーへの接続
client.run(token)
