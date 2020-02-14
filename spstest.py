import discord
import urllib.request
import json
import re
import gspread
from pdf2image import convert_from_path
from oauth2client.service_account import ServiceAccountCredentials

client = discord.Client()

###################################
# 定義
###################################
#spreadsheet
spreadsheet_url = "https://docs.google.com/spreadsheets/d/1qBNUJ1hkDg2N5v26ml5NAIua8HOZhxlO2PBlCeJVZIM/edit#gid=2122610144"

#2つのAPIを記述しないとリフレッシュトークンを3600秒毎に発行し続けなければならない
scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']

#認証情報設定（ファイルはgoogleの認証情報をリネーム）
credentials = ServiceAccountCredentials.from_json_keyfile_name('./testprogram-268103-c5de3b903380.json', scope)

#OAuth2の資格情報を使用してGoogle APIにログインします。
gc = gspread.authorize(credentials)

###################################
# 実行部分
###################################
@client.event
async def on_message(message):
    if message.author != client.user:
    # get_imageでスプレッドシートの画像取得実行
        if "!get_image" in message.content:
           #pdf取得
           pdf_export_url = 'https://docs.google.com/spreadsheets/d/' + '1qBNUJ1hkDg2N5v26ml5NAIua8HOZhxlO2PBlCeJVZIM' + '/export?format=pdf&gid='+'2122610144'
           pdf_name = "output.pdf"
           urllib.request.urlretrieve(pdf_export_url, pdf_name)
        
           #画像変換
           image = convert_from_path(pdf_name)
           image[0].save('output.png', 'png')
        
           #変換した画像ファイル送信
           imgname = ('output.png')
           #await message.channel.send(pdf_name,'output.png'))
           await message.channel.send('プログラムは動作しています'))  
client.run(token)

