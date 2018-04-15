# -*- coding: utf-8 -*-
from requests_oauthlib import OAuth1Session 
import json
import random
import datetime
CK = 'BvIg7lWfYhl9RHe7p3erlxLNf'  #consumerkey
CS = 'Yo1tsibL1KNDoiRpipPyN8UohI4Wq3dTwKlAwbdJAEN4Z0l9ZT' #consumer secret
AT = '825155594365526016-gfooV9FnXL5z98Pue4CkpC6nDfOpwjp' # access token
AS = 'iW4hmqiVfAQcsYyQiyoLqaTMhmu1oGzMiMOD6kPnVCbxO' # access token secret

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


