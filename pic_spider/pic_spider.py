import requests
import threading
from bs4 import BeautifulSoup
import re
import time


def saveImage(imgUrl, imgName="default.jpg"):
    response = requests.get(imgUrl, stream=True)
    image = response.content
    DstDir = "C:/Users/www/Pictures/test/"
    print("保存文件" + DstDir + imgName)
    try:
        with open(DstDir + imgName, "wb") as jpg:
            jpg.write(image)
    except IOError:
        print("IO Error\n")
        return
    finally:
        jpg.close


def downImageViaMutiThread(filelist):
    task_threads = []  # 存储线程
    count = 1
    for file in filelist:
        filename = file.replace("/", "-")
        if 'com-' in filename:
            p = re.compile(r'com-')
            filename = p.split(filename)[1]
            t = threading.Thread(target=saveImage, args=(file, filename))
            count = count + 1
            task_threads.append(t)
    for task in task_threads:
        task.start()
    for task in task_threads:
        task.join()


def getfilelist(pageUrl):
    try:
        filelist = []
        web = requests.get(pageUrl)
        soup = BeautifulSoup(web.text, 'lxml')
        for photo in soup.find_all('img'):
            filelist.append(photo.get('src'))
    except:
        pass
    return filelist


def getweblist(webUrl):
    web = requests.get(webUrl)
    soup = BeautifulSoup(web.text, 'lxml')
    weblist = []
    for pagelist in soup.find_all('a'):
        if len(weblist) < 20:
            weblist.append(pagelist.get('href'))
    return weblist


if __name__ == "__main__":
    start = time.clock()
    webUrl = 'http://www.csdn.net/'
    list = getweblist(webUrl)
    for page in list:
        imagelist = getfilelist(page)
        downImageViaMutiThread(imagelist)
    print('总时间为:', time.clock() - start)
