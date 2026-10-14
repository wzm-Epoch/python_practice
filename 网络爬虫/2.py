import requests
from lxml import etree


def main():
    # 1. 获取页面源代码
    # 1.1定义一个变量, 来描述要爬取的页面
    url = "https://www.baidu.com/"

    headers = {
        # 更好的模拟浏览器
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36 Edg/133.0.0.0'
    }

    # 1.2使用requests模块来获取网址的源代码
    r = requests.get(url, headers=headers).text #发送 GET 请求访问百度 拿到网页文本形式的 HTML 源代码，赋值给变量r

    ret = etree.HTML(r)  # 把字符串形式的 HTML 源码，解析成 etree 的 HTML 对象，之后就可以用 XPath 语法查找页面元素

    # 先拿所有的大标签
    li_list = ret.xpath('//ul[@id="hotsearch-content-wrapper"]/li')  # [li, li, li, li....li] 找到页面中 id="hotsearch-content-wrapper" 的 ul 标签

    for li in li_list:
        # 热搜内容
        content = li.xpath('.//span[@class="title-content-title"]/text()')[0] #找到 class 为title-content-title的 span 标签，里面存放热搜文字
        print(content)

if __name__ == '__main__':
    main()
