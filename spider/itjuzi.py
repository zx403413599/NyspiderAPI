#url:https://www.itjuzi.com/

import requests
from bs4 import BeautifulSoup
import time

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:39.0) Gecko/20100101 Firefox/39.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate',
    'Connection': 'keep-alive'}

def investevents(page):
    html=requests.get('https://www.itjuzi.com/investevents?page=%s'%page,headers=headers,timeout=50).text
    result=[]
    table=BeautifulSoup(html,'html.parser').find_all('ul',attrs={'class':'list-main-eventset'})[1].find_all('li')
    for li in table:
        item={}
        i=li.find_all('i')
        item['date']=i[0].get_text().replace('\n','').replace('\t','')
        item['url']=i[1].find('a').get('href')
        spans=i[2].find_all('span')
        item['name']=spans[0].get_text().replace('\n','').replace('\t','')
        item['industry']=spans[1].get_text().replace('\n','').replace('\t','')
        item['local']=spans[2].get_text().replace('\n','').replace('\t','')
        item['round']=i[3].get_text().replace('\n','').replace('\t','')
        item['capital']=i[4].get_text().replace('\n','').replace('\t','')
        companys=i[5].find_all('a')
        Investmenters=''
        if(companys==[]):
            Investmenters=i[5].get_text().replace('\n','').replace('\t','')
        else:
            for a in companys:
                Investmenters+=a.get_text().replace('\n','').replace('\t','')+';'
        item['Investmenters']=Investmenters
        result.append(item)
    return result

def merger(page):
    html=requests.get('https://www.itjuzi.com/merger?page=%s'%page,headers=headers,timeout=50).text
    result=[]
    table=BeautifulSoup(html,'html.parser').find_all('ul',attrs={'class':'list-main-eventset'})[1].find_all('li')
    for li in table:
        item={}
        i=li.find_all('i')
        item['date']=i[0].get_text().replace('\n','').replace('\t','')
        item['url']=i[1].find('a').get('href')
        spans=i[2].find_all('span')
        item['name']=spans[0].get_text().replace('\n','').replace('\t','')
        item['industry']=spans[1].get_text().replace('\n','').replace('\t','')
        item['local']=spans[2].get_text().replace('\n','').replace('\t','')
        item['round']=i[3].get_text().replace('\n','').replace('\t','')
        item['capital']=i[4].get_text().replace('\n','').replace('\t','')
        companys=i[5].find_all('a')
        acquirer=''
        if(companys==[]):
            acquirer=i[5].get_text().replace('\n','').replace('\t','')
        else:
            for a in companys:
                acquirer+=a.get_text().replace('\n','').replace('\t','')+';'
        item['acquirer']=acquirer
        result.append(item)
    return result

def foreign_investevents(page):
    html=requests.get('https://www.itjuzi.com/investevents/foreign?page=%s'%page,headers=headers,timeout=50).text
    result=[]
    table=BeautifulSoup(html,'html.parser').find_all('ul',attrs={'class':'list-main-eventset'})[1].find_all('li')
    for li in table:
        item={}
        i=li.find_all('i')
        item['date']=i[0].get_text().replace('\n','').replace('\t','')
        item['url']=i[1].find('a').get('href')
        spans=i[2].find_all('span')
        item['name']=spans[0].get_text().replace('\n','').replace('\t','')
        item['industry']=spans[1].get_text().replace('\n','').replace('\t','')
        item['local']=spans[2].get_text().replace('\n','').replace('\t','')
        item['round']=i[3].get_text().replace('\n','').replace('\t','')
        item['capital']=i[4].get_text().replace('\n','').replace('\t','')
        companys=i[5].find_all('a')
        Investmenters=''
        if(companys==[]):
            Investmenters=i[5].get_text().replace('\n','').replace('\t','')
        else:
            for a in companys:
                Investmenters+=a.get_text().replace('\n','').replace('\t','')+';'
        item['Investmenters']=Investmenters
        result.append(item)
    return result

def foreign_merger(page):
    html=requests.get('https://www.itjuzi.com/merger/foreign?page=%s'%page,headers=headers,timeout=50).text
    result=[]
    table=BeautifulSoup(html,'html.parser').find_all('ul',attrs={'class':'list-main-eventset'})[1].find_all('li')
    for li in table:
        item={}
        i=li.find_all('i')
        item['date']=i[0].get_text().replace('\n','').replace('\t','')
        item['url']=i[1].find('a').get('href')
        spans=i[2].find_all('span')
        item['name']=spans[0].get_text().replace('\n','').replace('\t','')
        item['industry']=spans[1].get_text().replace('\n','').replace('\t','')
        item['local']=spans[2].get_text().replace('\n','').replace('\t','')
        item['round']=i[3].get_text().replace('\n','').replace('\t','')
        item['capital']=i[4].get_text().replace('\n','').replace('\t','')
        companys=i[5].find_all('a')
        acquirer=''
        if(companys==[]):
            acquirer=i[5].get_text().replace('\n','').replace('\t','')
        else:
            for a in companys:
                acquirer+=a.get_text().replace('\n','').replace('\t','')+';'
        item['acquirer']=acquirer
        result.append(item)
    return result
