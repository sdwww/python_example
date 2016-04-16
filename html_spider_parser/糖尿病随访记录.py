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


def getYongYao(soup):
    yongyao = radiobox(soup, "ctl00_page_Content_ywqkList_radioList1")
    yaopins = soup.findAll(attrs={"name": re.compile("ctl00_page_Content_ywqkList_LabelTextBox2_div_ltb3")})
    for yaopin in yaopins:
        if yaopin.get('value'):
            yongyao += ' ' + yaopin.get('value')
    yongliangs = soup.findAll(attrs={"name": re.compile("ctl00\$page_Content\$ywqkList\$LabelTextBox2_div")})
    for yongliang in yongliangs:
        if yongliang.get('value'):
            yongyao += ' ' + yongliang.get('value')
    meicis = soup.findAll(attrs={"id": re.compile("ctl00_page_Content_ywqkList_LabelTextBox2_2_div_ltb3")})
    for meici in meicis:
        if meici.get('value'):
            yongyao += ' ' + meici.get('value')
    return yongyao


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
    DetailInfo.append(radiobox(soup, "ctl00_page_Content_sffs_radioList1"))
    DetailInfo.append(checkbox(soup, "ctl00_page_Content_zz_chkList1")
                      + str(soup.find(attrs={"id": "ctl00_page_Content_zz_tb"}).get('value')))
    DetailInfo.append(str(soup.find(attrs={"id": "ctl00_page_Content_xy_ltb1_tb"}).get('value'))
                      + ' ' + str(soup.find(attrs={"id": "ctl00_page_Content_xy_ltb2_tb"}).get('value')))
    DetailInfo.append(str(soup.find(attrs={"id": "ctl00_page_Content_tz_ltb1_tb"}).get('value'))
                      + ' ' + str(soup.find(attrs={"id": "ctl00_page_Content_tz_ltb2_tb"}).get('value')))
    DetailInfo.append(str(soup.find(attrs={"id": "ctl00_page_Content_sg_tb"}).get('value')))
    DetailInfo.append(str(soup.find(attrs={"id": "ctl00_page_Content_tzzd_ltb1_tb"}).get('value'))
                      + ' ' + str(soup.find(attrs={"id": "ctl00_page_Content_tzzd_ltb2_tb"}).get('value')))
    DetailInfo.append(radiobox(soup, "ctl00_page_Content_zbdmbd_radioList1"))
    DetailInfo.append(str(soup.find(attrs={"id": "ctl00_page_Content_tzqt_tb"}).get('value')))
    DetailInfo.append(str(soup.find(attrs={"id": "ctl00_page_Content_rxyl_ltb1_tb"}).get('value'))
                      + ' ' + str(soup.find(attrs={"id": "ctl00_page_Content_rxyl_ltb2_tb"}).get('value')))
    DetailInfo.append(str(soup.find(attrs={"id": "ctl00_page_Content_ryjl_ltb1_tb"}).get('value'))
                      + ' ' + str(soup.find(attrs={"id": "ctl00_page_Content_ryjl_ltb2_tb"}).get('value')))
    DetailInfo.append(str(soup.find(attrs={"id": "ctl00_page_Content_ydq_ltb1_tb"}).get('value'))  # 运动
                      + ' ' + str(soup.find(attrs={"id": "ctl00_page_Content_ydq_ltb2_tb"}).get('value')))
    DetailInfo.append(str(soup.find(attrs={"id": "ctl00_page_Content_ydh_ltb1_tb"}).get('value'))
                      + ' ' + str(soup.find(attrs={"id": "ctl00_page_Content_ydh_ltb2_tb"}).get('value')))
    DetailInfo.append(str(soup.find(attrs={"id": "ctl00_page_Content_zhushi_ltb1_tb"}).get('value'))
                      + ' ' + str(soup.find(attrs={"id": "ctl00_page_Content_zhushi_ltb2_tb"}).get('value')))
    DetailInfo.append(radiobox(soup, "ctl00_page_Content_xltz_radioList1"))
    DetailInfo.append(radiobox(soup, "ctl00_page_Content_zyxw_radioList1"))
    DetailInfo.append(str(soup.find(attrs={"name": "ctl00$page_Content$kfxt$tb"}).get('value')))
    DetailInfo.append(str(soup.find(attrs={"id": "ctl00_page_Content_thxhdb_tb"}).get('value')))
    DetailInfo.append(str(soup.find(attrs={"id": "ctl00_page_Content_qtjc_tb"}).get('value')))
    DetailInfo.append(str(soup.find(attrs={"id": "ctl00_page_Content_jcrq_tb"}).get('value')))
    DetailInfo.append(radiobox(soup, "ctl00_page_Content_fyycx_radioList1"))
    DetailInfo.append(radiobox(soup, "ctl00_page_Content_ywblfy_radioList1")
                      + ' ' + str(soup.find(attrs={"id": "ctl00_page_Content_ywblfy_tb"}).get('value')))
    DetailInfo.append(radiobox(soup, "ctl00_page_Content_dxtfy_radioList1"))
    DetailInfo.append(radiobox(soup, "ctl00_page_Content_sffl_radioList1"))
    DetailInfo.append(str(soup.find(attrs={"id": "ctl00_page_Content_yds_tb"}).get('value')))
    DetailInfo.append(getYongYao(soup))
    DetailInfo.append(str(soup.find(attrs={"id": "ctl00_page_Content_zzyy_tb"}).get('value')))
    DetailInfo.append(option(soup, "ctl00_page_Content_zzkb_ddl"))
    DetailInfo.append(str(soup.find(attrs={"id": "ctl00_page_Content_xcsfrq_tb"}).get('value')))
    DetailInfo.append(str(soup.find(attrs={"id": "ctl00_page_Content_sfys_tb"}).get('value')))
    DetailInfo.append(str(soup.find(attrs={"id": "ctl00_page_Content_jldarq_tb"}).get('value')))
    DetailInfo.append(str(soup.find(attrs={"id": "ctl00_page_Content_jdr_ltb1_tb"}).get('value')))
    DetailInfo.append(str(soup.find(attrs={"id": "ctl00_page_Content_jdr_ltb2_tb"}).get('value')))
    return DetailInfo


if __name__ == "__main__":
    start = time.clock()
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123456', db='spider_data', charset='utf8')
    cur = conn.cursor()
    dir = 'D:\爬虫数据-医疗\爬虫数据-医疗-王伟伟\www-爬虫数据\爬虫原始数据\糖尿病随访记录'
    allFiles = getAllFile(dirname=dir)
    count = 0
    for allFile in allFiles:
        if count >= 0:
            soup = BeautifulSoup(open(dir + '\\' + allFile, encoding="utf-8"), "lxml")
            basic = getBasicInfo(soup)
            detail = getDetailInfo(soup)
            basic.extend(detail)
            data_insert('糖尿病随访记录', basic)
            print(count)
        count += 1
    cur.close()
    conn.close()
    print('总时间为:', time.clock() - start)
