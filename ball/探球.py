import requests
import time
import re
from lxml import etree
# url = 'http://op1.win007.com/Oddslist/1669445.htm'
url = 'http://1x2d.win007.com/1669445.js'

response = requests.get(url = url).content.decode('utf-8')
# print(response)
pattern_01 = re.compile(r'game=Array.*?;')
name_01 = pattern_01.findall(response)
# print(name_01)
pattern_02 = re.compile(r'(".*?")')
name_02 = pattern_02.findall(name_01[0])
# print(name_02)
for name in name_02:
    arr = name.split('|')
    print(arr)
    gongsi_name = arr[-3]
    zhusheng_0 = arr[3]
    he_0 =arr[4]
    keshenng_0 = [5]
    zhushenglv_0 =[6]
    helv_0 = [7]
    keshenglv_0 = [8]
    fanhuanlv_0 = [9]
    # kaili_0_1 =


# tree = etree.HTML(response)
# name = tree.xpath('//*[@id="oddstr_281"]/td[2]/a[1]/text()')

# print(name)