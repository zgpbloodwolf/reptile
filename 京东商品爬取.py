import urllib.request
import re
import ssl
co=[]
def writ_filetxt(html):
    with open(r'C:\Users\MyPC\PycharmProjects\Django object\axf\info.txt','a') as f:
        f.write(html)
def image(url,i):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.5514.400 QQBrowser/10.1.1660.400"}
    req = urllib.request.Request(url, headers=headers)
    context = ssl._create_unverified_context()
    response = urllib.request.urlopen(req, context=context)
    try:
        HTML = response.read().decode('gbk')
        # with open(r'C:\Users\MyPC\PycharmProjects\Django object\axf\jd11.html','wb') as f:
        #     f.write(HTML)
        #类型爬取
        kin_par='mbNav-2">(.*?)</a>'
        re_kin = re.compile(kin_par,re.S)
        kind = re_kin.findall(HTML)[0]
        # print(kind)
        #图片爬取
        par='spec-img(.*?)/>'
        re_pic = re.compile(par,re.S)
        picelist = re_pic.search(HTML).group()
        # print(picelist)
        #名字爬取
        name_par='alt="(.*?)"/>'
        re_name = re.compile(name_par,re.S)
        name=re_name.findall(picelist)[0]
        name = re.sub('\s','',name)
        # print(name)
        img = re.search(r'//(.*?).jpg',picelist).group()
        img_url = 'https:'+img
        urllib.request.urlretrieve(img_url, filename=r"C:\Users\MyPC\PycharmProjects\Django object\axf\tup\\" + str(i) + '.jpg')
        c = [kind,name,'C:\\Users\MyPC\PycharmProjects\Django object\\axf\\tup\\' + str(i) + '.jpg']
        writ_filetxt(str(c)+'\n')
    except:
        pass
for i in range(851773,899999):
    url = r"https://item.jd.com/"+str(i)+".html"
    print(i)
    info = image(url,i)





