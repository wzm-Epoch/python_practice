"""
@File : 12案例_校验邮箱.py
@Author : 王子墨
@Description : 
@Date :2026/8/30
"""

import re

email = '279860263@qq.com'

#字母数字_4-20 @ 域名.com
result = re.match(r'^[a-zA-Z_0-9]{4,20}@(163|126|qq)\.com$',email)

# print(result.group() if result else '邮箱不合法!')
if result:
    print(f'合法邮箱为:{result.group()}')
    # print(f'合法邮箱为:{result.group(0)}') #整个匹配到的结果
    # print(f'合法邮箱为:{result.group(1)}')
else:
    print('邮箱不合法!')
