"""
@File : 8正则替换.py
@Author : 王子墨
@Description : 
@Date :2026/8/29

    result = re.compile('正则表达式').sub(替换后的内容，要被替换的字符串)

"""

import re

s = '开心你就大声笑，哈哈，呵呵，嘿嘿，嘻嘻，桀桀桀，啦啦啦'

#                       正则规则
result = re.compile('哈|呵|嘿|嘻|桀').sub('^',s)

print(result)
print("-"*23)

result = re.sub('哈|呵|嘿|嘻|桀','*',s)
result = re.sub('[哈呵嘿嘻桀]','*',s)
print(result)