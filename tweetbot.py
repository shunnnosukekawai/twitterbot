# -*- coding: utf-8 -*-
from requests_oauthlib import OAuth1Session 
import json
import random
import datetime
import setting
CK = setting.CK 
CS =setting.CS
AT = setting.AT
AS = setting.AS

# ツイート投稿用のURL
url = "https://api.twitter.com/1.1/statuses/home_timeline.json"

# ツイート本文
params = {"status": "Hello, World!"}

#Auth認証で POST method で投稿
twitter = OAuth1Session(CK, CS, AT, AS)
req = twitter.get(url, params = params)

# レスポンスを確認

timeline = json.loads(req.text)

for tweet in timeline:
	print(tweet["text"])

tweets = ['ワオーン','チッピ']
randomtweet = tweets[random.randrange(len(tweets))]
timestamp = datetime.datetime.today()
timestamp = str(timestamp.strftime('%Y/%m/%d %H:%M'))

params = {'status':randomtweet + ' ' + timestamp}

req = twitter.post('https://api.twitter.com/1.1/statuses/update.json',params = params)


