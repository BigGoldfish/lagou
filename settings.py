#encoding=utf-8
'''
    是否为第一页:first
    页码:pn
    职位名称:kd
    城市:city
'''
city = '杭州'
kd = 'linux'

filename = city + '-' + kd
para = {
    'first':'true',
    'pn':'1',
    'kd': kd,
    'city': city
}
url = 'https://www.lagou.com/jobs/positionAjax.json'

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
cookies = {
    'JSESSIONID':'ABAAABAAAGGABCBDB21D5CF07F7D347DDDD340CB63A8D22',
    '_ga':'GA1.2.1959103167.1544531718',
    'user_trace_token':'20181211203518-37a2ef31-fd41-11e8-8ced-5254005c3644',
    'LGUID':'20181211203518-37a2f4fe-fd41-11e8-8ced-5254005c3644',
    'Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6':'1544531718,1544663362,1544663444,1544667005',
    'index_location_city':'%E5%85%A8%E5%9B%BD',
    'sensorsdata2015jssdkcross':'%7B%22distinct_id%22%3A%22167a6bb1227cd3-0565244a59c5d-35617600-3686400-167a6bb1228ba%22%2C%22%24device_id%22%3A%22167a6bb1227cd3-0565244a59c5d-35617600-3686400-167a6bb1228ba%22%7D',
    'TG-TRACK-CODE':'index_search',
    '_gid':'GA1.2.312544047.1544969584',
    'LGSID':'20181218152232-af2ac3b9-0295-11e9-93c8-525400f775ce',
    'PRE_UTM':'',
    'PRE_HOST':'',
    'PRE_SITE':'https%3A%2F%2Fwww.lagou.com%2Fjobs%2Flist_linux%3Fpx%3Ddefault%26city%3D%25E6%259D%25AD%25E5%25B7%259E',
    'PRE_LAND':'https%3A%2F%2Fwww.lagou.com%2Fjobs%2Flist_linux%3Fcity%3D%25E6%259D%25AD%25E5%25B7%259E%26cl%3Dfalse%26fromSearch%3Dtrue%26labelWords%3D%26suginput%3D',
   'SEARCH_ID':'1595c75bca304f8c82b6c6c3247b22a4',
   '_gat':'1',
   'LGRID':'20181218154228-785a059f-0298-11e9-8d2c-5254005c3644',
   'Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6':'1545118949'
}
