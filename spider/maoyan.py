#url:http://piaofang.maoyan.com/

import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:39.0) Gecko/20100101 Firefox/39.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate',
    'Connection': 'keep-alive'}

def boxoffice(day="2016-05-01"):
    html=requests.get('http://piaofang.maoyan.com/?date=%s&cnt=10&_v_=yes'%day,headers=headers,timeout=50).text.replace('\n','')
    table=BeautifulSoup(html,'lxml').find('div',id='ticket_tbody').find_all('ul')
    result=[]
    for item in table:
        movie={}
        movie['name']=item.find('li').find('b').get_text()
        movie['url']=item.get('data-com').replace("hrefTo,href:'",'').replace("'",'')
        movie['release-days']=item.find('li',attrs={'class':'c1'}).find('em').get_text()
        movie['boxoffice']=item.find('li',attrs={'class':'c1'}).find_all('em')[-1].get_text()
        movie['boxoffice-today']=item.find('li',attrs={'class':'c2'}).get_text()
        movie['boxoffice-accounting']=item.find('li',attrs={'class':'c3'}).get_text()
        movie['row-piece-rate']=item.find('li',attrs={'class':'c4'}).get_text()
        movie['occupancy']=item.find('li',attrs={'class':'c5'}).get_text()
        result.append(movie)
    return result

def movieinfor(movieurl):
    html=requests.get(movieurl,headers=headers).text
    movie={}
    soup=BeautifulSoup(html,'lxml')
    infor=soup.find('aside',attrs={'class':'infos'}).find_all('p')
    movie['type']=infor[0].get_text().replace('类型：','')
    movie['release-date']=infor[3].get_text().replace('上映日期：','')
    tags=soup.find('article',attrs={'class':'tags clearfix'}).find_all('span')
    try:
        movie['boxoffice']=tags[0].get_text().replace('总票房:','')
    except:
        movie['boxoffice']=''
    try:
        movie['firstweek-boxoffice']=tags[1].get_text().replace('首周票房:','')
    except:
        movie['firstweek-boxoffice']=''
    table=soup.find('div',id='ticket_tbody').find_all('ul')
    day_boxoffice=[]
    for item in table:
        day={}
        lis=item.find_all('li')
        day['date']=lis[0].find('b').get_text()
        day['boxoffice-today']=lis[1].get_text()
        day['boxoffice-accounting']=lis[2].get_text()
        day['row-piece-rate']=lis[3].get_text()
        day['visits']=lis[4].get_text()
        day_boxoffice.append(day)
    movie['day-boxoffice']=day_boxoffice
    return movie
