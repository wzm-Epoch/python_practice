"""
@File : 13案例_提取QQ号.py
@Author : 王子墨
@Description : 
@Date :2026/8/30
"""

import re

#数据格式为: qq:数字 从中提取 qq文本 和 qq号

s = 'qq:279860263'

result = re.match(r'^(qq):(\d{5,12})$',s)

# print(result.group() if result else '邮箱不合法!')
if result:
    # print(f'{result.group(1)}:{result.group(2)}')
    # print(result.group(0))
    print(result.group(1))
    print(result.group(2))
else:
    print('未匹配')

