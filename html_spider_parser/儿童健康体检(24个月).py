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
    radio = radios.pop(0)
    try:
        values = str(radio.find(attrs={"checked": "checked"}).next_sibling.string)
    except:
        values = 'None'
    return values


def check(checks):
    check = checks.pop(0)
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
    DetailInfo.append(text(texts) + ' ' + radio(radios))
    DetailInfo.append(text(texts) + ' ' + radio(radios))
    DetailInfo.append(text(texts))

    DetailInfo.append(check(checks) + ' ' + text(texts))
    DetailInfo.append(radio(radios) + ' ' + text(texts))
    DetailInfo.append(radio(radios) + ' ' + text(texts) + '*' + text(texts))
    DetailInfo.append(radio(radios) + ' ' + text(texts))
    DetailInfo.append(radio(radios) + ' ' + text(texts))
    DetailInfo.append(radio(radios) + ' ' + text(texts))
    DetailInfo.append(radio(radios))
    DetailInfo.append(check(checks))
    DetailInfo.append(radio(radios) + ' ' + text(texts))
    DetailInfo.append(radio(radios) + ' ' + text(texts))
    DetailInfo.append(radio(radios) + ' ' + text(texts))
    DetailInfo.append(radio(radios) + ' ' + text(texts))
    DetailInfo.append(check(checks))
    DetailInfo.append(radio(radios) + ' ' + text(texts))
    DetailInfo.append(radio(radios) + ' ' + text(texts))
    DetailInfo.append(text(texts))
    DetailInfo.append(text(texts))

    DetailInfo.append(text(texts))
    DetailInfo.append(text(texts))
    DetailInfo.append(radio(radios))
    DetailInfo.append(radio(radios) + ' ' + text(texts))
    DetailInfo.append(text(texts))

    DetailInfo.append(radio(radios) + ' ' + text(texts))
    DetailInfo.append(text(texts))
    DetailInfo.append(check(checks) + ' ' + text(texts))
    DetailInfo.append(text(texts))
    DetailInfo.append(text(texts))
    DetailInfo.append(text(texts))
    DetailInfo.append(text(texts))
    DetailInfo.append(text(texts))
    DetailInfo.append(text(texts))
    return DetailInfo


if __name__ == "__main__":
    start = time.clock()
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123456', db='spider_data', charset='utf8')
    cur = conn.cursor()
    dir = 'D:\爬虫数据-医疗\爬虫数据-医疗-王伟伟\www-爬虫数据\爬虫原始数据\重性精神疾病随访记录'
    allFiles = getAllFile(dirname=dir)
    count = 0
    first = True
    for allFile in allFiles:
        if count >= 0:
            soup = BeautifulSoup(open(dir + '\\' + allFile, encoding="utf-8"), "lxml")
            ths = soup.findAll('th')
            detail = []
            sql_create = 'CREATE TABLE 重性精神疾病随访记录 ( 档案编号 varchar(50),本人姓名 varchar(50),家庭电话 varchar(50),' \
                         '性别 varchar(50),出生日期 varchar(50),身份证号 varchar(50),联系人 varchar(50),' \
                         '本人联系电话 varchar(50),婚姻状况 varchar(50),现居住地 varchar(50),所属单位 varchar(50),建档单位 varchar(50),'
            for th in ths:
                output = ''
                th_next = th.next_sibling
                while not th_next.name:
                    th_next = th_next.next_sibling
                if th_next.find(attrs={"id": re.compile('ctl00_page_Content_.*_radioList1$')}):
                    radio = th_next.find(attrs={"id": re.compile('ctl00_page_Content_.*_radioList1$')})
                    if radio.find(attrs={"checked": "checked"}):
                        output += str(radio.find(attrs={"checked": "checked"}).next_sibling.string) + ' '
                    else:
                        output += 'None' + ' '
                if th_next.find(attrs={"id": re.compile('ctl00_page_Content_.*_ddl$')}):
                    option = th_next.find(attrs={"id": re.compile('ctl00_page_Content_.*_ddl$')})
                    if option.find(attrs={"selected": "selected"}):
                        output += str(option.find(attrs={"selected": "selected"}).get('value')) + ' '
                    else:
                        output += 'None' + ' '
                if th_next.find(attrs={"id": re.compile('ctl00_page_Content_.*_chkList1$')}):
                    checks = th_next.find(attrs={"id": re.compile('ctl00_page_Content_.*_chkList1$')})
                    if checks.findAll(attrs={"checked": "checked"}):
                        for check in checks.findAll(attrs={"checked": "checked"}):
                            output += check.next_sibling.string + ' '
                    else:
                        output += 'None' + ' '
                if th_next.findAll(name='input', attrs={"id": re.compile('ctl00_page_Content_.*_tb$')}):
                    inputs = th_next.findAll(name='input', attrs={"id": re.compile('ctl00_page_Content_.*_tb$')})
                    for input in inputs:
                        output += str(input.get('value')) + ' '
                if output:
                    text = th.text.replace(' ', '').replace('\n', '').replace('(','').replace(')','')
                    detail.append(output)
                    if first:
                        sql_create += text + ' varchar(255),'
            basic = getBasicInfo(soup)
            basic.extend(detail)
            if first:
                sql_create = sql_create[0:len(sql_create) - 1]
                sql_create += ')'
                cur.execute(sql_create)
                first = False
            data_insert('重性精神疾病随访记录', basic)
        print(count)
        count += 1
    cur.close()
    conn.close()
    print('总时间为:', time.clock() - start)
