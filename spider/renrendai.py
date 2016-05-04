#url:http://www.we.com

#passwd为加密后的密码

import requests
from bs4 import BeautifulSoup

class Renrendai():
    def __init__(self,username,passwd):
        self.session=requests.session()
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:39.0) Gecko/20100101 Firefox/39.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate',
            'Connection': 'keep-alive'}
        self.username=username
        self.passwd=passwd
        self.login()

    def login(self):
        data={
            'j_username':self.username,
            'j_password':self.passwd,
            'rememberme':'on',
            'targetUrl':'http://www.we.com/',
            'returnUrl':'https://www.we.com/account/index.action'}
        self.session.post('https://www.we.com/j_spring_security_check',data=data,headers=self.headers).text

    def getLoan(self,loanid):
        try:
            html=self.session.get('http://www.we.com/lend/detailPage.action?loanId=%s'%loanid,headers=self.headers).text
            LoanInfor=self.parser(html)
            return LoanInfor
        except:
            return False

    def parser(self,html):
        soup=BeautifulSoup(html,'lxml').find('div',id='pg-loan-invest')
        infor_one=soup.find('div',id='loan-basic-panel')
        infor={}
        infor['Loan_type']=infor_one.find('div',attrs={'class':'fn-left fn-text-overflow pl25'}).get('title')
        infor['Loan_Title']=infor_one.find('em',attrs={'class':'title-text'}).get_text()
        em=infor_one.find('div',attrs={'class':'fn-clear  mb25'}).find_all('em')
        infor['Amount']=em[0].get_text()
        infor['Interest_Rate']=em[1].get_text()
        infor['Term']=em[3].get_text()
        ul=infor_one.find('div',attrs={'class':'fn-left pt10 loaninfo '}).find('ul').find_all('li')
        infor['Guarantee_Type']=ul[0].find('span',attrs={'class':'fn-left basic-value last'}).get_text()
        infor['Early_Repayment_Rate']=ul[0].find('span',attrs={'class':'fn-left basic-value num'}).get_text()
        infor['Repayment_Type']=ul[1].find('span',attrs={'class':'fn-left basic-value'}).get_text()
        statue=infor_one.find('div',attrs={'class':'pl25 pr25 fn-clear'}).find('div',attrs={'class':'stamp'}).find('em').get('class')
        infor['Loan_Status']=statue[0]
        if statue==['REPAYING']:
            infor['Term_Remain']=infor_one.find('div',attrs={'class':'pl25 pr25 fn-clear'}).find('div',attrs={'class':'box box-top'}).find('i').get_text()
            infor['Next_Payment_Day']=infor_one.find('div',attrs={'class':'pl25 pr25 fn-clear'}).find('div',attrs={'class':'box box-bottom'}).find('i').get_text()
        else:
            infor['Term_Remain']=''
            infor['Next_Payment_Day']=''
        table=soup.find('div',id='loan-details').find('table',attrs={'class':'ui-table-basic-list'}).find_all('tr')
        infor['Borrower_Id']=table[0].find('em').get_text()
        infor['Userid']=table[0].find('em').find('a').get('href').replace('/account/myInfo.action?userId=','')
        infor['Credit_Score']=table[0].find_all('em')[1].get('title')
        infor['Des']=soup.find('div',attrs={'class':'ui-tab-list color-dark-text'}).get_text().replace('\n','').replace('\t','')
        em=table[2].find_all('em')
        infor['Age']=em[0].get_text().replace('\n','').replace('\t','')
        infor['Education']=em[1].get_text().replace('\n','').replace('\t','')
        infor['Marital status']=em[2].get_text().replace('\n','').replace('\t','')
        em=table[4].find_all('em')
        infor['Number_of_Borrow']=em[0].get_text().replace('\n','').replace('\t','')
        infor['Credit_Limit']=em[1].get_text().replace('\n','').replace('\t','')
        infor['Overdue_amount']=em[2].get_text().replace('\n','').replace('\t','')
        em=table[5].find_all('em')
        infor['Number_of_Succesful_Loan']=em[0].get_text().replace('\n','').replace('\t','')
        infor['Total_Amount']=em[1].get_text().replace('\n','').replace('\t','')
        infor['Number_Arrears']=em[2].get_text().replace('\n','').replace('\t','')
        em=table[6].find_all('em')
        infor['Number_of_Repaid']=em[0].get_text().replace('\n','').replace('\t','')
        infor['Outstanding']=em[1].get_text().replace('\n','').replace('\t','')
        infor['Severe_overdue']=em[2].get_text().replace('\n','').replace('\t','')
        em=table[8].find_all('em')
        infor['Income_Range_Monthly']=em[0].get_text().replace('\n','').replace('\t','')
        infor['Homeowner']=em[1].get_text().replace('\n','').replace('\t','')
        infor['Mortgage']=em[2].get_text().replace('\n','').replace('\t','')
        em=table[9].find_all('em')
        infor['Car']=em[0].get_text().replace('\n','').replace('\t','')
        infor['Car_Loan']=em[1].get_text().replace('\n','').replace('\t','')
        em=table[11].find_all('em')
        infor['Working_City']=em[0].get_text().replace('\n','').replace('\t','')
        infor['Emploment_Length']=em[1].get_text().replace('\n','').replace('\t','')
        for item in soup.find('div',id='loan-details').find('table',attrs={'class':'ui-table-basic-list'}).find_all('td'):
            if item.get_text()[:4]=='公司行业':
                infor['Employment_Sector']=item.find('em').get_text()
            if item.get_text()[:4]=='公司规模':
                infor['Company_Scale']=item.find('em').get_text()
            if item.get_text()[:4]=='岗位职位':
                infor['Position']=item.find('em').get_text()
        return infor
