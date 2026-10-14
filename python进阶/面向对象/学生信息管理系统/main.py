"""
@File : main.py
@Author : 王子墨
@Description : 该文件 用作程序的入口文件
@Date :2026/4/23
"""

from studentcms import StudentCms

#程序的主入口
if __name__ == "__main__":
    #1.创建学生管理系统对象
    cms = StudentCms()
    #2.启动程序即可
    cms.start()