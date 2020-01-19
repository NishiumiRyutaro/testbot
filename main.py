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
from foo import mlist
from foo import MarisuMyMCommndList
from foo import MarisuMyECommndList
from foo import RMarisuCommndList
from foo import GrandCommndList
from foo import AlldateTimeList
from foo import FOdateTimeList
from foo import readydateTimeList



token = os.getenv('DISCORD_TOKEN')
#channel_id = 644583189331050537
TsuyoCHANNEL_ID = 627287563190665217 #チャンネルID
RushiCHANNEL_ID = 627064056771248128 #チャンネルID
AruCHANNEL_ID = 627064032280444938 #チャンネルID
MarisuCHANNEL_ID = 627329328333455373 #チャンネルID
GrandCHANNEL_ID = 656850361541197835 #チャンネルID


# 接続に必要なオブジェクトを生成
client = discord.Client()
# 起動時に動作する処理
@client.event
async def on_ready():
    print('ready')

async def AllSendMessage():
    channel = client.get_channel(channel_id)
    await channel.send('攻撃アビ発動5分前です')
    await channel.send('防衛アビ発動5分前です')
    await channel.send('副団アビ発動5分前です。次の副団アビは23時です。')
    await asyncio.sleep(35)    
async def FOSendMessage():
    channel = client.get_channel(channel_id)
    await channel.send('副団アビ発動5分前です')
    await asyncio.sleep(35)
async def readySendMessage():
    channel = client.get_channel(channel_id)
    await channel.send('古戦場だよ')
    await asyncio.sleep(35)
    
# 30秒に一回ループ
@tasks.loop(seconds=0)
async def time_check():
    # 現在の時刻
    now = datetime.now().strftime('%H:%M:%S')     
    
