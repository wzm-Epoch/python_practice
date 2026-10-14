"""
@File : 4演示编解码.py
@Author : 王子墨
@Description : 
@Date :2026/8/25

细节:
    1.编码 = 把我们看懂的 转成 我们看不懂的
        '字符串'.encode(码表)
    2.解码 = 把我们看不懂的 转成 我们看懂的
         二进制.encode(码表)
    3.只要乱码了，愿因只有1个，编解码不同
    4.英文字母，数字，特殊符号占1个字节，中文在gbk占2个字节，在utf-8占3个字节
    5.二进制数据特殊写法，即:b'字母 数字 特殊符号'，不能写中文
"""
#编码
s1 = '黑马124axav!'

print(s1.encode())        #b'\xe9\xbb\x91\xe9\xa9\xac124axav!'
print(s1.encode('utf-8')) #b'\xe9\xbb\x91\xe9\xa9\xac124axav!'
print(s1.encode('gbk'))   #b'\xba\xda\xc2\xed124axav!'
print('-'*23)

#解码
bys = b'\xe9\xbb\x91\xe9\xa9\xac124axav!'
print(type(bys))

s2 = bys.decode()
s3 = bys.decode('utf-8')
print(s2)
print(s3)
print('-'*23)

s4 = bys.decode('gbk')
print(s4)
