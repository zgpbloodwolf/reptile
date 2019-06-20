import urllib.request
import ssl
import re
def xiushi(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; "
                      "WOW64) AppleWebKit/537.36 (KHTML, "
                      "like Gecko) Chrome/63.0.3239.26 "
                      "Safari/537.36 Core/1.63.5514.400 "
                      "QQBrowser/10.1.1660.400"}
    req = urllib.request.Request(url,headers=headers)
    context = ssl._create_unverified_context()
    response = urllib.request.urlopen(req, context=context)
    HTML = response.read().decode("utf-8")
    # with open(r'C:\Users\MyPC\PycharmProjects\爬虫\xiushi'
    #           r'.html','w') as f:
    #
    #     f.write(HTML)
    pat = r'<div class="author clearfix">(.*?)<span class="stats-vote"><i class="number">'
    re_joke = re.compile(pat,re.S)
    divlist = re_joke.findall(HTML)
    print(len(divlist))
    # print(divlist)
    dic={}
    for div in divlist:
        #用户名
        re_u = re.compile(r"<h2>(.*?)</h2>",re.S)
        username = re_u.findall(div)[0].strip()
        #段子
        re_d = re.compile(r'<div class="content">\n<span>('
                          r'.*?)</span>',re.S)
        duanzi = re_d.findall(div)[0].strip()
        dic[username] = duanzi
    return dic
url = r"https://www.qiushibaike.com/text"
info = xiushi(url)

for usename,duanzi in info.items():
    print('作者：'+usename+'\n'+'段子：'+duanzi)
    with open(r'C:\Users\MyPC\PycharmProjects\爬虫\xiushi'
                  r'.txt','a',encoding='utf-8') as f:
        f.write('作者：'+usename+'\n'+'段子：'+duanzi+'\n\n')