# メッセージ受信時に動作する処理
@client.event
async def on_message(message):
    print('[' + message.author.name + ']' + message.content)
    if message.author.bot:
        return
    # 使用できるコマンド一覧
    if message.content == '!join':   
        role = discord.utils.get(message.guild.roles, name='test')
        await message.author.add_roles(role)
        reply = f'{message.author.mention} ようこそ！'
        await message.channel.send(reply)
    if message.content == '!specification':
        await message.channel.send('normal')
    if message.content == '!nowtime':
        now = datetime.now().strftime('%H:%M:%S')
        await message.channel.send(now)
    if message.content == '!list':
        testcmd = ",".join(allcmdlist)                              # コマンドリスト関連
        testcmd_new = testcmd.replace(',', '\n')                    #
        #allcmdlist_new =  testcmd_new.split(",")                    #
        await message.channel.send(testcmd_new.replace('"', '\n'))  #
    if message.content == '!mlist':
        await message.channel.send('\n'+mlist[0]+'\n'+mlist[1]+'\n'+mlist[2]+'\n'+mlist[3])
    if message.content != None:
        x = message.content
        if x.find('!') == 0:
            await message.delete()
            fromname = ('from'+' '+message.author.name)
            a = re.search(r',.*', x)
            #b = re.search(r'@.*', x, flags=re.DOTALL)
            if re.findall('^!', x, flags=re.IGNORECASE):
                tm = re.search(r'tb2030', x, flags=re.DOTALL)
                tl = re.search(r'tb2100', x, flags=re.DOTALL)
                tn = re.search(r'tb2130', x, flags=re.DOTALL)
                to = re.search(r'tb2200', x, flags=re.DOTALL)
                tp = re.search(r'tb2230', x, flags=re.DOTALL)
                mm = re.search(r'tm2030', x, flags=re.DOTALL)
                ml = re.search(r'tm2100', x, flags=re.DOTALL)
                mn = re.search(r'tm2130', x, flags=re.DOTALL)
                mo = re.search(r'tm2200', x, flags=re.DOTALL)
                mp = re.search(r'tm2230', x, flags=re.DOTALL)
                rvmo = re.search(r'rm2030', x, flags=re.DOTALL)
                rvmt = re.search(r'rm2100', x, flags=re.DOTALL)
                rvmth = re.search(r'rm2130', x, flags=re.DOTALL)
                rvmf = re.search(r'rm2200', x, flags=re.DOTALL)
                rvmfi = re.search(r'rm2230', x, flags=re.DOTALL)
                rvms = re.search(r'rm2300', x, flags=re.DOTALL)
                rvmse = re.search(r'rm2330', x, flags=re.DOTALL)
                rvme = re.search(r'rm2400', x, flags=re.DOTALL)
                rvmni = re.search(r'rm2430', x, flags=re.DOTALL)
                gro = re.search(r'gr2030', x, flags=re.DOTALL)
                grt = re.search(r'gr2100', x, flags=re.DOTALL)
                grth = re.search(r'gr2130', x, flags=re.DOTALL)
                grf = re.search(r'gr2200', x, flags=re.DOTALL)
                grfi = re.search(r'gr2230', x, flags=re.DOTALL)
                grs = re.search(r'gr2300', x, flags=re.DOTALL)
                grse = re.search(r'gr2330', x, flags=re.DOTALL)
                gre = re.search(r'gr2400', x, flags=re.DOTALL)
                grni = re.search(r'gr2430', x, flags=re.DOTALL)
                am = re.search(r'ab2030', x, flags=re.DOTALL)
                al = re.search(r'ab2100', x, flags=re.DOTALL)
                an = re.search(r'ab2130', x, flags=re.DOTALL)
                ao = re.search(r'ab2200', x, flags=re.DOTALL)
                ap = re.search(r'ab2230', x, flags=re.DOTALL)
                rm = re.search(r'rs2100', x, flags=re.DOTALL)
                rl = re.search(r'rs2130', x, flags=re.DOTALL)
                rn = re.search(r'rs2200', x, flags=re.DOTALL)
                ro = re.search(r'rs2230', x, flags=re.DOTALL)
                rp = re.search(r'rs2300', x, flags=re.DOTALL)
            if a != None :
                moji = a.group(0).replace(',', '')
                #obj = re.search(r'[0-9０-９]*', moji)
                if moji != None :
                    #await message.channel.send(moji)
                    #await message.channel.send(obj)
                    a = int(moji)
                    #await message.channel.send(a)
                    if a is not None and a >= 1 and a <= 31 :
                        a = str(a)
                        if tm:
                            channel = client.get_channel(TsuyoCHANNEL_ID)
                            await channel.send(TsuyoCHANNEL_ID)
                            await channel.send(a+'日'+ProtCommndList[0]+fromname)
                        if tl:
                            channel = client.get_channel(TsuyoCHANNEL_ID)
                            await channel.send(a+'日'+ProtCommndList[1]+fromname)
                        if tn:
                            channel = client.get_channel(TsuyoCHANNEL_ID)
                            await channel.send(a+'日'+ProtCommndList[2]+fromname)
                        if to:
                            channel = client.get_channel(TsuyoCHANNEL_ID)
                            await channel.send(a+'日'+ProtCommndList[3]+fromname)
                        if tp:
                            channel = client.get_channel(TsuyoCHANNEL_ID)
                            await channel.send(a+'日'+ProtCommndList[4]+fromname)
                        if mm:
                            channel = client.get_channel(MarisuCHANNEL_ID)
                            await channel.send(a+'日'+MarisuCommndList[0]+fromname)
                        if ml:
                            channel = client.get_channel(MarisuCHANNEL_ID)
                            await channel.send(a+'日'+MarisuCommndList[1]+fromname)
                        if mn:
                            channel = client.get_channel(MarisuCHANNEL_ID)
                            await channel.send(a+'日'+MarisuCommndList[2]+fromname)
                        if mo:
                            channel = client.get_channel(MarisuCHANNEL_ID)
                            await channel.send(a+'日'+MarisuCommndList[3]+fromname)
                        if mp:
                            channel = client.get_channel(MarisuCHANNEL_ID)
                            await channel.send(a+'日'+MarisuCommndList[4]+fromname)
                        if rvmo:
                            channel = client.get_channel(MarisuCHANNEL_ID)
                            await channel.send(a+'日'+RMarisuCommndList[0]+fromname)
                        if rvmt:
                            channel = client.get_channel(MarisuCHANNEL_ID)
                            await channel.send(a+'日'+RMarisuCommndList[1]+fromname)
                        if rvmth:
                            channel = client.get_channel(MarisuCHANNEL_ID)
                            await channel.send(a+'日'+RMarisuCommndList[2]+fromname)
                        if rvmf:
                            channel = client.get_channel(MarisuCHANNEL_ID)
                            await channel.send(a+'日'+RMarisuCommndList[3]+fromname)
                        if rvmfi:
                            channel = client.get_channel(MarisuCHANNEL_ID)
                            await channel.send(a+'日'+RMarisuCommndList[4]+fromname)
                        if rvms:
                            channel = client.get_channel(MarisuCHANNEL_ID)
                            await channel.send(a+'日'+RMarisuCommndList[5]+fromname)
                        if rvmse:
                            channel = client.get_channel(MarisuCHANNEL_ID)
                            await channel.send(a+'日'+RMarisuCommndList[6]+fromname)
                        if rvme:
                            channel = client.get_channel(MarisuCHANNEL_ID)
                            await channel.send(a+'日'+RMarisuCommndList[7]+fromname)
                        if rvmni:
                            channel = client.get_channel(MarisuCHANNEL_ID)
                            await channel.send(a+'日'+RMarisuCommndList[8]+fromname)
                        if gro:
                            channel = client.get_channel(GrandCHANNEL_ID)
                            await channel.send(a+'日'+GrandCommndList[0]+fromname)
                        if grt:
                            channel = client.get_channel(GrandCHANNEL_ID)
                            await channel.send(a+'日'+GrandCommndList[1]+fromname)
                        if grth:
                            channel = client.get_channel(GrandCHANNEL_ID)
                            await channel.send(a+'日'+GrandCommndList[2]+fromname)
                        if grf:
                            channel = client.get_channel(GrandCHANNEL_ID)
                            await channel.send(a+'日'+GrandCommndList[3]+fromname)
                        if grfi:
                            channel = client.get_channel(GrandCHANNEL_ID)
                            await channel.send(a+'日'+GrandCommndList[4]+fromname)
                        if grs:
                            channel = client.get_channel(GrandCHANNEL_ID)
                            await channel.send(a+'日'+GrandCommndList[5]+fromname)
                        if grse:
                            channel = client.get_channel(GrandCHANNEL_ID)
                            await channel.send(a+'日'+GrandCommndList[6]+fromname)
                        if gre:
                            channel = client.get_channel(GrandCHANNEL_ID)
                            await channel.send(a+'日'+GrandCommndList[7]+fromname)
                        if grni:
                            channel = client.get_channel(GrandCHANNEL_ID)
                            await channel.send(a+'日'+GrandCommndList[8]+fromname)
                        if am:
                            channel = client.get_channel(AruCHANNEL_ID)
                            await channel.send(a+'日'+AruCommndList[0]+fromname)
                        if al:
                            channel = client.get_channel(AruCHANNEL_ID)
                            await channel.send(a+'日'+AruCommndList[1]+fromname)
                        if an:
                            channel = client.get_channel(AruCHANNEL_ID)
                            await channel.send(a+'日'+AruCommndList[2]+fromname)
                        if ao:
                            channel = client.get_channel(AruCHANNEL_ID)
                            await channel.send(a+'日'+AruCommndList[3]+fromname)
                        if ap:
                            channel = client.get_channel(AruCHANNEL_ID)
                            await channel.send(a+'日'+AruCommndList[4]+fromname)
                        if rm: 
                            channel = client.get_channel(RushiCHANNEL_ID)
                            await channel.send(a+'日'+RushiCommndList[0]+fromname)
                        if rl: 
                            channel = client.get_channel(RushiCHANNEL_ID)
                            await channel.send(a+'日'+RushiCommndList[1]+fromname)
                        if rn: 
                            channel = client.get_channel(RushiCHANNEL_ID)
                            await channel.send(a+'日'+RushiCommndList[2]+fromname)
                        if ro: 
                            channel = client.get_channel(RushiCHANNEL_ID)
                            await channel.send(a+'日'+RushiCommndList[3]+fromname)
                        if rp: 
                            channel = client.get_channel(RushiCHANNEL_ID)
                            await channel.send(a+'日'+RushiCommndList[4]+fromname)
            else :
                if tm:
                    channel = client.get_channel(TsuyoCHANNEL_ID)
                    await channel.send(ProtCommndList[0]+fromname)
                if tl:
                    channel = client.get_channel(TsuyoCHANNEL_ID)
                    await channel.send(ProtCommndList[1]+fromname)
                if tn:
                    channel = client.get_channel(TsuyoCHANNEL_ID)
                    await channel.send(ProtCommndList[2]+fromname)
                if to:
                    channel = client.get_channel(TsuyoCHANNEL_ID)
                    await channel.send(ProtCommndList[3]+fromname)
                if tp:
                    channel = client.get_channel(TsuyoCHANNEL_ID)
                    await channel.send(ProtCommndList[4]+fromname)
                if mm:
                    channel = client.get_channel(MarisuCHANNEL_ID)
                    await channel.send(MarisuCommndList[0]+fromname)
                if ml:
                    channel = client.get_channel(MarisuCHANNEL_ID)
                    await channel.send(MarisuCommndList[1]+fromname)
                if mn:
                    channel = client.get_channel(MarisuCHANNEL_ID)
                    await channel.send(MarisuCommndList[2]+fromname)
                if mo:
                    channel = client.get_channel(MarisuCHANNEL_ID)
                    await channel.send(MarisuCommndList[3]+fromname)
                if mp:
                    channel = client.get_channel(MarisuCHANNEL_ID)
                    await channel.send(MarisuCommndList[4]+fromname)
                if rvmo:
                    channel = client.get_channel(MarisuCHANNEL_ID)
                    await channel.send(RMarisuCommndList[0]+fromname)
                if rvmt:
                    channel = client.get_channel(MarisuCHANNEL_ID)
                    await channel.send(RMarisuCommndList[1]+fromname)
                if rvmth:
                    channel = client.get_channel(MarisuCHANNEL_ID)
                    await channel.send(RMarisuCommndList[2]+fromname)
                if rvmf:
                    channel = client.get_channel(MarisuCHANNEL_ID)
                    await channel.send(RMarisuCommndList[3]+fromname)
                if rvmfi:
                    channel = client.get_channel(MarisuCHANNEL_ID)
                    await channel.send(RMarisuCommndList[4]+fromname)
                if rvms:
                    channel = client.get_channel(MarisuCHANNEL_ID)
                    await channel.send(RMarisuCommndList[5]+fromname)
                if rvmse:
                    channel = client.get_channel(MarisuCHANNEL_ID)
                    await channel.send(RMarisuCommndList[6]+fromname)
                if rvme:
                    channel = client.get_channel(MarisuCHANNEL_ID)
                    await channel.send(RMarisuCommndList[7]+fromname)
                if rvmni:
                    channel = client.get_channel(MarisuCHANNEL_ID)
                    await channel.send(RMarisuCommndList[8]+fromname)
                if gro:
                    channel = client.get_channel(GrandCHANNEL_ID)
                    await channel.send(GrandCommndList[0]+fromname)
                if grt:
                    channel = client.get_channel(GrandCHANNEL_ID)
                    await channel.send(GrandCommndList[1]+fromname)
                if grth:
                    channel = client.get_channel(GrandCHANNEL_ID)
                    await channel.send(GrandCommndList[2]+fromname)
                if grf:
                    channel = client.get_channel(GrandCHANNEL_ID)
                    await channel.send(GrandCommndList[3]+fromname)
                if grfi:
                    channel = client.get_channel(GrandCHANNEL_ID)
                    await channel.send(GrandCommndList[4]+fromname)
                if grs:
                    channel = client.get_channel(GrandCHANNEL_ID)
                    await channel.send(GrandCommndList[5]+fromname)
                if grse:
                    channel = client.get_channel(GrandCHANNEL_ID)
                    await channel.send(GrandCommndList[6]+fromname)
                if gre:
                    channel = client.get_channel(GrandCHANNEL_ID)
                    await channel.send(GrandCommndList[7]+fromname)
                if grni:
                    channel = client.get_channel(GrandCHANNEL_ID)
                    await channel.send(GrandCommndList[8]+fromname)
                if am:
                    channel = client.get_channel(AruCHANNEL_ID)
                    await channel.send(AruCommndList[0]+fromname)
                if al:
                    channel = client.get_channel(AruCHANNEL_ID)
                    await channel.send(AruCommndList[1]+fromname)
                if an:
                    channel = client.get_channel(AruCHANNEL_ID)
                    await channel.send(AruCommndList[2]+fromname)
                if ao:
                    channel = client.get_channel(AruCHANNEL_ID)
                    await channel.send(AruCommndList[3]+fromname)
                if ap:
                    channel = client.get_channel(AruCHANNEL_ID)
                    await channel.send(AruCommndList[4]+fromname)
                if rm: 
                    channel = client.get_channel(RushiCHANNEL_ID)
                    await channel.send(RushiCommndList[0]+fromname)
                if rl: 
                    channel = client.get_channel(RushiCHANNEL_ID)
                    await channel.send(RushiCommndList[1]+fromname)
                if rn: 
                    channel = client.get_channel(RushiCHANNEL_ID)
                    await channel.send(RushiCommndList[2]+fromname)
                if ro: 
                    channel = client.get_channel(RushiCHANNEL_ID)
                    await channel.send(RushiCommndList[3]+fromname)
                if rp: 
                    channel = client.get_channel(RushiCHANNEL_ID)
                    await channel.send(RushiCommndList[4]+fromname)
#ループ処理
time_check.start()
# Botの起動とDiscordサーバーへの接続
client.run(token)

