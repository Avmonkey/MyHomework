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
        answer='errorpage:'+url
        print(answer)
    return answer


def writetxt(name,cont):
    filename=name+'.txt'
    fileobj = open(filename, mode='a+',encoding="utf8")
    fileobj.write(cont)
    fileobj.close()


def urlmaker(s,y,t):
    sourceurl='https://maoyan.com/films?showType=3&sortId=1&sourceId=2&yearId=14&offset=0'



def stop(con):
    '需要re。传入页面内容，若没有了则返回true'
    stopsign='没有找到相关结果'
    bian = re.compile(stopsign)  # 我们在编译这段正则表达式
    matcher1 = re.findall(bian, con)
    if matcher1 == []:
        return False
    else:
        return True


def test():
    emptypage='https://maoyan.com/films?showType=3&sortId=1&sourceId=2&yearId=14&offset=660'
    loginpage='https://maoyan.com/films?showType=3&sortId=1&yearId=14&offset=2010'
    normalpage='https://maoyan.com/films?showType=3&sortId=1&yearId=14&offset=210'
    empty=spider(emptypage)
    normal=spider(normalpage)
    login = spider(loginpage)
    k=stop(empty)
    l=stop(normal)
    m=stop(login)
    ##writetxt('normal',normal)
    print(k)
    print(l)
    print(m)



#正式开爬！
i=True
sourceIDlist=['&sourceId=2','&sourceId=10','&sourceId=13']
#2是中国大陆，10香港，13台湾
yearIDlist=[14,13,12,11,10,9,8,7,6]
fullurl='https://maoyan.com/films?showType=3&sortId=1&sourceId=2&yearId=14&offset=0'
sourceurl2='https://maoyan.com/films?showType=3&sortId=1&sourceId=2&yearId=14'
sourceurl3='https://maoyan.com/films?showType=3&sortId=1&sourceId=2'
offsets=0
havearest=0
error=0

# 写入文件
filename='xianggang.txt'



for yearID in yearIDlist:
    #大陆的分年存文件
    fileobj = open('dalu'+str(yearID)+'.txt', mode='a+', encoding="utf8")
    while 1:
        tempurl=sourceurl3+"&yearId="+str(yearID)+"&offset="+str(offsets)
        offsets += 30
        havearest+=1
        tempcon=spider(tempurl)
        fileobj.write(tempcon)
        time.sleep(0.2)
        #print(tempurl)
        if havearest>15:
            time.sleep(2)
            print('delay')
            havearest=0
        if offsets >=2000:
            offsets = 0
            break
        elif stop(tempcon):
            offsets = 0
            break

    print("爬完一年"+str(yearID))
    fileobj.write('\n\n\n\n分割线'+str(yearID)+'\n\n\n\n')
    fileobj.close()
print('终于完了！！！')
