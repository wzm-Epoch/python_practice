"""
@File : 11正则表达式_校验分组.py
@Author : 王子墨
@Description : 
@Date :2026/8/29
"""

import re

#匹配apple,pear
fruits = ['apple','banana','orange','pear']

for fruit in fruits:

    if  re.match('apple|pear',fruit):
        print(f'喜欢吃:{fruit}')

    else:
        print(f'不喜欢吃:{fruit}')