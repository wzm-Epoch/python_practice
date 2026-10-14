"""
@File : 4案例_生成器生成批次歌词.py
@Author : 王子墨
@Description : 
@Date :2026/8/29
"""
import math

def dataset_loader(batch_size): # 8条/批次
    """
    自定义的 歌词 批量生成器
    :param batch_size: 每批次的歌词条数
    :return: 生成器，每个元素都是一批次的数据，例如:(8条,8条,8条...)
    """
    #读取文件数据
    with open('','r',encoding='utf-8') as src_f:
        # lines = [line.strip() for line in src_f.readlines()]
        #一次读取所有行
        lines = src_f.readlines()
        # print(lines)

        #计算批次总数  5批
        total_batch = math.ceil(len(lines)/batch_size)

        #for循环方式，获取到每批次的数据，放到生成器中，并返回
        for idx in range(total_batch): #idx的值:0,1,2,3,4
            # 第1批歌词，批次索引(idx=0)，歌词为:第1条 - 第8条，索引为:0 - 7
            # 第2批歌词，批次索引(idx=2)，歌词为:第9条 - 第16条，索引为:8 - 15
            # 第3批歌词，批次索引(idx=3)，歌词为:第17条 - 第24条，索引为:16 - 23
            yield lines[idx*batch_size:(idx+1)*batch_size]


dl = dataset_loader(8)
print(next(dl))
print(next(dl))

for line in dl:
    print(line)