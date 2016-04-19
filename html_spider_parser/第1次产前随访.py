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
    DetailInfo.append(str(soup.find(attrs={"id": "ctl00_page_Content_tbrq_tb"}).get('value')))
    DetailInfo.append(str(soup.find(attrs={"id": "ctl00_page_Content_tbyz_tb"}).get('value')))
    DetailInfo.append(str(soup.find(attrs={"id": "ctl00_page_Content_yfnl_tb"}).get('value')))
    DetailInfo.append(str(soup.find(attrs={"id": "ctl00_page_Content_zf_ltb1_tb"}).get('value')))
    DetailInfo.append(str(soup.find(attrs={"id": "ctl00_page_Content_zf_ltb2_tb"}).get('value')))
    DetailInfo.append(str(soup.find(attrs={"id": "ctl00_page_Content_zfnl_tb"}).get('value')))
    DetailInfo.append(str(soup.find(attrs={"id": "ctl00_page_Content_yunci_tb"}).get('value')))
    DetailInfo.append(str(soup.find(attrs={"id": "ctl00_page_Content_chanci_ltb1_tb"}).get('value')))
    DetailInfo.append(str(soup.find(attrs={"id": "ctl00_page_Content_chanci_ltb2_tb"}).get('value')))
    DetailInfo.append(radiobox(soup, "ctl00_page_Content_mcyj_radioList1")
                      + ' ' + str(soup.find(attrs={"id": "ctl00_page_Content_mcyj_tb"}).get('value')))
    DetailInfo.append(str(soup.find(attrs={"id": "ctl00_page_Content_ycq_tb"}).get('value')))
    DetailInfo.append(checkbox(soup, "ctl00_page_Content_jws_chkList1")
                      + str(soup.find(attrs={"id": "ctl00_page_Content_jws_tb"}).get('value')))
    DetailInfo.append(checkbox(soup, "ctl00_page_Content_jzs_chkList1")
                      + str(soup.find(attrs={"id": "ctl00_page_Content_jzs_tb"}).get('value')))
    DetailInfo.append(checkbox(soup, "ctl00_page_Content_grs_chkList1")
                      + str(soup.find(attrs={"id": "ctl00_page_Content_grs_tb"}).get('value')))
    DetailInfo.append(radiobox(soup, "ctl00_page_Content_fksss_radioList1")
                      + ' ' + str(soup.find(attrs={"id": "ctl00_page_Content_fksss_tb"}).get('value')))
    DetailInfo.append(str(soup.find(attrs={"id": "ctl00_page_Content_liuchan_tb"}).get('value')) + ' '
                      + str(soup.find(attrs={"id": "ctl00_page_Content_sitai_tb"}).get('value')) + ' '
                      + str(soup.find(attrs={"id": "ctl00_page_Content_sichan_tb"}).get('value')) + ' '
                      + str(soup.find(attrs={"id": "ctl00_page_Content_xsesw_tb"}).get('value')) + ' '
                      + str(soup.find(attrs={"id": "ctl00_page_Content_csqxe_tb"}).get('value')))
    DetailInfo.append(str(soup.find(attrs={"id": "ctl00_page_Content_shengao_tb"}).get('value')))
    DetailInfo.append(str(soup.find(attrs={"id": "ctl00_page_Content_tizhong_tb"}).get('value')))
    DetailInfo.append(str(soup.find(attrs={"id": "ctl00_page_Content_BMI_tb"}).get('value')))
    DetailInfo.append(str(soup.find(attrs={"id": "ctl00_page_Content_xy_ltb1_tb"}).get('value'))+'/'+
                      str(soup.find(attrs={"id": "ctl00_page_Content_xy_ltb2_tb"}).get('value')))
    DetailInfo.append(radiobox(soup, "ctl00_page_Content_xinzang_radioList1")
                      + ' ' + str(soup.find(attrs={"id": "ctl00_page_Content_xinzang_tb"}).get('value')))
    DetailInfo.append(radiobox(soup, "ctl00_page_Content_feibu_radioList1")
                      + ' ' + str(soup.find(attrs={"id": "ctl00_page_Content_feibu_tb"}).get('value')))
    DetailInfo.append(radiobox(soup, "ctl00_page_Content_waiyin_radioList1")
                      + ' ' + str(soup.find(attrs={"id": "ctl00_page_Content_waiyin_tb"}).get('value')))
    DetailInfo.append(radiobox(soup, "ctl00_page_Content_yindao_radioList1")
                      + ' ' + str(soup.find(attrs={"id": "ctl00_page_Content_yindao_tb"}).get('value')))
    DetailInfo.append(radiobox(soup, "ctl00_page_Content_gongji_radioList1")
                      + ' ' + str(soup.find(attrs={"id": "ctl00_page_Content_gongji_tb"}).get('value')))
    DetailInfo.append(radiobox(soup, "ctl00_page_Content_zigong_radioList1")
                      + ' ' + str(soup.find(attrs={"id": "ctl00_page_Content_zigong_tb"}).get('value')))
    DetailInfo.append(radiobox(soup, "ctl00_page_Content_fujian_radioList1")
                      + ' ' + str(soup.find(attrs={"id": "ctl00_page_Content_fujian_tb"}).get('value')))
    DetailInfo.append(str(soup.find(attrs={"id": "ctl00_page_Content_xhdb_tb"}).get('value')))#血常规
    DetailInfo.append(str(soup.find(attrs={"id": "ctl00_page_Content_bxb_tb"}).get('value')))
    DetailInfo.append(str(soup.find(attrs={"id": "ctl00_page_Content_xxb_tb"}).get('value')))
    DetailInfo.append(str(soup.find(attrs={"id": "ctl00_page_Content_xcgqt_tb"}).get('value')))
    DetailInfo.append(str(soup.find(attrs={"id": "ctl00_page_Content_ndb_tb"}).get('value')))#尿常规
    DetailInfo.append(str(soup.find(attrs={"id": "ctl00_page_Content_niaotang_tb"}).get('value')))
    DetailInfo.append(str(soup.find(attrs={"id": "ctl00_page_Content_ntt_tb"}).get('value')))
    DetailInfo.append(str(soup.find(attrs={"id": "ctl00_page_Content_nqx_tb"}).get('value')))
    DetailInfo.append(str(soup.find(attrs={"id": "ctl00_page_Content_ncgqt_tb"}).get('value')))
    DetailInfo.append(str(soup.find(attrs={"id": "ctl00_page_Content_xuexiABO_tb"}).get('value')))
    DetailInfo.append(str(soup.find(attrs={"id": "ctl00_page_Content_xuexiRh_tb"}).get('value')))
    DetailInfo.append(str(soup.find(attrs={"id": "ctl00_page_Content_xt_tb"}).get('value')))
    DetailInfo.append(str(soup.find(attrs={"id": "ctl00_page_Content_xqgbzam_tb"}).get('value'))) #肝功能
    DetailInfo.append(str(soup.find(attrs={"id": "ctl00_page_Content_xqgczam_tb"}).get('value')))
    DetailInfo.append(str(soup.find(attrs={"id": "ctl00_page_Content_bdb_tb"}).get('value')))
    DetailInfo.append(str(soup.find(attrs={"id": "ctl00_page_Content_zdhs_tb"}).get('value')))
    DetailInfo.append(str(soup.find(attrs={"id": "ctl00_page_Content_jhdhs_tb"}).get('value')))
    DetailInfo.append(str(soup.find(attrs={"id": "ctl00_page_Content_xqjg_tb"}).get('value')))
    DetailInfo.append(str(soup.find(attrs={"id": "ctl00_page_Content_xnsd_tb"}).get('value')))
    DetailInfo.append(checkbox(soup, "ctl00_page_Content_ydfmw_chkList1")
                      + str(soup.find(attrs={"id": "ctl00_page_Content_ydfmw_tb"}).get('value')))
    DetailInfo.append(radiobox(soup, "ctl00_page_Content_ydqjd_radioList1"))
    DetailInfo.append(str(soup.find(attrs={"id": "ctl00_page_Content_yxgybmky_tb"}).get('value')))
    DetailInfo.append(str(soup.find(attrs={"id": "ctl00_page_Content_yxgybmkt_tb"}).get('value')))
    DetailInfo.append(str(soup.find(attrs={"id": "ctl00_page_Content_yxgyEky_tb"}).get('value')))
    DetailInfo.append(str(soup.find(attrs={"id": "ctl00_page_Content_yxgyEke_tb"}).get('value')))
    DetailInfo.append(str(soup.find(attrs={"id": "ctl00_page_Content_yxgykxkt_tb"}).get('value')))
    DetailInfo.append(radiobox(soup, "ctl00_page_Content_mdxqxsy_radioList1"))
    DetailInfo.append(radiobox(soup, "ctl00_page_Content_HIV_radioList1"))
    DetailInfo.append(str(soup.find(attrs={"id": "ctl00_page_Content_Bchao_tb"}).get('value')))
    DetailInfo.append(radiobox(soup, "ctl00_page_Content_ztpg_radioList1")
                      + ' ' + str(soup.find(attrs={"id": "ctl00_page_Content_ztpg_tb"}).get('value')))
    DetailInfo.append(checkbox(soup, "ctl00_page_Content_byzd_chkList1")
                      + str(soup.find(attrs={"id": "ctl00_page_Content_byzd_tb"}).get('value')))
    DetailInfo.append(radiobox(soup, "ctl00_page_Content_zhuanzhen_radioList1")
                      + ' ' + str(soup.find(attrs={"id": "ctl00_page_Content_zhuanzhen_tb"}).get('value')))
    DetailInfo.append(str(soup.find(attrs={"id": "ctl00_page_Content_zzjg_tb"}).get('value')))
    DetailInfo.append(str(soup.find(attrs={"id": "ctl00_page_Content_xcsfrq_tb"}).get('value')))
    DetailInfo.append(str(soup.find(attrs={"id": "ctl00_page_Content_sfys_tb"}).get('value')))
    DetailInfo.append(radiobox(soup, "ctl00_page_Content_brsfzxjzd_radioList1"))
    DetailInfo.append(str(soup.find(attrs={"id": "ctl00_page_Content_czsj_tb"}).get('value')))
    DetailInfo.append(str(soup.find(attrs={"id": "ctl00_page_Content_czy_ltb1_tb"}).get('value')))
    DetailInfo.append(str(soup.find(attrs={"id": "ctl00_page_Content_czy_ltb2_tb"}).get('value')))
    return DetailInfo


if __name__ == "__main__":
    start = time.clock()
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123456', db='spider_data', charset='utf8')
    cur = conn.cursor()
    dir = 'D:\爬虫数据-医疗\爬虫数据-医疗-王伟伟\www-爬虫数据\爬虫原始数据\第1次产前随访'
    allFiles = getAllFile(dirname=dir)
    count = 0
    for allFile in allFiles:
        if count >= 0:
            soup = BeautifulSoup(open(dir + '\\' + allFile, encoding="utf-8"), "lxml")
            basic = getBasicInfo(soup)
            detail = getDetailInfo(soup)
            basic.extend(detail)
            data_insert('第1次产前随访', basic)
            print(count)
        count += 1
    cur.close()
    conn.close()
    print('总时间为:', time.clock() - start)
