import os

import discord
from datetime import datetime
from discord.ext import tasks

token = os.getenv('DISCORD_TOKEN')
channel_id = os.getenv('CHANNEL_ID')

# 接続に必要なオブジェクトを生成
client = discord.Client()


#投稿する日時
DefensedateTimeList = [
'2019/11/13 09:50',
'2019/11/13 09:51',
'2019/11/13 09:52',
'2019/11/13 09:53',
'2019/11/13 09:54',
'2019/11/13 09:55',
'2019/11/13 09:56'
]

AttackdateTimeList = [
'2019/11/13 12:24:00',
'2019/05/25 07:00:00'
]
# 起動時に動作する処理
@client.event
async def on_ready():
    print('ready')

async def DSendMessage():
    channel = client.get_channel(channel_id)
    await channel.send('攻撃アビの時間だよ')
    await channel.send('防衛アビの時間だよ')
    await asyncio.sleep(30)
# 30秒に一回ループ
@tasks.loop(seconds=0)
async def time_check():
    await message.channel.send(now)
    sleepTime = 0
    # 現在の時刻
    now = datetime.now().strftime('%Y/%m/%d %H:%M')
    if now in DefensedateTimeList:
        await DSendMessage()
#該当時間だった場合は２重に投稿しないよう３０秒余計に待機
    #await asyncio.sleep(30)

# メッセージ受信時に動作する処理
@client.event
async def on_message(message):
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return
    # 使用できるコマンド一覧
    if message.content == '!help':
        now = datetime.now().strftime('%Y/%m/%d %H:%M')
        await message.channel.send(now)

#ループ処理
time_check.start()
# Botの起動とDiscordサーバーへの接続
client.run(token)
