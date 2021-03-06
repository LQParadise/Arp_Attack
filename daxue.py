#!/usr/bin/env python
# coding=utf-8
import requests
from bs4 import BeautifulSoup
import bs4
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

def getHTMLText(url):
    try :
        r = requests.get(url,timeout = 30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text

    except:
        return ""

def fillUnivList(ulist,html):
    soup = BeautifulSoup(html,"html.parser")
    for tr in soup.find('tbody').children:
        if isinstance(tr,bs4.element.Tag):
            tds = tr.find_all('td')
            ulist.append([tds[0].string,tds[1].string,tds[2].string])

def printUnivList(ulist,num):
    cha = chr(32)
    h = cha
    tplt ="{0:^10}\t{1:{3}^10}\t{2:^10}"
    #print (tplt.format("paiming","xuexiao","fenshu",h))
    for i in range(num):
        u = ulist[i]
        print (tplt.format(i,u[1],u[2],h))

def main():
    uinfo=[]
    url = 'http://www.zuihaodaxue.cn/zuihaodaxuepaiming2017.html'
    html = getHTMLText(url)
    #print html
    fillUnivList(uinfo,html)
    printUnivList(uinfo,20)
main()
