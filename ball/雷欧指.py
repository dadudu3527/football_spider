import re
import time
from lxml import etree
import requests

url = 'https://api.leisu.com/api/v2/match/odds_detail?sid=2733796'
headers = {
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
'Cookie': 'acw_tc=2f61f27615659363681365495e305a174e9c7bd415651c20bb3038b0111c52; Hm_lvt_63b82ac6d9948bad5e14b1398610939a=1565936370,1565957233,1566017933,1566046696; PHPSESSID=00qs3a1l8u4ju1g34vde51a0m2; ftb-music=-1; ftb-schedule-lottery=zc; SERVERID=4ab2f7c19b72630dd03ede01228e3e61|1566197751|1566171479; Hm_lpvt_63b82ac6d9948bad5e14b1398610939a=1566197753',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'
}
response = requests.get(url=url,headers = headers).content.decode('utf-8')
tree = etree.HTML(response)

