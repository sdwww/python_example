import threading
import requests
import time
from bs4 import BeautifulSoup
import os
import xlrd


def login():
    login_url = "http://10.116.110.88:7001/sicp3/logon.do"
    login_data = {'method': 'doLogon', 'userid': '3337', 'passwd': 'a4fa7175d4757e45eac71a8487751f63',
                  'userLogSign': '0', 'passWordLogSign': '0', 'screenHeight': '768', 'screenWidth': '1366',
                  'mode': 'true', 'fromProduct': 'false', 'ukeyid': ''}
    s.post(login_url, data=login_data)
    req = s.get('http://10.116.110.88:7001/sicp3/index.jsp')
    soup = BeautifulSoup(req.text, 'lxml')
    ticks = soup.findAll("script")
    for tick in ticks:
        if tick.string and str(tick.string).find('__LOGON_TICKET__') != -1:
            st_index = str(tick.string).find('__LOGON_TICKET__')
            return str(tick.string)[st_index + 20:st_index + 61]


def getId():
    all_id = []
    some_id = []
    xls_name = ['东张博', '马营', '西张博', '薛屯', '杨屯', '张飞垓']
    for xls in xls_name:
        this_id = []
        data = xlrd.open_workbook('./居民信息/' + xls + '.xls')
        table = data.sheets()[0]
        for i in table.col_values(0):
            this_id.append(i)
        this_id.pop(0)
        all_id.extend(this_id)
    for i in range(add_num, add_num + 750):
        some_id.append(all_id[i])
    return some_id


def getRydj(local_num):
    params = {'method': 'lovForPerInfo', 'containerName': 'formPatientManage', '_xmlString':
        '<?xml version="1.0" encoding="UTF-8"?><p><s rqlb="B"/><s grbh="' + all_id[local_num] + '"/></p>',
              '_jbjgqxfw': '37083205', '_sbjbjg': '37083205', '_dwqxfw': '',
              '__logon_ticket': ticket}
    content = s.post('http://10.116.110.88:7001/sicp3/md3Lov.do', data=params, timeout=20).text
    soup = BeautifulSoup(content, 'lxml')
    rydj = str(soup.find(attrs={"id": "rydjid_1"})['value'])
    return rydj


def saveHtmltoFile(savePath, filename, content):
    filename.replace(':', '')
    if not os.path.isdir(savePath + '/'):
        os.mkdir(savePath + '/')
    html = open(savePath + '/' + filename + '.html', 'w', encoding='utf-8')
    html.write(content)
    html.close()


def getTreePost(rydj, savePath, nodeId, level):
    time.sleep(0.1)
    rootUrl = 'http://10.116.110.88:7001/sicp3/treeServlet'
    if level == '1':
        post_data = {'nodeId': nodeId, 'level': '1', 'className': 'cp3.md3.query.PerInfoQueryTree',
                     '_sbjbjg': '37083205', 'userParameter': 'rydjid:' + rydj + ';rqlb:B'}
    elif level == '2':
        post_data = {'nodeId': nodeId, 'level': '2', 'className': 'cp3.md3.query.PerInfoQueryTree', 'userParameter':
            'rydjid:' + rydj + ';rqlb:B;', '_sbjbjg': '37083205', '_jbjgqxfw': '37083205'}
    elif level == '3':
        post_data = {'nodeId': nodeId, 'level': '3', 'className': 'cp3.md3.query.PerInfoQueryTree', 'userParameter':
            'rydjid:' + rydj + ';rqlb:B;', '_sbjbjg': '37083205', '_jbjgqxfw': '37083205', '_sbjbjg': '37083205',
                     '_jbjgqxfw': '37083205'}
    else:
        return
    tree2 = s.post(url=rootUrl, data=post_data, timeout=20)
    soup = BeautifulSoup(tree2.text, 'lxml')
    els = soup.find('tree').findAll('tree')
    for tree in els:
        nodevalue = str(tree["nodevalue"])
        if nodevalue in no_use:
            return
        ac = str(tree["action"])
        if len(ac) > 17:
            pu = ac[15:len(ac) - 2]
            postUrl = "http://10.116.110.88:7001/sicp3/" + pu + "&_xmlString=<?xml version=\"1.0\" encoding=\"UTF-8\"?><p><s _sbjbjg=\"37083205\"/></p>&_jbjgqxfw=37083205&_dwqxfw=" + "&__logon_ticket=" + ticket
            postContent = s.post(postUrl, 'gbk', timeout=20).text
            saveHtmltoFile(savePath, nodevalue, postContent)

        haveChild = str(tree["havechild"])
        if haveChild == 'true':
            npath = savePath + "/" + nodevalue.replace(':', '')
            nlevel = str(tree["level"])
            nnodeId = str(tree["nodeid"])
            getTreePost(rydj, npath, nnodeId, nlevel)


class myThread(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.t_name = name

    def run(self):
        global num  # 声明为全局变量
        while num < len(all_id):
            mylock.acquire()
            local_num = num
            num += 1
            mylock.release()
            try:
                rydj = getRydj(local_num)
                if rydj:
                    root0_url = "http://10.116.110.88:7001/sicp3/md3PatientTree.do"
                    lev0_post = {'method': 'fwTreePagePersonInfoJsp', '_xmlString':
                        '<?xml version="1.0" encoding="UTF-8"?><p><s rydjid="' + rydj + '"/><s _sbjbjg="37083205"/></p>',
                                 '_jbjgqxfw': '37083205', '_dwqxfw': '', '__logon_ticket': ticket};
                    root0_cont = s.post(root0_url, data=lev0_post, timeout=20).text
                    if not os.path.isdir(rootdir + str(local_num + add_num) + '-' + all_id[local_num] + '/'):
                        os.mkdir(rootdir + str(local_num + add_num) + '-' + all_id[local_num] + '/')
                    html = open(rootdir + str(local_num + add_num) + '-' + all_id[local_num] + '.html', 'w',
                                encoding='gbk')
                    html.write(root0_cont)
                    html.close()
                    getTreePost(rydj, rootdir + str(local_num + add_num) + '-' + all_id[local_num], "root_ROOT", '1')
            except:
                error_log = open('error.txt', 'a')
                error_log.write(all_id[local_num] + '\n')
                error_log.close()
                time.sleep(1)
                continue
            print(local_num, self.name)
            time.sleep(1)
        print(time.clock() - start)


def creatManyThreads(count):
    for i in range(count):
        myThread(i).start()


if __name__ == '__main__':
    start = time.clock()
    rootdir = 'C:/Users/www/lssb/'
    mylock = threading.RLock()
    num = 0
    add_num = 5000
    s = requests.session()
    headers = {'Content-type': 'application/x-www-form-urlencoded'}
    ticket = login()
    print('ticket', ticket)
    no_use = ['备案信息及定点医院查询', '当日费用凭单', '个人账户对账单', '个人账户收支查询',
              '医疗费支出明细', '暂缓费用查询', '个人账户收支查询', '个人账户支出明细', '人员变更历史',
              '缴费历史', '个人申报', '个人账户', '年度统筹情况', '报销单据']
    all_id = getId()
    creatManyThreads(10)
