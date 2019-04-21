#用于分析爬取网页代码，抓到片名+网页
import re
def cleaner(filename):
    '''用于处理抓取页面信息，清洗为元胞数组形式，每个小元胞包含ID和电影名称'''
    fname = filename + '.txt'
    f = open(fname, mode='r',encoding="utf8")
    cont = f.read()
    f.close()
    p1 = "data-val=\"\{movieId:(.*)\}\">(.+)<"  # 寻找相应代码段
    pattern1 = re.compile(p1)  # 我们在编译这段正则表达式
    matcher1 = re.findall(pattern1,cont)  # 在源文本中搜索符合正则表达式的部分
    return matcher1

def writelist(newfilename,cleandata):
    '''把被清洗好的数据写入文本文件'''
    newname=newfilename+'.txt'
    newf = open(newname, mode='w',encoding="utf8")
    # newf.write('ID'+'Name\n')
    for eachmovie in cleandata:
        newf.write(str(eachmovie[0]) + '##' + str(eachmovie[1]) + '&&\n')
    newf.close()

data=cleaner('dalucom')
writelist('daluCLEAN',data)



