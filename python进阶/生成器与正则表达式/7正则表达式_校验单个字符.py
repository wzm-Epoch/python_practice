"""
@File : 7正则表达式_校验单个字符.py
@Author : 王子墨
@Description : 
@Date :2026/8/29
正则表达式介绍：
概述：
    正确的，符合特定规则的字符串。
    Regular Expression，正则表达式，简称：re

细节：
1. 学正则表达式，就是学正则表达式的规则，你不用背，网上一搜一大堆。
2. 关于正则我对大家的要求是，能用我们讲的规则，看懂别人写的式子，且会简单修改即可。
3. 正则不独属于Python，像Java，JavaScript，PHP，Go等都支持。

步骤：
1. 导包
    import re
2. 正则匹配
    result = re.match('正则表达式', '要校验的字符串')   #从前往后依次匹配，只要能匹配即可
    result = re.search('正则表达式', '要校验的字符串')   #分段查找
3. 获取匹配结果。
    result.group()

正则常用的规则：
.       代表任意的 1个字符，除了 \n
\.      取消.的特殊含义，就是1个普通的字符
a       代表1个普通的字符 a
[abc][a-c]代表a,b,c中任意的1个字符
[^abc]  代表除了a,b,c外，任意的1个字符
\d      代表数字，等价于 [0‑9]
\D      代表非数字，等价于 [^0‑9]
\s      匹配空白字符,即 空格，tab键
\S      匹配非空白字符
\w      匹配非特殊字符，即a-z,A-Z,0-9,_,汉字
\W      匹配特殊字符，即非字母，非数字，非汉字，非_
|       匹配左右任意的一个表达式 或者
(ab)    将括号中字符作为一个分组 分组 从左往右数，第几个左小括号(,代表第几组
\num    引用分组num匹配到的字符串 代表 引用第几组的内容
(?p<分组名>)   设置分组
(?p=分组名)    使用分组
*       数量词，匹配前一个字符至少0次，至多无所谓
+       匹配前一个字符出现1次或者无限次，即至少有1次
?      匹配前一个字符出现1次或者0次，即要么有1次，要么没有
{m}     匹配前一个字符出现m次
{m,}    匹配前一个字符至少出现m次，至多无限次
{m,n}   匹配前一个字符出现从m到n次
^       表示开头
$       表示结尾
.*      贪婪模式
.*?      非模式
"""

import re

# result = re.match('.it','ait')  #匹配成功
# result = re.match('.it','\nit') #匹配失败
# result = re.match('.it','你it')  #匹配成功
# result = re.match('.it','你好it') #匹配失败


# result = re.match('\.it','你it')  #匹配失败
# result = re.match('\.it','.it')  #匹配成功

# result = re.match('[ahg]it','ait')  #匹配成功
# result = re.match('[ahg]it','hit')  #匹配成功
# result = re.match('[ahg]it','git')  #匹配成功
# result = re.match('[ahg]it','g it')  #匹配失败

# result = re.match('[^ahg]it','ait')  #匹配失败
# result = re.match('[^ahg]it','x it')  #匹配失败
# result = re.match('[^ahg]it','xit')  #匹配成功
# result = re.match('[^ahg]it','xitabcxyz')  #匹配成功
# result = re.match('[^ahg]it','abcxitxyz')  #匹配失败

# result = re.search('[^ahg]it','abcxitxyz')  #匹配成功

# result = re.match('[3-7]it','3it')  #匹配成功

# result = re.match('a\\dhm','a3hm')  #匹配成功
# result = re.match('a\\dhm','a03hm')  #匹配失败

# result = re.match('a\\Dhm','a!hm')  #匹配成功

# result = re.match('a\\shm','a!hm')  #匹配失败
# result = re.match('a\\shm','a\thm')  #匹配成功
# result = re.match('a\\shm','a hm')  #匹配成功
# result = re.match('a\\shm','a\nhm')  #匹配成功

# result = re.match('a\\whm','a\thm')  #匹配失败
# result = re.match('a\\whm','axhm')  #匹配成功
# result = re.match('a\\whm','a_hm')  #匹配成功
# result = re.match('a\\whm','a1hm')  #匹配成功
# result = re.match('a\\whm','a!hm')  #匹配失败
# result = re.match('a\\whm','a你hm')  #匹配成功

if result:
    print(result.group())
else:
    print("匹配失败!")