# -*- coding: utf-8 -*-
from requests_oauthlib import OAuth1Session
import json
import random
import datetime
import setting
import random
import os
import base64

CK = setting.CK 
CS =setting.CS
AT = setting.AT
AS = setting.AS

# ツイート投稿用のURL
url_text = "https://api.twitter.com/1.1/statuses/update.json"

url_media ="https://upload.twitter.com/1.1/media/upload.json"

#Auth認証で POST method で投稿
twitter = OAuth1Session(CK, CS, AT, AS)

#画像データをランダム取得
images = os.listdir('img/')
images = random.choice(images)
print(images)

with open ('img/' + images,'rb') as file1:
	file1 = file1.read()
	files = {'media':file1}

	req_media = twitter.post(url_media,files = files)
	print(req_media.text)
	
#レスポンスを確認
	if req_media.status_code != 200:
		print("画像アップロード失敗:%s" % req_media.text)
		print(req_media.text)
		exit()

	#Media IDを利用
	media_id = json.loads(req_media.text)['media_id']
	print("Media_id:%d" % media_id)
	
	#ランダムツイート
	rtweet = ['ランダム1','なまけもの1','テスティング1']
	rtweet = random.choice(rtweet)
	print (rtweet)

	#Media idを付与してテキストを投稿
	params = {'status':rtweet ,"media_id":[media_id]}
	req_media = twitter.post(url_text,params = params)

	#再びレスポンスを確認
	if req_media.status_code != 200:
		print("テキストアップデート失敗:%s"%req_media.text)
		exit()
print('OK')
