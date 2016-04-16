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

def getChiLie(soup):
    chilie=''
    if soup.find(attrs={"checked": "checked","id":'ctl00_page_Content_chilie_yx0'}):
        chilie+=soup.find(attrs={"checked": "checked","id":'ctl00_page_Content_chilie_yx0'}).next_sibling.string
    if soup.find(attrs={"checked": "checked","id":'ctl00_page_Content_chilie_yx1'}):
        chilie+=soup.find(attrs={"checked": "checked","id":'ctl00_page_Content_chilie_yx1'}).next_sibling.string
    if soup.find(attrs={"checked": "checked","id":'ctl00_page_Content_chilie_yx2'}):
        chilie+=soup.find(attrs={"checked": "checked","id":'ctl00_page_Content_chilie_yx2'}).next_sibling.string
    if soup.find(attrs={"checked": "checked","id":'ctl00_page_Content_chilie_yx3'}):
        chilie+=soup.find(attrs={"checked": "checked","id":'ctl00_page_Content_chilie_yx3'}).next_sibling.string
    chilie+=' '+str(soup.find(attrs={"id": "ctl00_page_Content_chilie_yx11_tb"}).get('value'))+' '\
            +str(soup.find(attrs={"id": "ctl00_page_Content_chilie_yx22_tb"}).get('value'))+' '\
            +str(soup.find(attrs={"id": "ctl00_page_Content_chilie_yx33_tb"}).get('value'))
    return chilie

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
    DetailInfo.append(str(soup.find(attrs={"name": "ctl00$page_Content$F_NJDATE$tb"}).get('value')))
    DetailInfo.append(str(soup.find(attrs={"name": "ctl00$page_Content$F_DOCTOR$tb"}).get('value')))
    DetailInfo.append(checkbox(soup, "ctl00_page_Content_F_ZZ_CHK_chkList1")
                        + str(soup.find(attrs={"id": "ctl00_page_Content_F_ZZ_CHK_tb"}).get('value')))
    DetailInfo.append(str(soup.find(attrs={"name": "ctl00$page_Content$F_TW$tb"}).get('value')))
    DetailInfo.append(str(soup.find(attrs={"name": "ctl00$page_Content$F_MB$tb"}).get('value')))
    DetailInfo.append(str(soup.find(attrs={"name": "ctl00$page_Content$F_HX$tb"}).get('value')))
    DetailInfo.append(str(soup.find(attrs={"id": "ctl00_page_Content_xyz_ltb1_tb"}).get('value'))+'/'+
                        str(soup.find(attrs={"id": "ctl00_page_Content_xyz_ltb2_tb"}).get('value')))
    DetailInfo.append(str(soup.find(attrs={"id": "ctl00_page_Content_xyy_ltb1_tb"}).get('value'))+'/'+
                        str(soup.find(attrs={"id": "ctl00_page_Content_xyy_ltb2_tb"}).get('value')))
    DetailInfo.append(str(soup.find(attrs={"id": "ctl00_page_Content_F_SG_tb"}).get('value')))
    DetailInfo.append(str(soup.find(attrs={"id": "ctl00_page_Content_F_TZ_tb"}).get('value')))
    DetailInfo.append(str(soup.find(attrs={"id": "ctl00_page_Content_F_YW_tb"}).get('value')))
    DetailInfo.append(str(soup.find(attrs={"id": "ctl00_page_Content_F_BMI_tb"}).get('value')))
    DetailInfo.append(radiobox(soup, "ctl00_page_Content_lnrpg_radioList1"))
    DetailInfo.append(radiobox(soup, "ctl00_page_Content_lnrzlpg_radioList1"))
    DetailInfo.append(radiobox(soup, "ctl00_page_Content_F_RZGN_OPT_radioList1"))
    DetailInfo.append(str(soup.find(attrs={"id": "ctl00_page_Content_F_RZGN_PF_tb"}).get('value')))
    DetailInfo.append(radiobox(soup, "ctl00_page_Content_F_QGZT_OPT_radioList1"))
    DetailInfo.append(str(soup.find(attrs={"id": "ctl00_page_Content_F_QGZT_PF_tb"}).get('value')))
    DetailInfo.append(radiobox(soup, "ctl00_page_Content_F_SHXG_DLPL_OPT_radioList1"))
    DetailInfo.append(str(soup.find(attrs={"id": "ctl00_page_Content_F_SHXG_DLFS_tb"}).get('value')))
    DetailInfo.append(str(soup.find(attrs={"id": "ctl00_page_Content_F_SHXG_DLSJ_tb"}).get('value')))
    DetailInfo.append(str(soup.find(attrs={"id": "ctl00_page_Content_F_SHXG_JCDLSJ_tb"}).get('value')))
    DetailInfo.append(checkbox(soup, "ctl00_page_Content_F_SHXG_YSXG_chkList1"))
    DetailInfo.append(radiobox(soup, "ctl00_page_Content_F_SHXG_SFXY_OPT_radioList1"))
    DetailInfo.append(str(soup.find(attrs={"id": "ctl00_page_Content_F_SHXG_MTXYL_tb"}).get('value')))
    DetailInfo.append(str(soup.find(attrs={"id": "ctl00_page_Content_F_SHXG_KSXYSJ_tb"}).get('value')))
    DetailInfo.append(str(soup.find(attrs={"id": "ctl00_page_Content_F_SHXG_JYSJ_tb"}).get('value')))
    DetailInfo.append(radiobox(soup, "ctl00_page_Content_F_SHXG_YJPL_OPT_radioList1"))
    DetailInfo.append(str(soup.find(attrs={"id": "ctl00_page_Content_F_SHXG_MCYJ_tb"}).get('value')))
    DetailInfo.append(radiobox(soup, "ctl00_page_Content_F_SHXG_SFJJ_OPT_radioList1"))
    DetailInfo.append(str(soup.find(attrs={"id": "ctl00_page_Content_F_SHXG_JJSJ_tb"}).get('value')))
    DetailInfo.append(str(soup.find(attrs={"id": "ctl00_page_Content_F_SHXG_KSYJSJ_tb"}).get('value')))
    DetailInfo.append(radiobox(soup, "ctl00_page_Content_zuijiu_radioList1"))
    DetailInfo.append(checkbox(soup, "ctl00_page_Content_F_SHXG_ZYYJ_CHK_chkList1")
                        + ' ' + str(soup.find(attrs={"id": "ctl00_page_Content_F_SHXG_ZYYJ_CHK_tb"}).get('value')))
    DetailInfo.append(radiobox(soup, "ctl00_page_Content_zybyw_radioList1"))
    DetailInfo.append(str(soup.find(attrs={"id": "ctl00_page_Content_zybgz_ltb1_tb"}).get('value')))
    DetailInfo.append(str(soup.find(attrs={"id": "ctl00_page_Content_zybgz_ltb2_tb"}).get('value')))
    DetailInfo.append(str(soup.find(attrs={"id": "ctl00_page_Content_fcwz_tb"}).get('value')))
    DetailInfo.append(radiobox(soup, "ctl00_page_Content_fcfh_radioList1")
                        +' '+str(soup.find(attrs={"id": "ctl00_page_Content_fcfh_tb"}).get('value')))
    DetailInfo.append(str(soup.find(attrs={"id": "ctl00_page_Content_fswz_tb"}).get('value')))
    DetailInfo.append(radiobox(soup, "ctl00_page_Content_fswzfh_radioList1")
                        +' '+str(soup.find(attrs={"id": "ctl00_page_Content_fswzfh_tb"}).get('value')))
    DetailInfo.append(str(soup.find(attrs={"id": "ctl00_page_Content_wlys_tb"}).get('value')))
    DetailInfo.append(radiobox(soup, "ctl00_page_Content_wlysfh_radioList1")
                        +' '+str(soup.find(attrs={"id": "ctl00_page_Content_wlysfh_tb"}).get('value')))
    DetailInfo.append(str(soup.find(attrs={"id": "ctl00_page_Content_hxwz_tb"}).get('value')))
    DetailInfo.append(radiobox(soup, "ctl00_page_Content_hxwzfh_radioList1")
                        +' '+str(soup.find(attrs={"id": "ctl00_page_Content_hxwzfh_tb"}).get('value')))
    DetailInfo.append(str(soup.find(attrs={"id": "ctl00_page_Content_zywhqt_tb"}).get('value')))
    DetailInfo.append(radiobox(soup, "ctl00_page_Content_zywhqtfh_radioList1")
                        +' '+str(soup.find(attrs={"id": "ctl00_page_Content_zywhqtfh_tb"}).get('value')))
    DetailInfo.append(checkbox(soup, "ctl00_page_Content_zywhqtfh_tb"))
    DetailInfo.append(getChiLie(soup))
    DetailInfo.append(checkbox(soup, "ctl00_page_Content_yanbu_chkList1")
                        +' '+str(soup.find(attrs={"id": "ctl00_page_Content_yanbu_tb"}).get('value')))
    DetailInfo.append(str(soup.find(attrs={"id": "ctl00_page_Content_lysl_ltb1_tb"}).get('value')))
    DetailInfo.append(str(soup.find(attrs={"id": "ctl00_page_Content_lysl_ltb2_tb"}).get('value')))
    DetailInfo.append(str(soup.find(attrs={"id": "ctl00_page_Content_jzsl_ltb1_tb"}).get('value')))
    DetailInfo.append(str(soup.find(attrs={"id": "ctl00_page_Content_jzsl_ltb2_tb"}).get('value')))
    DetailInfo.append(radiobox(soup, "ctl00_page_Content_F_TL_OPT_radioList1"))    #听力
    DetailInfo.append(radiobox(soup, "ctl00_page_Content_F_YD_OPT_radioList1"))
    DetailInfo.append(radiobox(soup, "ctl00_page_Content_F_YANDI_OPT_radioList1"))
    DetailInfo.append(radiobox(soup, "ctl00_page_Content_F_PF_OPT_radioList1")
                        +' '+str(soup.find(attrs={"id": "ctl00_page_Content_F_PF_OPT_tb"}).get('value')))
    DetailInfo.append(radiobox(soup, "ctl00_page_Content_gongmo_radioList1")
                        +' '+str(soup.find(attrs={"id": "ctl00_page_Content_gongmo_tb"}).get('value')))
    DetailInfo.append(radiobox(soup, "ctl00_page_Content_F_LB_OPT_radioList1")
                        +' '+str(soup.find(attrs={"id": "ctl00_page_Content_F_LB_OPT_tb"}).get('value')))
    DetailInfo.append(radiobox(soup, "ctl00_page_Content_F_FTZX_OPT_radioList1"))
    DetailInfo.append(radiobox(soup, "ctl00_page_Content_F_FHXY_OPT_radioList1")
                        +' '+str(soup.find(attrs={"id": "ctl00_page_Content_F_FHXY_OPT_tb"}).get('value')))
    DetailInfo.append(radiobox(soup, "ctl00_page_Content_F_FLY_OPT_radioList1")
                        +' '+str(soup.find(attrs={"id": "ctl00_page_Content_F_FLY_OPT_tb"}).get('value')))
    DetailInfo.append(str(soup.find(attrs={"id": "ctl00_page_Content_F_XZXL_tb"}).get('value')))
    DetailInfo.append(radiobox(soup, "ctl00_page_Content_F_XZXL_OPT_radioList1"))
    DetailInfo.append(radiobox(soup, "ctl00_page_Content_F_XZZY_OPT_radioList1")
                        +' '+str(soup.find(attrs={"id": "ctl00_page_Content_F_XZZY_OPT_tb"}).get('value')))
    DetailInfo.append(radiobox(soup, "ctl00_page_Content_F_FBYT_OPT_radioList1")
                        +' '+str(soup.find(attrs={"id": "ctl00_page_Content_F_FBYT_OPT_tb"}).get('value')))
    DetailInfo.append(radiobox(soup, "ctl00_page_Content_F_FBBK_OPT_radioList1")
                        +' '+str(soup.find(attrs={"id": "ctl00_page_Content_F_FBBK_OPT_tb"}).get('value')))
    DetailInfo.append(radiobox(soup, "ctl00_page_Content_F_FBGD_OPT_radioList1")
                        +' '+str(soup.find(attrs={"id": "ctl00_page_Content_F_FBGD_OPT_tb"}).get('value')))
    DetailInfo.append(radiobox(soup, "ctl00_page_Content_F_FBPD_OPT_radioList1")
                        +' '+str(soup.find(attrs={"id": "ctl00_page_Content_F_FBPD_OPT_tb"}).get('value')))
    DetailInfo.append(radiobox(soup, "ctl00_page_Content_F_FBYDX_OPT_radioList1")
                        +' '+str(soup.find(attrs={"id": "ctl00_page_Content_F_FBYDX_OPT_tb"}).get('value')))
    DetailInfo.append(radiobox(soup, "ctl00_page_Content_F_XZSZ_OPT_radioList1"))
    DetailInfo.append(radiobox(soup, "ctl00_page_Content_F_TSRQ_ZBDM_OPT_radioList1"))
    DetailInfo.append(radiobox(soup, "ctl00_page_Content_F_GMZZ_OPT_radioList1")
                        +' '+str(soup.find(attrs={"id": "ctl00_page_Content_F_GMZZ_OPT_tb"}).get('value')))
    DetailInfo.append(radiobox(soup, "ctl00_page_Content_ruxian_chkList1")
                        +' '+str(soup.find(attrs={"id": "ctl00_page_Content_ruxian_tb"}).get('value')))
    DetailInfo.append(radiobox(soup, "ctl00_page_Content_waiyin_radioList1")   #妇科
                        +' '+str(soup.find(attrs={"id": "ctl00_page_Content_waiyin_tb"}).get('value')))
    DetailInfo.append(radiobox(soup, "ctl00_page_Content_yindao_radioList1")
                        +' '+str(soup.find(attrs={"id": "ctl00_page_Content_yindao_tb"}).get('value')))
    DetailInfo.append(radiobox(soup, "ctl00_page_Content_gongjing_radioList1")
                        +' '+str(soup.find(attrs={"id": "ctl00_page_Content_gongjing_tb"}).get('value')))
    DetailInfo.append(radiobox(soup, "ctl00_page_Content_gongti_radioList1")
                        +' '+str(soup.find(attrs={"id": "ctl00_page_Content_gongti_tb"}).get('value')))
    DetailInfo.append(radiobox(soup, "ctl00_page_Content_fujian_radioList1")
                        +' '+str(soup.find(attrs={"id": "ctl00_page_Content_fujian_tb"}).get('value')))
    DetailInfo.append(str(soup.find(attrs={"id": "ctl00_page_Content_F_CT_EXP_tb"}).get('value')))    #其他
    DetailInfo.append(str(soup.find(attrs={"id": "ctl00_page_Content_F_XCG_HB_tb"}).get('value')))
    DetailInfo.append(str(soup.find(attrs={"id": "ctl00_page_Content_F_XCG_WBC_tb"}).get('value')))
    DetailInfo.append(str(soup.find(attrs={"id": "ctl00_page_Content_F_XCG_PLT_tb"}).get('value')))
    DetailInfo.append(str(soup.find(attrs={"id": "ctl00_page_Content_F_XCG_QT_tb"}).get('value')))
    DetailInfo.append(str(soup.find(attrs={"id": "ctl00_page_Content_F_NCG_NDB_tb"}).get('value')))
    DetailInfo.append(str(soup.find(attrs={"id": "ctl00_page_Content_F_NCG_NT_tb"}).get('value')))
    DetailInfo.append(str(soup.find(attrs={"id": "ctl00_page_Content_F_NCG_NTT_tb"}).get('value')))
    DetailInfo.append(str(soup.find(attrs={"id": "ctl00_page_Content_F_NCG_NQX_tb"}).get('value')))
    DetailInfo.append(str(soup.find(attrs={"id": "ctl00_page_Content_F_NCG_QT_tb"}).get('value')))
    DetailInfo.append(str(soup.find(attrs={"id": "ctl00_page_Content_F_KFXT_ltb1_tb"}).get('value'))+'或'+
                        str(soup.find(attrs={"id": "ctl00_page_Content_F_KFXT_ltb2_tb"}).get('value')))
    DetailInfo.append(radiobox(soup, "ctl00_page_Content_F_XDT_OPT_radioList1")
                        +' '+str(soup.find(attrs={"id": "ctl00_page_Content_F_XDT_OPT_tb"}).get('value'))) #心电图
    DetailInfo.append(str(soup.find(attrs={"id": "ctl00_page_Content_nwldb_tb"}).get('value')))
    DetailInfo.append(radiobox(soup, "ctl00_page_Content_F_DBQX_OPT_radioList1"))
    DetailInfo.append(str(soup.find(attrs={"id": "ctl00_page_Content_F_TSRQ_THXADB_tb"}).get('value')))
    DetailInfo.append(radiobox(soup, "ctl00_page_Content_ygkt_radioList1"))
    DetailInfo.append(str(soup.find(attrs={"id": "ctl00_page_Content_F_GGN_ALT_tb"}).get('value')))
    DetailInfo.append(str(soup.find(attrs={"id": "ctl00_page_Content_F_GGN_AST_tb"}).get('value')))
    DetailInfo.append(str(soup.find(attrs={"id": "ctl00_page_Content_F_GGN_ALB_tb"}).get('value')))
    DetailInfo.append(str(soup.find(attrs={"id": "ctl00_page_Content_F_GGN_TBIL_tb"}).get('value')))
    DetailInfo.append(str(soup.find(attrs={"id": "ctl00_page_Content_F_GGN_DBIL_tb"}).get('value')))
    DetailInfo.append(str(soup.find(attrs={"id": "ctl00_page_Content_F_SGN_SCR_tb"}).get('value')))  #肾功能
    DetailInfo.append(str(soup.find(attrs={"id": "ctl00_page_Content_F_SGN_BUN_tb"}).get('value')))
    DetailInfo.append(str(soup.find(attrs={"id": "ctl00_page_Content_xjnd_tb"}).get('value')))
    DetailInfo.append(str(soup.find(attrs={"id": "ctl00_page_Content_xnnd_tb"}).get('value')))
    DetailInfo.append(str(soup.find(attrs={"id": "ctl00_page_Content_F_XZ_CHO_tb"}).get('value')))  #血脂
    DetailInfo.append(str(soup.find(attrs={"id": "ctl00_page_Content_F_XZ_TG_tb"}).get('value')))
    DetailInfo.append(str(soup.find(attrs={"id": "ctl00_page_Content_F_XZ_LDLC_tb"}).get('value')))
    DetailInfo.append(str(soup.find(attrs={"id": "ctl00_page_Content_F_XZ_HDLC_tb"}).get('value')))
    DetailInfo.append(radiobox(soup, "ctl00_page_Content_F_XP_OPT_radioList1")
                        +' '+str(soup.find(attrs={"id": "ctl00_page_Content_F_XP_OPT_tb"}).get('value')))
    DetailInfo.append(radiobox(soup, "ctl00_page_Content_F_BC_OPT_radioList1")     #b超
                        +' '+str(soup.find(attrs={"id": "ctl00_page_Content_F_BC_OPT_tb"}).get('value')))
    DetailInfo.append(radiobox(soup, "ctl00_page_Content_gjtp_radioList1")
                        +' '+str(soup.find(attrs={"id": "ctl00_page_Content_gjtp_tb"}).get('value')))
    DetailInfo.append(str(soup.find(attrs={"id": "ctl00_page_Content_F_FZJC_EXP_tb"}).get('value')))
    DetailInfo.append(radiobox(soup, "ctl00_page_Content_F_ZY_PHZ_OPT_radioList1"))    #中医
    DetailInfo.append(radiobox(soup, "ctl00_page_Content_F_ZY_QXZ_OPT_radioList1"))
    DetailInfo.append(radiobox(soup, "ctl00_page_Content_F_ZY_YXZ_OPT_radioList1"))
    DetailInfo.append(radiobox(soup, "ctl00_page_Content_F_ZY_YIXZ_OPT_radioList1"))
    DetailInfo.append(radiobox(soup, "ctl00_page_Content_F_ZY_TSZ_OPT_radioList1"))
    DetailInfo.append(radiobox(soup, "ctl00_page_Content_F_ZY_SRZ_OPT_radioList1"))
    DetailInfo.append(radiobox(soup, "ctl00_page_Content_F_ZY_XYZ_OPT_radioList1"))
    DetailInfo.append(radiobox(soup, "ctl00_page_Content_F_ZY_QYZ_OPT_radioList1"))
    DetailInfo.append(radiobox(soup, "ctl00_page_Content_F_ZY_TBZ_OPT_radioList1"))
    DetailInfo.append(checkbox(soup, "ctl00_page_Content_F_JKWT_NXG_CHK_chkList1")    #健康问题
                        +' '+str(soup.find(attrs={"id": "ctl00_page_Content_F_JKWT_NXG_CHK_tb"}).get('value')))
    DetailInfo.append(checkbox(soup, "ctl00_page_Content_F_JKWT_SZ_CHK_chkList1")
                        +' '+str(soup.find(attrs={"id": "ctl00_page_Content_F_JKWT_SZ_CHK_tb"}).get('value')))
    DetailInfo.append(checkbox(soup, "ctl00_page_Content_F_JKWT_XZ_CHK_chkList1")
                        +' '+str(soup.find(attrs={"id": "ctl00_page_Content_F_JKWT_XZ_CHK_tb"}).get('value')))
    DetailInfo.append(checkbox(soup, "ctl00_page_Content_F_JKWT_XG_CHK_chkList1")
                        +' '+str(soup.find(attrs={"id": "ctl00_page_Content_F_JKWT_XG_CHK_tb"}).get('value')))
    DetailInfo.append(checkbox(soup, "ctl00_page_Content_F_JKWT_YB_CHK_chkList1")
                        +' '+str(soup.find(attrs={"id": "ctl00_page_Content_F_JKWT_YB_CHK_tb"}).get('value')))
    DetailInfo.append(radiobox(soup, "ctl00_page_Content_F_JKWT_SJ_OPT_radioList1")
                        +' '+str(soup.find(attrs={"id": "ctl00_page_Content_F_JKWT_SJ_OPT_tb"}).get('value')))
    DetailInfo.append(radiobox(soup, "ctl00_page_Content_F_JKWT_QTJB_radioList1")
                        +' '+str(soup.find(attrs={"id": "ctl00_page_Content_F_JKWT_QTJB_tb"}).get('value')))
    DetailInfo.append(radiobox(soup, "ctl00_page_Content_zhuyuanzhiliao_radioList1"))  #住院史
    DetailInfo.append(radiobox(soup, "ctl00_page_Content_jiatingbingchuang_radioList1"))
    DetailInfo.append(radiobox(soup, "ctl00_page_Content_yonghaoshi_radioList1"))
    DetailInfo.append(radiobox(soup, "ctl00_page_Content_jiezhongshi_radioList1"))
    DetailInfo.append(radiobox(soup, "ctl00_page_Content_F_JKPJ_OPT_radioList1"))
    DetailInfo.append(str(soup.find(attrs={"id": "ctl00_page_Content_F_JKPJ_YC1_tb"}).get('value')))  #异常
    DetailInfo.append(str(soup.find(attrs={"id": "ctl00_page_Content_F_JKPJ_YC2_tb"}).get('value')))
    DetailInfo.append(str(soup.find(attrs={"id": "ctl00_page_Content_F_JKPJ_YC3_tb"}).get('value')))
    DetailInfo.append(str(soup.find(attrs={"id": "ctl00_page_Content_F_JKPJ_YC4_tb"}).get('value')))
    DetailInfo.append(checkbox(soup, "ctl00_page_Content_jkzd_chkList1")
                        +' '+str(soup.find(attrs={"id": "ctl00_page_Content_jkzd_tb"}).get('value')))
    DetailInfo.append(checkbox(soup, "ctl00_page_Content_F_JJCF_WXYS_CHK_chkList1")
                        +' '+str(soup.find(attrs={"id": "ctl00_page_Content_F_JJCF_WXYS_CHK_tb"}).get('value')))
    DetailInfo.append(str(soup.find(attrs={"id": "ctl00_page_Content_F_JJCF_JFMB_tb"}).get('value')))  #减体重
    DetailInfo.append(str(soup.find(attrs={"id": "ctl00_page_Content_jyjzym_tb"}).get('value')))
    DetailInfo.append(str(soup.find(attrs={"id": "ctl00_page_Content_jldarq_tb"}).get('value')))
    DetailInfo.append(str(soup.find(attrs={"id": "ctl00_page_Content_lrr_ltb1_tb"}).get('value')))
    DetailInfo.append(str(soup.find(attrs={"id": "ctl00_page_Content_lrr_ltb2_tb"}).get('value')))
    DetailInfo.append(str(soup.find(attrs={"id": "ctl00_page_Content_updatetime_tb"}).get('value')))
    DetailInfo.append(str(soup.find(attrs={"id": "ctl00_page_Content_updateID_tb"}).get('value')))
    return DetailInfo


if __name__ == "__main__":
    start = time.clock()
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123456', db='spider_data', charset='utf8')
    cur = conn.cursor()
    dir = 'D:\爬虫数据-医疗\爬虫数据-医疗-王伟伟\www-爬虫数据\爬虫原始数据\健康体检'
    allFiles = getAllFile(dirname=dir)
    count = 0
    for allFile in allFiles:
        soup = BeautifulSoup(open(dir + '\\' + allFile, encoding="utf-8"), "lxml")
        basic = getBasicInfo(soup)
        detail = getDetailInfo(soup)
        basic.extend(detail)
        data_insert('健康体检',basic)
        print(count)
        count += 1
    cur.close()
    conn.close()
    print('总时间为:', time.clock() - start)
