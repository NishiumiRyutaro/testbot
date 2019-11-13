import os

import discord
from datetime import datetime
from discord.ext import tasks

token = os.getenv('DISCORD_TOKEN')
# 接続に必要なオブジェクトを生成
client = discord.Client()


#投稿する日時
DefensedateTimeList = [
'2019/11/13 19:00:00',
'2019/11/13 18:30:00',
'2019/11/13 12:46:00',
'2019/05/22 07:00:00',
'2019/05/23 07:00:00',
'2019/05/24 07:00:00',
'2019/05/25 07:00:00'
]
# 起動時に動作する処理
@client.event
async def on_ready():
    print('ready')

async def DSendMessage():
    channel = client.get_channel(CHANNEL_ID)
    await channel.send('攻撃アビの時間だよ')
    await channel.send('防衛アビの時間だよ')
    await asyncio.sleep(30)
# 30秒に一回ループ
@tasks.loop(seconds=0)
async def time_check():
    sleepTime = 0
    # 現在の時刻
    now = datetime.now().strftime('%Y/%m/%d %H:%M:%S')
    if now in DefensedateTimeList:
        print(now)
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
        await message.channel.send('現在使用できるコマンドはありません')

#ループ処理
time_check.start()
# Botの起動とDiscordサーバーへの接続
client.run(token)
