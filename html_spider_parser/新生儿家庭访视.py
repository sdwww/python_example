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
    DetailInfo.append(str(soup.find(attrs={"id": "ctl00_page_Content_fqname_tb"}).get('value')))
    DetailInfo.append(option(soup, "ctl00_page_Content_fqzy_ddl"))
    DetailInfo.append(str(soup.find(attrs={"id": "ctl00_page_Content_fqcsrq_tb"}).get('value')))
    DetailInfo.append(str(soup.find(attrs={"id": "ctl00_page_Content_fqlxdh_tb"}).get('value')))
    DetailInfo.append(str(soup.find(attrs={"id": "ctl00_page_Content_mqname_tb"}).get('value')))
    DetailInfo.append(option(soup, "ctl00_page_Content_mqzy_ddl"))
    DetailInfo.append(str(soup.find(attrs={"id": "ctl00_page_Content_mqcsrq_tb"}).get('value')))
    DetailInfo.append(str(soup.find(attrs={"id": "ctl00_page_Content_mqlxdh_tb"}).get('value')))
    DetailInfo.append(str(soup.find(attrs={"id": "ctl00_page_Content_csyz_tb"}).get('value')))
    DetailInfo.append(radiobox(soup, "ctl00_page_Content_jbqk_radioList1")
                      + ' ' + str(soup.find(attrs={"id": "ctl00_page_Content_jbqk_tb"}).get('value')))
    DetailInfo.append(str(soup.find(attrs={"id": "ctl00_page_Content_jcjg_tb"}).get('value')))
    DetailInfo.append(checkbox(soup, "ctl00_page_Content_csqk_chkList1")
                      + str(soup.find(attrs={"id": "ctl00_page_Content_csqk_tb"}).get('value')))
    DetailInfo.append(radiobox(soup, "ctl00_page_Content_xsezx_radioList1")+' '
                      +radiobox(soup, "ctl00_page_Content_zjApgar_radioList1"))
    DetailInfo.append(radiobox(soup, "ctl00_page_Content_sfjx_radioList1")
                      + ' ' + str(soup.find(attrs={"id": "ctl00_page_Content_sfjx_tb"}).get('value')))
    DetailInfo.append(radiobox(soup, "ctl00_page_Content_tlsc_radioList1"))
    DetailInfo.append(checkbox(soup, "ctl00_page_Content_jbscdx_chkList1")
                      + str(soup.find(attrs={"id": "ctl00_page_Content_jbscdx_tb"}).get('value')))
    DetailInfo.append(str(soup.find(attrs={"id": "ctl00_page_Content_cstz_tb"}).get('value')))
    DetailInfo.append(str(soup.find(attrs={"id": "ctl00_page_Content_mqtz_tb"}).get('value')))
    DetailInfo.append(str(soup.find(attrs={"id": "ctl00_page_Content_cssc_tb"}).get('value')))
    DetailInfo.append(radiobox(soup, "ctl00_page_Content_wyfs_radioList1"))
    DetailInfo.append(str(soup.find(attrs={"id": "ctl00_page_Content_cnl_tb"}).get('value')))
    DetailInfo.append(str(soup.find(attrs={"id": "ctl00_page_Content_cncs_tb"}).get('value')))
    DetailInfo.append(radiobox(soup, "ctl00_page_Content_ot_radioList1"))
    DetailInfo.append(radiobox(soup, "ctl00_page_Content_db_radioList1"))
    DetailInfo.append(str(soup.find(attrs={"id": "ctl00_page_Content_dbcs_tb"}).get('value')))
    DetailInfo.append(str(soup.find(attrs={"id": "ctl00_page_Content_tiwen_tb"}).get('value')))
    DetailInfo.append(str(soup.find(attrs={"id": "ctl00_page_Content_maibo_tb"}).get('value')))
    DetailInfo.append(str(soup.find(attrs={"id": "ctl00_page_Content_hxpl_tb"}).get('value')))
    DetailInfo.append(checkbox(soup, "ctl00_page_Content_mianse_chkList1")
                      + str(soup.find(attrs={"id": "ctl00_page_Content_mianse_tb"}).get('value')))
    DetailInfo.append(checkbox(soup, "ctl00_page_Content_hdbw_chkList1"))
    DetailInfo.append(str(soup.find(attrs={"id": "ctl00_page_Content_qx_ltb1_tb"}).get('value'))+' '+
                      str(soup.find(attrs={"id": "ctl00_page_Content_qx_ltb2_tb"}).get('value'))+' '+
                      radiobox(soup, "ctl00_page_Content_qxqk_radioList1")+' '
                      + str(soup.find(attrs={"id": "ctl00_page_Content_qxqk_tb"}).get('value')))
    DetailInfo.append(radiobox(soup, "ctl00_page_Content_yan_radioList1")
                      + ' ' + str(soup.find(attrs={"id": "ctl00_page_Content_yan_tb"}).get('value')))
    DetailInfo.append(radiobox(soup, "ctl00_page_Content_szhdd_radioList1")
                      + ' ' + str(soup.find(attrs={"id": "ctl00_page_Content_szhdd_tb"}).get('value')))
    DetailInfo.append(radiobox(soup, "ctl00_page_Content_er_radioList1")
                      + ' ' + str(soup.find(attrs={"id": "ctl00_page_Content_er_tb"}).get('value')))
    DetailInfo.append(radiobox(soup, "ctl00_page_Content_jbbk_radioList1")
                      + ' ' + str(soup.find(attrs={"id": "ctl00_page_Content_jbbk_tb"}).get('value')))
    DetailInfo.append(radiobox(soup, "ctl00_page_Content_bi_radioList1")
                      + ' ' + str(soup.find(attrs={"id": "ctl00_page_Content_bi_tb"}).get('value')))
    DetailInfo.append(checkbox(soup, "ctl00_page_Content_pf_chkList1")
                      + ' ' + str(soup.find(attrs={"id": "ctl00_page_Content_pf_tb"}).get('value')))
    DetailInfo.append(radiobox(soup, "ctl00_page_Content_kq_radioList1")
                      + ' ' + str(soup.find(attrs={"id": "ctl00_page_Content_kq_tb"}).get('value')))
    DetailInfo.append(radiobox(soup, "ctl00_page_Content_gm_radioList1")
                      + ' ' + str(soup.find(attrs={"id": "ctl00_page_Content_gm_tb"}).get('value')))
    DetailInfo.append(radiobox(soup, "ctl00_page_Content_xf_radioList1")
                      + ' ' + str(soup.find(attrs={"id": "ctl00_page_Content_xf_tb"}).get('value')))
    DetailInfo.append(radiobox(soup, "ctl00_page_Content_wszq_radioList1")
                      + ' ' + str(soup.find(attrs={"id": "ctl00_page_Content_wszq_tb"}).get('value')))
    DetailInfo.append(radiobox(soup, "ctl00_page_Content_fb_radioList1")
                      + ' ' + str(soup.find(attrs={"id": "ctl00_page_Content_fb_tb"}).get('value')))
    DetailInfo.append(radiobox(soup, "ctl00_page_Content_jz_radioList1")
                      + ' ' + str(soup.find(attrs={"id": "ctl00_page_Content_jz_tb"}).get('value')))
    DetailInfo.append(radiobox(soup, "ctl00_page_Content_qd_radioList1")
                      + ' ' + str(soup.find(attrs={"id": "ctl00_page_Content_qd_tb"}).get('value')))
    DetailInfo.append(radiobox(soup, "ctl00_page_Content_zhuanzhen_radioList1")
                      + ' ' + str(soup.find(attrs={"id": "ctl00_page_Content_zhuanzhen_tb"}).get('value')))
    DetailInfo.append(str(soup.find(attrs={"id": "ctl00_page_Content_zzjg_tb"}).get('value')))
    DetailInfo.append(checkbox(soup, "ctl00_page_Content_zhidao_chkList1")
                      + ' ' + str(soup.find(attrs={"id": "ctl00_page_Content_zhidao_tb"}).get('value')))

    DetailInfo.append(str(soup.find(attrs={"name": "ctl00$page_Content$sfrq$tb"}).get('value')))
    DetailInfo.append(str(soup.find(attrs={"id": "ctl00_page_Content_xcsfdd_tb"}).get('value')))
    DetailInfo.append(str(soup.find(attrs={"id": "ctl00_page_Content_xcsfrq_tb"}).get('value')))
    DetailInfo.append(str(soup.find(attrs={"id": "ctl00_page_Content_sfys_tb"}).get('value')))
    DetailInfo.append(str(soup.find(attrs={"id": "ctl00_page_Content_czsj_tb"}).get('value')))
    DetailInfo.append(str(soup.find(attrs={"id": "ctl00_page_Content_czy_ltb1_tb"}).get('value')))
    DetailInfo.append(str(soup.find(attrs={"id": "ctl00_page_Content_czy_ltb2_tb"}).get('value')))
    DetailInfo.append(str(soup.find(attrs={"id": "ctl00_page_Content_updatetime_tb"}).get('value')))
    DetailInfo.append(str(soup.find(attrs={"id": "ctl00_page_Content_updateID_tb"}).get('value')))
    return DetailInfo


if __name__ == "__main__":
    start = time.clock()
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123456', db='spider_data', charset='utf8')
    cur = conn.cursor()
    dir = 'D:\爬虫数据-医疗\爬虫数据-医疗-王伟伟\www-爬虫数据\爬虫原始数据\新生儿家庭访视'
    allFiles = getAllFile(dirname=dir)
    count = 0
    for allFile in allFiles:
        if count >=0:
            soup = BeautifulSoup(open(dir + '\\' + allFile, encoding="utf-8"), "lxml")
            basic = getBasicInfo(soup)
            detail = getDetailInfo(soup)
            basic.extend(detail)
            data_insert('新生儿家庭访视', basic)
        print(count)
        count += 1
    cur.close()
    conn.close()
    print('总时间为:', time.clock() - start)
