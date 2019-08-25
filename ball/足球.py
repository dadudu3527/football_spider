import requests
from lxml import etree
from bs4 import BeautifulSoup
import time
import re
import json
import string

def get_data(url,headers):
    response = requests.get(url=url,headers=headers).content.decode('utf-8')
    prttern_01 = re.compile(r'{"matchesTrans".*?}};')#公开赛事

    aaaa  = prttern_01.findall(response)[0][0:-1]
    print(aaaa)
    all_data = json.loads(aaaa)#转成json数据
    # print(all_data)
    for key in all_data:#查看数据key值
        print(key)
        # matchesTrans
        # events
        # teams
        # pankou
        # heightVal
        # lottery




    # list_all = all_data['matchesTrans']['live']#正在进行的比赛
    list_all = all_data['matchesTrans']['notStart']#未开始的比赛
    teams_all = all_data['teams']  #所有的球队
    # print('++++++++++++++++',teams_all)#所有的球队
    for list in list_all:
        print(list)
        tree = etree.HTML(response)
        name = tree.xpath('//label[@data-id="{}"]/span[1]/text()'.format(list[1]))#赛事
        zhu_team = teams_all['{}'.format(list[5][0])][0].split(',')#将主场球队名字切出来
        ke_team = teams_all['{}'.format(list[6][0])][0].split(',')#将客场球队名字切出来
        start_time = time.strftime('%H:%M',time.localtime(list[3]))
        print('赛事：',name[0],'---时间:',start_time,'---主场球队：',zhu_team[0],'---比分：','---客场球队：',ke_team[0])
    # soup = BeautifulSoup(response,'lxml')
    # with open('zuqiu.html','a',encoding='utf-8') as pf:
    #     pf.write(response)
    # print(soup)

if __name__ == '__main__':
    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Referer': 'https://live.leisu.com/',
        'Sec-Fetch-Mode': 'no-cors',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'
    }
    url = 'https://live.leisu.com'
    get_data(url,headers)


# https://api.leisu.com/api/v2/match/odds_detail?sid=2733796