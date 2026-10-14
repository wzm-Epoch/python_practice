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
    r = requests.get(url, headers=headers).text

    ret = etree.HTML(r)  # ret仍然是源代码, 只不过它是xml类型的源代码

    # 先拿所有的大标签
    li_list = ret.xpath('//ul[@id="hotsearch-content-wrapper"]/li')  # [li, li, li, li....li]

    for li in li_list:
        # 热搜内容
        # content = li.xpath('./a/span[2]/text()')[0]
        # content = li.xpath('.//span[2]/text()')[0]
        content = li.xpath('.//span[@class="title-content-title"]/text()')[0]
        print(content)


if __name__ == '__main__':
    main()
