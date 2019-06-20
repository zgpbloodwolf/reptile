import urllib.request
import ssl
import re
import os
from collections import deque
#写入文件
def writ_filehtml(html,topath):
    with open(topath,'wb') as f:
        f.write(html)
def writ_filetxt(html,topath):
    with open(topath,'a') as f:
        f.write(html)
#浏览器模拟
def get_response(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.5514.400 QQBrowser/10.1.1660.400"}
    req = urllib.request.Request(url, headers=headers)
    context = ssl._create_unverified_context()
    response = urllib.request.urlopen(req, context=context)
    return response.read()
def qq_crawler(url,topath):
    topathtxt = topath+r'\qq.txt'
    qqcra = get_response(url)
    html_str = str(qqcra)
    patqq = r"[1-9]\d{4,10}"
    re_qq = re.compile(patqq)
    qq_list = re_qq.findall(html_str)
    qq_list = list(set(qq_list))
    for qq in qq_list:
        writ_filetxt(qq+'\n',topathtxt)
    paturl = r'(((http|ftp|https)://)(([' \
             r'a-zA-Z0-9\._-]+\.[' \
          r'a-zA-Z]{2,6})|([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{' \
          r'1,3}\.[0-9]{1,3}))(:[0-9]{1,4})*(/[' \
          r'a-zA-Z0-9\&%_\./-~-]*)?)'
    re_url = re.compile(paturl)
    url_list = re_url.findall(html_str)
    url_list = list(set(url_list))
    return url_list
def center(url,topath):
    que = deque()
    que.append(url)
    while len(que) !=0:
        try:
            target_url = que.popleft()
            urllist =  qq_crawler(target_url,topath)
            for item in urllist:
                temo_url = item[0]
                que.append(temo_url)
        except :
            pass
url = "http://tieba.baidu.com/p/5471533241"
topath=r'C:\Users\MyPC\PycharmProjects\爬虫\爬取QQ号'
center(url,topath)



