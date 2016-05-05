#coding:utf-8

import requests
import xlwt3
from bs4 import BeautifulSoup
import re


headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:39.0) Gecko/20100101 Firefox/39.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate',
    'Connection': 'keep-alive'}

def community(pageurl):
    html=requests.get(pageurl,headers=headers).text
    table=BeautifulSoup(html,'lxml').find('div',id='list-content').find_all('div',attrs={'class':'li-itemmod'})
    result=[]
    for item in table:
        hourse={}
        hourse['url']=item.find('a').get('href')
        hourse['name']=item.find('a').get('title')
        hourse['address']=item.find('address').get_text().replace('\n','').replace(' ','')
        hourse['price']=item.find('div',attrs={'class':'li-side'}).find('p').get_text().replace('\n','').replace(' ','')
        result.append(hourse)
    return result

def newhourse(pageurl):
    html=requests.get(pageurl,headers=headers).text
    table=BeautifulSoup(html,'lxml').find('div',attrs={'class':'key-list'}).find_all('div',attrs={'class':'item-mod'})
    result=[]
    for item in table:
        hourse={}
        hourse['url']=item.find('a').get('href')
        hourse['name']=item.find('div',attrs={'class':'lp-name'}).find('h3').get_text()
        hourse['address']=item.find('p',attrs={'class':'address'}).get_text().replace('\xa0','').replace('\n','')
        try:
            hourse['price']=item.find('p',attrs={'class':'price'}).get_text()
        except:
            hourse['price']=''
        hourse['tel']=item.find('p',attrs={'class':'tel'}).get_text()
        result.append(hourse)
    return result
