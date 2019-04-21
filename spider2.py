import requests
import re
import time


def spider(url):
    #url='https://maoyan.com/films?showType=3/'
    #filename=filename+'.txt'
    #fileobj = open(filename, 'a+')
    try:
        reobj=requests.get(url)
        answer=reobj.text
        print('done')
    except:
        answer='errorpage:'+url+'\n'
        print(answer)
    return answer

def writetxt(name,cont):
    filename=name+'.txt'
    fileobj = open(filename, mode='a+',encoding="utf8")
    fileobj.write(cont)
    fileobj.close()

def readIDs(name):
    filename = name + '.txt'
    fileobj = open(filename, mode='r', encoding="utf8")
    temp=fileobj.read()

    ids = '(\d+)##'
    idsb = re.compile(ids)  # 编译正则表达式
    IDlist = re.findall(idsb, temp)
    fileobj.close()
    return IDlist

def sort(cont):
    output=[]
    cont = cont.replace("\n", "")#取消回车
    filmname = "<h3 class=\"name\">(.*?)</h3>"  # 提取电影名称
    pic = '<img class=\"avatar\" src=\"(.*?)@'  # 提取电影图片链接
    # 编译正则表达式
    filmnameb = re.compile(filmname)
    # 电影种类<li class="ellipsis">剧情,爱情</li>
    kindb = re.compile('<li class=\"ellipsis\">(.+?)</li>')
    contantsb = re.compile('<span class=\"dra\">(.*?)</span>')
    pinglunb=re.compile('<div class="comment-content">(.+?)</div>')
    picb = re.compile(pic)
    # 在源文本中搜索符合正则表达式的部分
    namef = re.findall(filmnameb, cont)
    picf = re.findall(picb, cont)
    kindf = re.findall(kindb, cont)
    contantsf = re.findall(contantsb, cont)
    pinglunf = re.findall(pinglunb, cont)
    output.append(['【片名】'])
    output.append(namef)
    output.append(['【封面】'])
    output.append(picf)
    output.append(['【信息】'])
    output.append(kindf)
    output.append(['【简介】'])
    output.append(contantsf)
    output.append(['【评论】'])
    output.append(pinglunf)
    return output




'''

cont=spider(testurl)
writetxt('testconf',cont)
'''
sourceURL='https://maoyan.com/films/'
openfilename='daluCLEAN' # 要打开的文件名称在这里改
IDlist=readIDs(openfilename)
# 创建文件
wfilename=openfilename+'grabs'

wfilename=wfilename+'.txt'
fileobj = open(wfilename, mode='a+',encoding="utf8")
print('文件创建成功')


#循环参数
sleeptimes=0
trueline=0

for ID in IDlist:
    URL=sourceURL+ID
    print(URL)
    trueline += 1
    persent=round(trueline*100/len(IDlist),3)

    cont=spider(URL)
    k=sort(cont)
    fileobj.write(str(trueline)+'##'+ID+'&&')
    for mm in k:
        for m in mm:
            fileobj.write(str(m)+'\t')
    fileobj.write('FILEEND\n')
    sleeptimes+=1
    #time.sleep(0.1)
    print('进度'+str(persent)+'%')

    if sleeptimes >=50:
        time.sleep(5)
        sleeptimes=0
fileobj.close()
print('完成！')
