import os
import requests
from bs4 import BeautifulSoup

# Create your views here.
# 首先我们写好抓取网页的函数
from django.utils.crypto import random
from django.utils.datetime_safe import time

# 简书爬文章 http://www.jianshu.com/c/8c92f845cd4d 绘画
address='http://www.jianshu.com/'

def get_html(url):
    try:
        r = requests.get(url,timeout=30)
        r.raise_for_status()
        r.encoding='utf-8'
        return r.text
    except:
        return "ERROR"

def get_article(url):
    html = get_html(url)
    soup = BeautifulSoup(html, 'lxml')
    litagList = soup.find('ul', {'class': 'note-list'}).find_all('li')

    contents = []
    for litag in litagList:
        content = {}
        try:
            aobj = litag.find('a',{'class': 'title'})
            content['title'] = aobj.text.strip()
            content['url'] = aobj['href']
            content['content'] = getContent(address + aobj['href'])
            content['abstract'] = litag.find('p',{'class': 'abstract'})
            content['author'] = litag.find('div',{'class': 'name'}).find('a', {'class': 'blue-link'}).text
            contents.append(content)
        except:
            print('出了点小问题')
    return contents

# 获取文章
def getContent(url):
    html = get_html(url)
    soup = BeautifulSoup(html, 'lxml')
    divObj = soup.find('div', {'class': 'show-content'})
    imagelist = divObj.find_all('div',{'class': 'image-package'})
    currtime = time.localtime()
    # 创建保存图片的目录
    dirname = time.strftime("%Y%m%d", currtime)
    path = '/blog/static/' + dirname
    mkdir(path)
    imageprefix = time.strftime("%Y%m%d%H%M%S", currtime)

    for divimage in imagelist:
        image = divimage.find('img')
        imagesrc = image['src']
        imagedata = requests.get('http:'+ imagesrc).content
        imagepath = path+'/'+ imageprefix+''+random.randint(101, 999)+'.png'
        with open(imagepath, 'wb') as f:
            f.write(imagedata)
        image['src'] = imagepath
        del image['data-original-src']

    return divObj


def mkdir(path):
    '''
    防止目录存在
    '''
    if not os.path.exists(path):
        os.mkdir(path)

# 保存数据
def save(contents):
    print(contents)

# 生成静态页
def createStaticHtml(content):
    print(content)