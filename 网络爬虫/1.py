"""
@File : 1.py
@Author : 王子墨
@Description : 
@Date :2026/9/1
"""

import requests
from bs4 import BeautifulSoup
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/152.0.0.0 Safari/537.36 Edg/152.0.0.0"}
num=1
for start_num in range(0,250,25):
    print(f"{'-'*13}第{num}页{'-'*13}")
    num+=1
    result = requests.get(f'https://movie.douban.com/top250?start={start_num}',headers=headers)
    # result = requests.get('http://books.toscrape.com/',headers=headers)
    html = result.text

    # print(result)
    # print(result.status_code)
    if result.ok:
        soup = BeautifulSoup(html, 'html.parser')
        # print(soup.p)
        # print(soup.img)
        # all_prices = soup.find_all("p",attrs={"class":"price_color"})
        # for price in all_prices:
        #     print(price.string[2:])

        # all_titles = soup.find_all("h3")
        # for title in all_titles:
            # all_links = title.find_all("a")
            # for link in all_links:
            #     print(link.string)
            # link = title.find("a")
            # print(link.string)

        all_titles = soup.find_all("span",attrs={"class":"title"})
        for title in all_titles:
            title_string = title.string
            if "/" not in title_string:
                print(title_string)

    else:
        print("请求失败!")