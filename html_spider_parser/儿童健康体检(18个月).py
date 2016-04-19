from bs4 import BeautifulSoup
import time
import os
import pymysql
import re


def getAllFile(dirname):
    all_file = []
    for dirpath, dirnames, filenames in os.walk(dirname):
        for filename in filenames:
            all_file.append(filename)
    return all_file


def data_insert(database, values):
    sql = "INSERT INTO " + database + " VALUES ('"
    for v in range(0, len(values) - 1):
        sql += values[v] + "','"
    sql += values[len(values) - 1] + "')"
    cur.execute(sql)
    conn.commit()


def text(texts):
    return str(texts.pop(0).get('value'))


def radio(radios):
    radio=radios.pop(0)
    try:
        values = str(radio.find(attrs={"checked": "checked"}).next_sibling.string)
    except:
        values = 'None'
    return values
def check(checks):
    check=checks.pop(0)
    values = check.findAll(attrs={"checked": "checked"})
    v = ''
    for i in values:
        v += str(i.next_sibling.string) + ' '
    if not v:
        v = 'None'
    return v


def getBasicInfo(soup):
    BasicInfo = []
    BasicInfo.append(str(soup.find(attrs={"name": "ctl00$page_Content$SuiFangGRXX$dabh"}).get('value')))
    BasicInfo.append(str(soup.find(attrs={"name": "ctl00$page_Content$SuiFangGRXX$xm"}).get('value')))
    BasicInfo.append(str(soup.find(attrs={"name": "ctl00$page_Content$SuiFangGRXX$jtdh"}).get('value')))
    BasicInfo.append(str(soup.find(attrs={"name": "ctl00$page_Content$SuiFangGRXX$xb"}).get('value')))
    BasicInfo.append(str(soup.find(attrs={"name": "ctl00$page_Content$SuiFangGRXX$csrq"}).get('value')))
    BasicInfo.append(str(soup.find(attrs={"name": "ctl00$page_Content$SuiFangGRXX$sfzh"}).get('value')))
    BasicInfo.append(str(soup.find(attrs={"name": "ctl00$page_Content$SuiFangGRXX$lxr"}).get('value')))
    BasicInfo.append(str(soup.find(attrs={"name": "ctl00$page_Content$SuiFangGRXX$Tel"}).get('value')))
    BasicInfo.append(str(soup.find(attrs={"name": "ctl00$page_Content$SuiFangGRXX$hyzk"}).get('value')))
    BasicInfo.append(str(soup.find(attrs={"name": "ctl00$page_Content$SuiFangGRXX$xxdz"}).get('value')))
    BasicInfo.append(str(soup.find(attrs={"name": "ctl00$page_Content$SuiFangGRXX$ssdw"}).get('value')))
    BasicInfo.append(str(soup.find(attrs={"name": "ctl00$page_Content$SuiFangGRXX$jddw"}).get('value')))
    return BasicInfo


def getDetailInfo(soup):
    DetailInfo = []
    texts = soup.findAll(attrs={"id": re.compile('ctl00_page_Content_.*_tb$')})
    radios = soup.findAll(attrs={"id": re.compile('ctl00_page_Content_.*_radioList1$')})
    checks = soup.findAll(attrs={"id": re.compile('ctl00_page_Content_.*_chkList1$')})
    DetailInfo.append(text(texts)+' '+radio(radios))
    DetailInfo.append(text(texts)+' '+radio(radios))
    DetailInfo.append(text(texts))

    DetailInfo.append(check(checks)+' '+text(texts))
    DetailInfo.append(radio(radios)+' '+text(texts))
    DetailInfo.append(radio(radios)+' '+text(texts)+'*'+text(texts))
    DetailInfo.append(radio(radios)+' '+text(texts))
    DetailInfo.append(radio(radios)+' '+text(texts))
    DetailInfo.append(radio(radios)+' '+text(texts))
    DetailInfo.append(radio(radios))
    DetailInfo.append(radio(radios)+' '+text(texts))
    DetailInfo.append(radio(radios)+' '+text(texts))
    DetailInfo.append(radio(radios)+' '+text(texts))
    DetailInfo.append(radio(radios)+' '+text(texts))
    DetailInfo.append(check(checks))
    DetailInfo.append(radio(radios)+' '+text(texts))
    DetailInfo.append(check(checks))
    DetailInfo.append(text(texts))
    DetailInfo.append(radio(radios)+' '+text(texts))
    DetailInfo.append(text(texts))
    DetailInfo.append(text(texts))

    DetailInfo.append(text(texts))
    DetailInfo.append(text(texts))
    DetailInfo.append(radio(radios))
    DetailInfo.append(radio(radios)+' '+text(texts))
    DetailInfo.append(text(texts))

    DetailInfo.append(radio(radios)+' '+text(texts))
    DetailInfo.append(text(texts))
    DetailInfo.append(check(checks)+' '+text(texts))
    DetailInfo.append(text(texts))
    DetailInfo.append(text(texts))
    DetailInfo.append(text(texts))
    DetailInfo.append(text(texts))
    DetailInfo.append(text(texts))
    DetailInfo.append(text(texts))
    print(DetailInfo.__len__())
    return DetailInfo


if __name__ == "__main__":
    start = time.clock()
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123456', db='spider_data', charset='utf8')
    cur = conn.cursor()
    dir = 'D:\爬虫数据-医疗\爬虫数据-医疗-王伟伟\www-爬虫数据\爬虫原始数据\儿童健康体检(18个月)'
    allFiles = getAllFile(dirname=dir)
    count = 0
    for allFile in allFiles:
        if count >= 0:
            soup = BeautifulSoup(open(dir + '\\' + allFile, encoding="utf-8"), "lxml")
            basic = getBasicInfo(soup)
            detail = getDetailInfo(soup)
            basic.extend(detail)
            data_insert('儿童健康体检_18个月', basic)
        print(count)
        count += 1
    cur.close()
    conn.close()
    print('总时间为:', time.clock() - start)
