#coding:utf-8

import requests
import json

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:39.0) Gecko/20100101 Firefox/39.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate',
    'Connection': 'keep-alive'}

def lagouJobs(page,keyword=''):
    js_data=requests.get('http://www.lagou.com/jobs/positionAjax.json?px=new&kd=%s&pn=%s&'%(keyword,page),headers=headers).text
    data=json.loads(js_data)
    data=data['content']['result']
    jobs=[]
    for item in data:
        job={}
        job['postiontype']=item['positionType']
        job['company']=item['companyShortName']
        job['salary']=item.get('salary')
        job['workYear']=item['workYear']
        job['education']=item['education']
        job['industryField']=item['industryField']
        job['companySize']=item['companySize']
        job['createTime']=item['createTime']
        job['city']=item['city']
        job['financeStage']=item['financeStage']
        jobs.append(job)
    return jobs
