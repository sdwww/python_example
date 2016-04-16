from bs4 import BeautifulSoup
import time
import os
import pymysql


def getAllFile(dirname):
    all_file = []
    for dirpath, dirnames, filenames in os.walk(dirname):
        for filename in filenames:
            all_file.append(filename)
    return all_file


start = time.clock()
conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123456', db='spider_data', charset='utf8')
dir = 'D:\爬虫数据-医疗\爬虫数据-医疗-王伟伟\www-爬虫数据\爬虫原始数据\个人健康档案'
allFiles = getAllFile(dirname=dir)
count = 0
for allFile in allFiles:
    count += 1
    soup = BeautifulSoup(open(dir + '\\' + allFile, encoding="utf-8"), "lxml")
    v0 = str(soup.find(attrs={"name": "ctl00$page_Content$grdabh$tb"})['value'])
    v1 = str(soup.find(attrs={"name": "ctl00$page_Content$ryxm$tb"})['value'])
    v2 = str(soup.find(attrs={"name": "ctl00$page_Content$sfzh$tb"})['value'])
    v3 = str(soup.find(attrs={"name": "ctl00$page_Content$xingbie$ddl"}).find(attrs={"selected": "selected"}).string)
    v4 = str(soup.find(attrs={"name": "ctl00$page_Content$csrq$tb"})['value'])
    try:
        v5 = str(soup.find(attrs={"name": "ctl00$page_Content$jtdh$tb"})['value'])
    except:
        v5 = ''
    try:
        v6 = str(soup.find(attrs={"name": "ctl00$page_Content$lxr$tb"})['value'])
    except:
        v6 = ''
    try:
        v7 = str(soup.find(attrs={"name": "ctl00$page_Content$lxrdh$tb"})['value'])
    except:
        v7 = ''
    v8 = str(soup.find(attrs={"name": "ctl00$page_Content$hyzk$ddl"}).find(attrs={"selected": "selected"}).string)
    v9 = str(soup.find(attrs={"name": "ctl00$page_Content$dazt$ddl"}).find(attrs={"selected": "selected"}).string)
    try:
        v10 = str(soup.find(attrs={"name": "ctl00$page_Content$ssdwName$tb"})['value'])
    except:
        v10 = ''
    try:
        v11 = str(soup.find(attrs={"name": "ctl00$page_Content$jddwName$tb"})['value'])
    except:
        v11 = ''
    try:
        v12 = str(soup.find(attrs={"name": "ctl00$page_Content$jtbm$tb"})['value'])
    except:
        v12 = ''
    try:
        v13 = str(soup.find(attrs={"name": "ctl00$page_Content$gzdw$tb"})['value'])
    except:
        v13 = ''
    v14 = str(soup.find(attrs={"name": "ctl00$page_Content$czlx$ddl"}).find(attrs={"selected": "selected"}).string)
    v15 = str(soup.find(attrs={"name": "ctl00$page_Content$zhiye$ddl"}).find(attrs={"selected": "selected"}).string)
    v16 = str(soup.find(attrs={"name": "ctl00$page_Content$minzu$ddl"}).find(attrs={"selected": "selected"}).string)
    v17 = str(soup.find(attrs={"name": "ctl00$page_Content$xuexing$ddl"}).find(attrs={"selected": "selected"}).string)
    v18 = str(soup.find(attrs={"name": "ctl00$page_Content$sfRH$ddl"}).find(attrs={"selected": "selected"}).string)
    v19 = str(soup.find(attrs={"name": "ctl00$page_Content$whcd$ddl"}).find(attrs={"selected": "selected"}).string)
    v20 = str(soup.find(attrs={"name": "ctl00$page_Content$XZQH$sheng"}).find(attrs={"selected": "selected"}).string)
    v21 = str(soup.find(attrs={"name": "ctl00$page_Content$XZQH$shi"}).find(attrs={"selected": "selected"}).string)
    v22 = str(soup.find(attrs={"name": "ctl00$page_Content$XZQH$qu"}).find(attrs={"selected": "selected"}).string)
    v23 = str(soup.find(attrs={"name": "ctl00$page_Content$XZQH$jie"}).find(attrs={"selected": "selected"}).string)
    v24 = str(soup.find(attrs={"name": "ctl00$page_Content$XZQH$cun"}).find(attrs={"selected": "selected"}).string)
    try:
        v25 = str(soup.find(attrs={"name": "ctl00$page_Content$xxdz$tb"})['value'])
    except:
        v25 = ''
    v26 = ''
    v26s = soup.find(attrs={"id": "ctl00_page_Content_ylzfxs_chkList1"}).findAll(attrs={"checked": "checked"})
    for i in v26s:
        v26 += str(i.next_sibling.string) + ' '
    try:
        other1 = str(soup.find(attrs={"name": "ctl00$page_Content$ylzfxs$tb"})['value'])
    except:
        other1 = ''
    v26 += other1
    try:
        v27 = str(soup.find(attrs={"name": "ctl00$page_Content$ylzh$tb"})['value'])
    except:
        v27 = ''
    v28 = str(soup.find(attrs={"id": "ctl00_page_Content_guomingshi_radioList1"}).find(
        attrs={"checked": "checked"}).next_sibling.string)
    v28s = soup.find(attrs={"id": "ctl00_page_Content_guomingshi_ctb1_chkList1"}).findAll(attrs={"checked": "checked"})
    for i in v28s:
        v28 += str(i.next_sibling.string) + ' '
    try:
        other2 = str(soup.find(attrs={"name": "ctl00$page_Content$guomingshi$ctb1$tb"})['value'])
    except:
        other2 = ''
    v28 += other2
    v29 = str(soup.find(attrs={"id": "ctl00_page_Content_baoloushi_rtb_radioList1"}).find(
        attrs={"checked": "checked"}).next_sibling.string)
    try:
        other3 = ' 化学品：' + str(soup.find(attrs={"name": "ctl00$page_Content$baoloushi$rtb$tb"})['value'])
    except:
        other3 = ' 化学品：无'
    try:
        other4 = ' 毒物：' + str(soup.find(attrs={"name": "ctl00$page_Content$baoloushi$ltb1$tb"})['value'])
    except:
        other4 = ' 毒物：无'
    try:
        other5 = ' 射线：' + str(soup.find(attrs={"name": "ctl00$page_Content$baoloushi$ltb2$tb"})['value'])
    except:
        other5 = ' 射线：无'
    v29 += other3 + other4 + other5
    v30 = str(soup.find(attrs={"id": "ctl00_page_Content_jibing_radioList1"}).find(
        attrs={"checked": "checked"}).next_sibling.string)
    v31 = str(soup.find(attrs={"id": "ctl00_page_Content_shoushu_radioList1"}).find(
        attrs={"checked": "checked"}).next_sibling.string)
    v32 = str(soup.find(attrs={"id": "ctl00_page_Content_waishang_radioList1"}).find(
        attrs={"checked": "checked"}).next_sibling.string)
    v33 = str(soup.find(attrs={"id": "ctl00_page_Content_shuxue_radioList1"}).find(
        attrs={"checked": "checked"}).next_sibling.string)
    v34 = str(soup.find(attrs={"id": "ctl00_page_Content_jiazushi_radioList1"}).find(
        attrs={"checked": "checked"}).next_sibling.string)
    try:
        v35 = str(soup.find(attrs={"id": "ctl00_page_Content_ycbs_radioList1"}).find(
            attrs={"checked": "checked"}).next_sibling.string)
    except:
        v35 = ''
    try:
        other6 = ' 疾病名称：' + str(soup.find(attrs={"name": "ctl00$page_Content$ycbs$tb"})['value'])
    except:
        other6 = ''
    v35 += other6
    v36 = ''
    v36s = soup.find(attrs={"id": "ctl00_page_Content_cjqk_chkList1"}).findAll(attrs={"checked": "checked"})
    for i in v36s:
        v36 += str(i.next_sibling.string) + ' '
    try:
        other7 = str(soup.find(attrs={"name": "ctl00$page_Content$cjqk$tb"})['value'])
    except:
        other7 = ''
    v36 += other7
    v37 = str(soup.find(attrs={"id": "ctl00_page_Content_pfss_radioList1"}).find(
        attrs={"checked": "checked"}).next_sibling.string)
    v38 = str(soup.find(attrs={"id": "ctl00_page_Content_rllx_radioList1"}).find(
        attrs={"checked": "checked"}).next_sibling.string)
    v39 = str(soup.find(attrs={"id": "ctl00_page_Content_yins_radioList1"}).find(
        attrs={"checked": "checked"}).next_sibling.string)
    v40 = str(soup.find(attrs={"id": "ctl00_page_Content_ces_radioList1"}).find(
        attrs={"checked": "checked"}).next_sibling.string)
    v41 = str(soup.find(attrs={"id": "ctl00_page_Content_qcl_radioList1"}).find(
        attrs={"checked": "checked"}).next_sibling.string)
    try:
        v42 = str(soup.find(attrs={"name": "ctl00$page_Content$jdrq$tb"})['value'])
    except:
        v42 = ''
    try:
        v43 = str(soup.find(attrs={"name": "ctl00$page_Content$jdr$ltb1$tb"})['value'])
    except:
        v43 = ''
    try:
        v44 = str(soup.find(attrs={"name": "ctl00$page_Content$jdr$ltb2$tb"})['value'])
    except:
        v44 = ''
    cur = conn.cursor()
    cur.execute("INSERT INTO 个人健康档案 VALUES ('" + v0 + "','" + v1 + "','" + v2 + "','" + v3 + "','" + v4 + "','" + v5
                + "','" + v6 + "','" + v7 + "','" + v8 + "','" + v9 + "','" + v10 + "','" + v11 + "','" + v12 + "','" + v13 +
                "','" + v14 + "','" + v15 + "','" + v16 + "','" + v17 + "','" + v18 + "','" + v19 + "','" + v20 + "','" + v21
                + "','" + v22 + "','" + v23 + "','" + v24 + "','" + v25 + "','" + v26 + "','" + v27 + "','" + v28 +
                "','" + v29 + "','" + v30 + "','" + v31 + "','" + v32 + "','" + v33 + "','" + v34 + "','" + v35 + "','" + v36
                + "','" + v37 + "','" + v38 + "','" + v39 + "','" + v40 + "','" + v41 + "','" + v42 + "','" + v43 + "','"
                + v44 + "')")
    conn.commit()
cur.close()
conn.close()
print(time.clock() - start)
