#encoding=utf-8
import json
import requests
import time
import numpy

headers = {
	'Accept': 'application/json, text/javascript, */*; q=0.01',
	'Accept-Encoding': 'gzip, deflate, br',
	'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
	'Connection': 'keep-alive',
	'Content-Length': '25',
	'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
	'Host': 'www.lagou.com',
	'Origin': 'https://www.lagou.com',
	'Referer': 'https://www.lagou.com/jobs/list_linux?city=%E6%9D%AD%E5%B7%9E&cl=false&fromSearch=true&labelWords=&suginput=',
	'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36',
	'X-Anit-Forge-Code': '0',
	'X-Anit-Forge-Token': 'None',
	'X-Requested-With': 'XMLHttpRequest',
}
url = 'https://www.lagou.com/jobs/positionAjax.json'



for j in range(30):
	try:
		html = requests.get(url, headers = headers).text
		time.sleep(numpy.random.rand()*10)
		json_obj = json.loads(html)
		positionresult = json_obj['content']['positionResult']
		result = positionresult['result']
		for i in range(15):
			print(result[i]['companyShortName'])
	except:
		print("failure")
		continue

