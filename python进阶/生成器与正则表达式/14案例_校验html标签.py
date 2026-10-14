"""
@File : 14案例_校验html标签.py
@Author : 王子墨
@Description : 
@Date :2026/9/3
"""

import re

# html_s = '<html>我是html页面</html>'

# result = re.match('<[a-zA-Z]{4}>.*</[a-zA-Z]{4}>',html_s)
# result = re.match(r'<([a-zA-Z]{4})>.*</\1>',html_s)

# if result:
#     print(result.group())
# else:
#     print("未匹配!")

html_s = '<html><h1>我是html页面</h1></html>' #字母数:1-4 标题标签:1-6
# result = re.match(r'<([a-zA-Z]{1,4})><(h[1-6])>.*</\2></\1>',html_s)
result = re.match(r'<(?P<A>[a-zA-Z]{1,4})><(?P<B>h[1-6])>.*</(?P=B)></(?P=A)>',html_s)
if result:
    print(result.group())
else:
    print("未匹配!")