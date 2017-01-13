import requests
from bs4 import BeautifulSoup
import re
url = 'http://www.1kkk.com/manhua-shaonvaiqing/'

url_main = 'http://www.1kkk.com'

tag1 ="#ipg"

path = "F:\\testing"




regex = re.compile(r"/ch")
'''r = requests.get(url)
t = BeautifulSoup(r.text)
for link in t.findAll('p'):
    link1 = link.a.get('href')
    url2 = url1 +str(link1)
    print (url2)
    print('-----------------------')'''

def confirm_page(num):
    url_list=[]
    for i in range(1,num):
        add_str = '-p' +str(i)+"/"
        url_go = split_url(url) +add_str
        if url_go not in url_list:
            url_list.append(url_go)
      #  print("It's page: " + str(i))
       # print
    print(url_list)
    return url_list







def split_url(url):
    regex = re.compile(r"/d/")

    if url.endswith(str(regex)):
        url = url[:-1]
    return url


def find_exact_manga(url_target,tag):
    url_list=[]
    get_url = requests.get(url_target)
    url_info = BeautifulSoup(get_url.text)
    for link in url_info.findAll(tag):
        try:
            manga_link = link.a.get('href')
            url2 = url_main +str(manga_link)
            if url2 not in url_list:
                url_list.append(url2)
          #  print (url2)
           # print('-----------------------')
        except:
            pass
    print('***********One Page Complete**************')
    return url_list

def find_manga_links(url_the_manga):
    url_list =[]

    get_url = requests.get(url_the_manga)
    url_info = BeautifulSoup(get_url.text)
    for link in url_info.findAll('li'):

        try:
            manga_link = link.a.get('href')
            flag = regex.match(manga_link)
            if flag:
                url2 = url_main +str(manga_link)
            if url2 not in url_list:
                url_list.append(url2)
           # print(url2)
           # print('-----------------------')
        except:
            pass
    return url_list

def read_page(url):
    get_url = requests.get(url)                    #为了文件夹名字，抓取漫画名字
    name = BeautifulSoup(get_url.text)
    jpg_link = name.get("src")
    print(jpg_link)
    print(str(name.h1).split(">")[1].split("<")[0])   #掐头去尾
    for i in range(1,50):
        url_new = url +tag1+str(i)
        get_url = requests.get(url_new)
        name = BeautifulSoup(get_url.text)
        jpg_link = name.findAll("div", id= "showimage")

        print(jpg_link)

        print(url_new)






for i in confirm_page(2):
    #Find the needed page and return a list
    print("现在的页码是："+i)
    for n in find_exact_manga(i,'p'):
        #Find the manga and return
        print("现在的漫画地址是："+n)
        for c in find_manga_links(n):
            print("现在查找的漫画单张地址是: "+c)
            #Find all chapters
            print(c)
            read_page(c)







