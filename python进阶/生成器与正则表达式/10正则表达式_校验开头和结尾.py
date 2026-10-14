"""
@File : 10正则表达式_校验开头和结尾.py
@Author : 王子墨
@Description : 
@Date :2026/8/29
"""

import re

#必须以数字开头
result = re.match(r'\d+.*','abc123xyz')    #匹配失败
result = re.search(r'\d+.*','abc123xyz')   #匹配成功

result = re.match(r'^\d+.*','abc123xyz')  #匹配失败
result = re.search(r'^\d+.*','abc123xyz')  #匹配失败

#必须以数字开头,以任意的3个字母结尾
result = re.match(r'^\d+.*[a-zA-Z]{3}',' 123abcxyz')    #匹配成功
result = re.match(r'^\d+.*[a-zA-Z]{3}',' 123abcxyz12')    #匹配失败
result = re.match(r'^\d+.*[a-zA-Z]{3}$',' 123abcxyz')    #匹配成功
result = re.match(r'^\d+.*[a-zA-Z]{3}$','123abcxyz12')  #匹配失败

#校验手机号 1.长度必须是11位 2.必须是纯数字 3.第1位数字必须是1 4.第2位数字可以是 3-9
result = re.search(r'^1[3-9]\d{9}','13919541007a')  #匹配成功 不规范
result = re.search(r'^1[3-9]\d{9}$','13919541007a')  #匹配失败
result = re.search(r'^1[3-9]\d{9}$','13919541007')  #匹配成功

print(result.group() if result else '匹配失败')

