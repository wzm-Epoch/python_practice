"""
@File : 3.py
@Author : 王子墨
@Description : 
@Date :2026/9/22
"""



import requests
from bs4 import BeautifulSoup
import time

# 设置请求头，模拟浏览器访问，降低被网站直接拦截的概率
headers = {"User-Agent": ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) ""AppleWebKit/537.36 (KHTML, like Gecko) ""Chrome/152.0.0.0 Safari/537.36 Edg/152.0.0.0")}

# 用于显示当前页码
page_num = 1

# 豆瓣电影 Top 250 每页显示 25 部电影
# start 参数依次为：0、25、50……225，共 10 页
for start_num in range(0, 250, 25):

    print(f"{'-' * 13}第{page_num}页{'-' * 13}")
    page_num += 1

    url = f"https://movie.douban.com/top250?start={start_num}"

    # 向豆瓣服务器发送 GET 请求
    result = requests.get(url,headers=headers)

    # 判断请求是否成功
    if result.ok:

        # 获取网页源代码
        html = result.text

        # 将 HTML 文本解析成 BeautifulSoup 对象
        soup = BeautifulSoup(html, "html.parser")

        # 查找所有 class="title" 的 span 标签
        all_titles = soup.find_all("span",attrs={"class": "title"})

        # 遍历找到的标题标签
        for title in all_titles:
            # 提取标签中的文字，并去除首尾空白字符
            title_string = title.get_text(strip=True)

            # 外文标题通常以“/”开头，只输出不含“/”的中文标题
            if "/" not in title_string:
                print(title_string)


    else:
        # 请求失败时输出 HTTP 状态码
        print(f"请求失败！状态码：{result.status_code}")
    time.sleep(0.3)