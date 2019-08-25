import requests
from lxml import etree
from bs4 import BeautifulSoup
import time
from selenium import webdriver
print()




def get_data(url):
    driver = webdriver.PhantomJS(executable_path=r'C:\Users\15974\Desktop\phantomjs-2.1.1-windows\bin\phantomjs.exe')
    driver.get(url=url)
    driver.save_screenshot('jinqu.png')
if __name__ == '__main__':
    url = 'https://live.leisu.com'
    get_data(url)
    path ='//*[@id="list"]/tbody/tr[2]/td[2]/a'