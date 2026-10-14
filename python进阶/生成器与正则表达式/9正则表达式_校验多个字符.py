"""
@File : 9正则表达式_校验多个字符.py
@Author : 王子墨
@Description : 
@Date :2026/8/29
"""

import re

result = re.match('.*hm.*','abchm123')  #匹配成功
result = re.match('.*hm.*','hm123') #匹配成功
result = re.match('.*hm.*','abchm') #匹配成功

result = re.match('.+hm.*','abchm') #匹配成功
result = re.match('.+hm.*','hm123') #匹配失败

result = re.match('.?hm.*','ahm123')    #匹配成功
result = re.match('.?hm.*','hm123') #匹配成功
result = re.match('.?hm.*','abchm123')  #匹配失败

result = re.match(r'\d{3}hm\w{2,5}','123hm123') #匹配成功
result = re.match(r'\d{3}hm\w{2,5}','1234hm123') #匹配失败
result = re.match(r'\d{3}hm\w{2,5}','12hm123') #匹配失败
result = re.match(r'\d{3}hm\w{2,5}','123hm12@') #匹配成功
result = re.match(r'\d{3}hm\w{2,5}','123hm1@') #匹配失败
result = re.match(r'\d{3}hm\w{2,5}','123hmabcAB') #匹配成功
result = re.match(r'\d{3}hm\w{2,5}','123hmabcAB1') #匹配成功
result = re.match(r'\d{3}hm\w{2,5}','123hmabcA@1') #匹配成功
# result = re.match(r'\d{3}hm\w{2,5}$','123hmabcA@1') #匹配失败

result = re.match(r'\d{3}hm\w{2,}','123hm1@') #匹配失败
result = re.match(r'\d{3}hm\w{2,}','123hm12@') #匹配成功
result = re.match(r'\d{3}hm\w{2,}','123hm123@') #匹配成功
result = re.match(r'\d{3,}hm\w{2,5}','123hm123@') #匹配成功
result = re.match(r'\d{3,}hm\w{2, 5}','123hm123@') #匹配失败 注意空格

print(result.group() if result else '匹配失败')