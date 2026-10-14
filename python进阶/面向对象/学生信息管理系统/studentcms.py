"""
@File : studentcms.py
@Author : 王子墨
@Description : 
@Date :2026/4/23
"""

import time
from student import Student
#学生管理系统
class StudentCms(object):

    def __init__(self):
        self.stu_list = []

    @staticmethod
    def show_view():
        print("*"*23)
        print("学生管理系统")
        print("\t1.添加学生信息")
        print("\t2.删除学生信息")
        print("\t3.修改学生信息")
        print("\t4.查询单个学生信息")
        print("\t5.查询所有学生信息")
        print("\t6.保存学生信息")
        print("\t0.退出系统")
        print("*"*23)

    def add_student(self):
        name = input("请输入学生姓名:")
        gender = input("请输入学生性别:")
        age = int(input("请输入学生年龄:"))
        phone = input("请输入学生手机号:")
        desc = input("请输入学生描述信息:")
        stu = Student(name, gender, age, phone, desc)
        self.stu_list.append(stu)
        print(f"添加{name}学生信息成功!\n")

    def del_student(self):
        del_name = input("请输入要删除的学生的姓名:")
        for stu in self.stu_list :
            if stu.name == del_name:
                self.stu_list.remove(stu)
                print(f"学生{del_name}信息删除成功!\n")
                break
        else :
            print("查无此人,请检查后重新删除!\n")

    def update_student(self):
        update_name = input("请输入要修改的学生的姓名:")
        for stu in self.stu_list:
            if stu.name == update_name:
                stu.gender = input("请输入修改后的性别:")
                stu.age = int(input("请输入修改后的年龄:"))
                stu.phone = input("请输入修改后的电话:")
                stu.desc = input("请输入修改后的描述信息:")
                print(f"学生{update_name}信息修改成功!\n")
                break
        else:
            print("查无此人,请检查后重新修改!\n")


    def search_one_student(self):
        search_name = input("请输入要查找的学生的姓名:")
        for stu in self.stu_list:
            if stu.name == search_name:
                print(stu,end="\n\n")
                print(f"学生{search_name}信息查找成功!\n")
                break
        else:
            print("查无此人,请检查后重新操作!\n")

    def search_all_student(self):
        if len(self.stu_list) == 0 :
            print("暂无学生信息,请添加后查询!\n")
        else :
            for stu in self.stu_list:
                print(stu)
            print()

    def save_student(self):
        with open("./stu_data.txt", "w",encoding='utf-8') as dest_f:
            stu_dict = [stu.__dict__ for stu in self.stu_list]
            dest_f.write(str(stu_dict))

    def load_student(self):
        try:
            with open("./stu_data.txt",'r',encoding='utf-8') as src_f:
                stu_data = src_f.read()
                stu_list = eval(stu_data)
                #补充兜底
                if len(stu_list) == 0 :
                    stu_list = []
                self.stu_list = [Student(**stu_dict) for stu_dict in stu_list]
        except:
            with open("./stu_data.txt", "w", encoding='utf-8') as dest_f:
                pass

    def start(self):
        self.load_student()
        while True:
            time.sleep(1)
            StudentCms.show_view()
            input_num = input("请输入您要操作的编号:")
            if input_num == "1":
                #print("添加学生信息\n")
                self.add_student()
            elif input_num == "2":
                #print("删除学生信息\n")
                self.del_student()
            elif input_num == "3":
                #print("修改学生信息\n")
                self.update_student()
            elif input_num == "4":
                #print("查询单个学生信息\n")
                self.search_one_student()
            elif input_num == "5":
                #print("查询所有学生信息\n")
                self.search_all_student()
            elif input_num == "6":
                self.save_student()
                print("保存学生信息成功!\n")
            elif input_num == "0":
                result = input("您确定要退出吗?(Y/N) -> ")
                if result.lower() == "y":
                    self.save_student()
                    print("谢谢您的使用, 期待下次再会!")
                    break
            else :
                print("录入有误,请重新录入\n")

if __name__ == "__main__":
    cms = StudentCms()
    cms.start()

    #查看当前路径
    #import os
    #print(os.getcwd())