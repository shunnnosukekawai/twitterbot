import urllib3
from bs4 import BeautifulSoup
import json

http = urllib3.PoolManager()
r = http.request('GET','https://www.nikkei.com/markets/kabu/')
soup = BeautifulSoup(r.data,"html.parser")

a =soup.select_one("#CONTENTS_MARROW > div.mk-top_stock_average.cmn-clearfix > div.cmn-clearfix > div.mkc-guidepost > div.mkc-prices > span.mkc-stock_prices")

a =a.text

#span要素を全て摘出する
span = soup.findAll("span")

#print時にエラーにならないよう最初に宣言
nikkei_heikin = ""

# for分で全てのspan要素の中からClass="mkc-stock_prices"となっている物を探します
for tag in span:
	# classの設定がされていない要素は、tag.get("class").pop(0)を行うことのできないでエラーとなるため、tryでエラーを回避する
	try:
        # tagの中からclass="n"のnの文字列を摘出します。複数classが設定されている場合があるので
        # get関数では配列で帰ってくる。そのため配列の関数pop(0)により、配列の一番最初を摘出する
        # <span class="hoge" class="foo">  →   ["hoge","foo"]  →   hoge
		string1 =tag.get("class").pop(0)
        # 摘出したclassの文字列にmkc-stock_pricesと設定されているかを調べます
		if string1 in "m-miH01C_rate":
        	# mkc-stock_pricesが設定されているのでtagで囲まれた文字列を.stringであぶり出します
			nikkei_heikin = tag.string
		#算出が完了したのでfor分をすり抜けます
			break

	except:
		#pass 何も処理を行わない
		pass

#摘出した日経平均株価を出力します。
print (nikkei_heikin)



