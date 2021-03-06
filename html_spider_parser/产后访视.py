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
    sql = "INSERT INTO " + database + " VALUES('"
    for v in range(0, len(values) - 1):
        sql += values[v] + "','"
    sql += values[len(values) - 1] + "')"
    cur.execute(sql)
    conn.commit()


def checkbox(soup, id_content):
    values = soup.find(attrs={"id": id_content}).findAll(attrs={"checked": "checked"})
    v = ''
    for i in values:
        v += str(i.next_sibling.string) + ' '
    if not v:
        v = 'None'
    return v


def radiobox(soup, id_content):
    try:
        values = str(soup.find(attrs={"id": id_content}).find(attrs={"checked": "checked"}).next_sibling.string)
    except:
        values = 'None'
    return values


def option(soup, id_content):
    try:
        values = str(soup.find(attrs={"id": id_content}).find(attrs={"selected": "selected"}).string)
    except:
        values = 'None'
    return values


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
    DetailInfo.append(str(soup.find(attrs={"id": "ctl00_page_Content_sfrq_tb"}).get('value')))
    DetailInfo.append(str(soup.find(attrs={"id": "ctl00_page_Content_tiwen_tb"}).get('value')))
    DetailInfo.append(str(soup.find(attrs={"id": "ctl00_page_Content_fmsj_tb"}).get('value')))
    DetailInfo.append(str(soup.find(attrs={"id": "ctl00_page_Content_xy_ltb1_tb"}).get('value'))+' '
                      +str(soup.find(attrs={"id": "ctl00_page_Content_xy_ltb2_tb"}).get('value')))
    DetailInfo.append(str(soup.find(attrs={"id": "ctl00_page_Content_ybjkzk_tb"}).get('value')))
    DetailInfo.append(str(soup.find(attrs={"id": "ctl00_page_Content_ybxlzk_tb"}).get('value')))
    DetailInfo.append(radiobox(soup, "ctl00_page_Content_rufang_radioList1")
                      + ' ' + str(soup.find(attrs={"id": "ctl00_page_Content_rufang_tb"}).get('value')))
    DetailInfo.append(radiobox(soup, "ctl00_page_Content_elu_radioList1")
                      + ' ' + str(soup.find(attrs={"id": "ctl00_page_Content_elu_tb"}).get('value')))
    DetailInfo.append(radiobox(soup, "ctl00_page_Content_zigong_radioList1")
                      + ' ' + str(soup.find(attrs={"id": "ctl00_page_Content_zigong_tb"}).get('value')))
    DetailInfo.append(radiobox(soup, "ctl00_page_Content_shangkou_radioList1")
                      + ' ' + str(soup.find(attrs={"id": "ctl00_page_Content_shangkou_tb"}).get('value')))
    DetailInfo.append(str(soup.find(attrs={"id": "ctl00_page_Content_qita_tb"}).get('value')))
    DetailInfo.append(radiobox(soup, "ctl00_page_Content_fenlei_radioList1")
                      + ' ' + str(soup.find(attrs={"id": "ctl00_page_Content_fenlei_tb"}).get('value')))
    DetailInfo.append(radiobox(soup, "ctl00_page_Content_zhuanzhen_radioList1")
                      + ' ' + str(soup.find(attrs={"id": "ctl00_page_Content_zhuanzhen_tb"}).get('value')))
    DetailInfo.append(radiobox(soup, "ctl00_page_Content_chuli_radioList1")
                      + ' ' + str(soup.find(attrs={"id": "ctl00_page_Content_chuli_tb"}).get('value')))
    DetailInfo.append(str(soup.find(attrs={"id": "ctl00_page_Content_zzjg_tb"}).get('value')))
    DetailInfo.append(checkbox(soup, "ctl00_page_Content_zhidao_chkList1")
                      + str(soup.find(attrs={"id": "ctl00_page_Content_zhidao_tb"}).get('value')))
    DetailInfo.append(str(soup.find(attrs={"id": "ctl00_page_Content_sfys_tb"}).get('value')))
    DetailInfo.append(str(soup.find(attrs={"id": "ctl00_page_Content_czsj_tb"}).get('value')))
    DetailInfo.append(str(soup.find(attrs={"id": "ctl00_page_Content_czy_ltb1_tb"}).get('value')))
    DetailInfo.append(str(soup.find(attrs={"id": "ctl00_page_Content_czy_ltb2_tb"}).get('value')))
    return DetailInfo


if __name__ == "__main__":
    start = time.clock()
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123456', db='spider_data', charset='utf8')
    cur = conn.cursor()
    dir = 'D:\爬虫数据-医疗\爬虫数据-医疗-王伟伟\www-爬虫数据\爬虫原始数据\产后访视'
    allFiles = getAllFile(dirname=dir)
    count = 0
    for allFile in allFiles:
        if count >= 0:
            soup = BeautifulSoup(open(dir + '\\' + allFile, encoding="utf-8"), "lxml")
            basic = getBasicInfo(soup)
            detail = getDetailInfo(soup)
            basic.extend(detail)
            data_insert('产后访视', basic)
            print(count)
        count += 1
    cur.close()
    conn.close()
    print('总时间为:', time.clock() - start)
