import re
def cleaner(filename):
    '''用于处理抓取页面信息，清洗为元胞数组形式，每个小元胞包含ID和电影名称'''
    output=[]
    fname = filename + '.txt'
    f = open(fname, mode='r',encoding="utf8")
    cont = f.read()
    cont=cont.replace("\n","")
    f.close()
    #filmID = "IDIDID(.*？)&&"

    filmname = "<h3 class=\"name\">(.*?)</h3>"  # 提取电影名称
    pic='<img class=\"avatar\" src=\"(.*?)@' #提取电影图片链接

    # 编译正则表达式
    filmnameb = re.compile(filmname)
    # 电影种类<li class="ellipsis">剧情,爱情</li>
    kindb= re.compile('<li class=\"ellipsis\">(.+?)</li>')
    contantsb=re.compile('<span class=\"dra\">(.*?)</span>')
    #filmIDb = re.compile(filmID)
    picb = re.compile(pic)
    # 在源文本中搜索符合正则表达式的部分
    #IDf = re.findall(filmIDb, cont)
    namef = re.findall(filmnameb,cont)
    picf = re.findall(picb, cont)
    kindf = re.findall(kindb, cont)
    contantsb = re.findall(contantsb, cont)
    output.append(['【片名】'])
    output.append(namef)
    output.append(['【链接】'])
    output.append(picf)
    output.append(['【信息】'])
    output.append(kindf)
    output.append(['【评论】'])
    output.append(contantsb)
    return output

def writelist(newfilename,inputlist):
    '''把被清洗好的数据写入文本文件'''
    newname=newfilename+'.txt'
    newf = open(newname, mode='w',encoding="utf8")
    for inp in inputlist:
        if 0:
            pass
        newf.write(inp+'\n')
    newf.close()

data=cleaner('testclean')
print(data)
#writelist('daluCLEAN2',data)
'''
f = open('testclean.txt', mode='r',encoding="utf8")
cont = f.read()
f.close()
devb = re.compile("IDIDID(*)FILEEND")
namef = re.findall(devb,cont)
print(namef)
'''