import requests
import threading
from bs4 import BeautifulSoup
import time
import os
from os.path import getsize


def saveImage(local_num):
    response = session.get(list[local_num * 2 + 1], stream=True)
    image = response.content
    with open(DstDir + list[local_num * 2] + '.jpg', "wb") as jpg:
        jpg.write(image)
        jpg.close
    if getsize(DstDir + list[local_num * 2] + '.jpg') < 10000:
        os.remove(DstDir + list[local_num * 2] + '.jpg')
        return False
    return True


class myThread(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.t_name = name

    def run(self):
        global num  # 声明为全局变量
        while num < len(list) / 2:
            mylock.acquire()
            local_num = num
            num += 1
            mylock.release()
            if saveImage(local_num):
                print("保存文件" + DstDir + list[local_num * 2] + '.jpg', self.name)
        time.sleep(0.1)


def creatManyThreads(count):
    threads = []
    for i in range(count):
        myth = myThread(i)
        myth.start()
        threads.append(myth)
    for thread in threads:
        thread.join()


def getimagelist(webUrl):
    web = requests.get(webUrl)
    soup = BeautifulSoup(web.text, 'lxml')
    pagelist = soup.findAll('img')
    for page in pagelist:
        try:
            list.append(page['alt'])
            list.append(page['r-lazyload'])
        except:
            pass


if __name__ == "__main__":
    start = time.clock()
    mylock = threading.RLock()
    num = 0
    list = []
    session = requests.session()
    DstDir = "C:/Users/www/Pictures/test/"
    for i in range(250):
        webUrl = 'http://v.qq.com/x/teleplaylist/?sort=4&offset=' + str(i*20) + '&itype=-1'
        getimagelist(webUrl)
        print(i)
    print(list.__len__())
    creatManyThreads(5)
    print('总时间为:', time.clock() - start)
