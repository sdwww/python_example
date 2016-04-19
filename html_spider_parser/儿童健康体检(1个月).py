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
    print(sql)
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
    DetailInfo.append(str(soup.find(attrs={"id": "ctl00_page_Content_tizhong_tb"}).get('value')) + ' '
                      + radiobox(soup, "ctl00_page_Content_tzfl_radioList1"))
    DetailInfo.append(str(soup.find(attrs={"id": "ctl00_page_Content_shenchang_tb"}).get('value')) + ' '
                      + radiobox(soup, "ctl00_page_Content_scfl_radioList1"))
    DetailInfo.append(str(soup.find(attrs={"id": "ctl00_page_Content_tw_tb"}).get('value')))
    DetailInfo.append(radiobox(soup, "ctl00_page_Content_mianse_chkList1")
                      + ' ' + str(soup.find(attrs={"id": "ctl00_page_Content_mianse_tb"}).get('value')))
    DetailInfo.append(radiobox(soup, "ctl00_page_Content_pifu_radioList1")
                      + ' ' + str(soup.find(attrs={"id": "ctl00_page_Content_pifu_tb"}).get('value')))
    DetailInfo.append(radiobox(soup, "ctl00_page_Content_qianxin_radioList1")
                      + ' ' + str(soup.find(attrs={"id": "ctl00_page_Content_qianxinchicun_ltb1_tb"}).get('value'))
                      + '*' + str(soup.find(attrs={"id": "ctl00_page_Content_qianxinchicun_ltb2_tb"}).get('value')))
    DetailInfo.append(radiobox(soup, "ctl00_page_Content_sz_radioList1")
                      + ' ' + str(soup.find(attrs={"id": "ctl00_page_Content_sz_tb"}).get('value')))
    DetailInfo.append(radiobox(soup, "ctl00_page_Content_yan_radioList1")
                      + ' ' + str(soup.find(attrs={"id": "ctl00_page_Content_yan_tb"}).get('value')))
    DetailInfo.append(radiobox(soup, "ctl00_page_Content_er_radioList1")
                      + ' ' + str(soup.find(attrs={"id": "ctl00_page_Content_er_tb"}).get('value')))
    DetailInfo.append(radiobox(soup, "ctl00_page_Content_gm_radioList1")
                      + ' ' + str(soup.find(attrs={"id": "ctl00_page_Content_gm_tb"}).get('value')))
    DetailInfo.append(str(texts[11].get('value')))
    DetailInfo.append(radiobox(soup, "ctl00_page_Content_xf_radioList1")
                      + ' ' + str(texts[12].get('value')))
    DetailInfo.append(radiobox(soup, "ctl00_page_Content_fb_radioList1")
                      + ' ' + str(texts[13].get('value')))
    DetailInfo.append(radiobox(soup, "ctl00_page_Content_jbbk_radioList1")
                      + ' ' + str(texts[14].get('value')))
    DetailInfo.append(radiobox(soup, "ctl00_page_Content_qb_radioList1")
                      + ' ' + str(texts[15].get('value')))
    DetailInfo.append(checkbox(soup, "ctl00_page_Content_glbtz_chkList1"))
    DetailInfo.append(radiobox(soup, "ctl00_page_Content_kq_radioList1")
                      + ' ' + str(texts[16].get('value')))
    DetailInfo.append(str(texts[20].get('value')))
    DetailInfo.append(str(texts[21].get('value')))
    DetailInfo.append(radiobox(soup, "ctl00_page_Content_fypg_radioList1"))
    DetailInfo.append(radiobox(soup, "ctl00_page_Content_hbqk_radioList1")
                      + ' ' + str(texts[22].get('value')))
    DetailInfo.append(str(texts[23].get('value')))
    DetailInfo.append(radiobox(soup, "ctl00_page_Content_zhuanzhen_radioList1")
                      + ' ' + str(texts[24].get('value')))
    DetailInfo.append(str(texts[25].get('value')))
    DetailInfo.append(checkbox(soup, "ctl00_page_Content_zhidao_chkList1") + ' '
                      + str(texts[26].get('value')))
    DetailInfo.append(str(texts[27].get('value')))
    DetailInfo.append(str(texts[28].get('value')))
    DetailInfo.append(str(texts[29].get('value')))
    DetailInfo.append(str(texts[30].get('value')))
    DetailInfo.append(str(texts[31].get('value')))
    DetailInfo.append(str(texts[32].get('value')))
    return DetailInfo


if __name__ == "__main__":
    start = time.clock()
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123456', db='spider_data', charset='utf8')
    cur = conn.cursor()
    dir = 'D:\爬虫数据-医疗\爬虫数据-医疗-王伟伟\www-爬虫数据\爬虫原始数据\儿童健康体检(1个月)'
    allFiles = getAllFile(dirname=dir)
    count = 0
    for allFile in allFiles:
        if count >= 0:
            soup = BeautifulSoup(open(dir + '\\' + allFile, encoding="utf-8"), "lxml")
            basic = getBasicInfo(soup)
            detail = getDetailInfo(soup)
            basic.extend(detail)
            data_insert('儿童健康体检_1个月', basic)
        print(count)
        count += 1
    cur.close()
    conn.close()
    print('总时间为:', time.clock() - start)
