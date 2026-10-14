"""
@File : 4.py
@Author : 王子墨
@Description : 
@Date :2026/9/22
"""
# 导入 requests 库，用于发送网络请求
import requests

# 设置请求头，模拟浏览器访问
headers = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/152.0.0.0 Safari/537.36 Edg/152.0.0.0"
    )
}

# 豆瓣电影 Top 250 第一页的网址
url = "https://movie.douban.com/top250?start=0"

# 向指定网址发送 GET 请求
# headers 用于携带上面设置的浏览器标识
# timeout=10 表示最多等待服务器响应 10 秒
result = requests.get(url, headers=headers, timeout=10)


# 判断请求是否成功
# result.ok 为 True，一般表示 HTTP 状态码小于 400
if result.ok:
    # 获取服务器返回的网页源代码
    html = result.text
    # 输出完整的 HTML 网页源代码
    print(html)
else:
    # 请求失败时输出提示和 HTTP 状态码
    print(f"请求失败！状态码：{result.status_code}")