import pandas as pd
# 1. 读取成绩文件
file_name = r"C:\Users\wzmam\Desktop\学生成绩2.csv"

try:
    df = pd.read_csv(file_name, encoding='gbk')
except:
    df = pd.read_csv(file_name)

print("成绩文件读取成功！")

print("*" * 23)
print("    学生管理系统")
print("\t1.添加学生信息")
print("\t2.统计")
print("\t3.排序")
print("\t4.查询")
print("\t5.退出")
print("*"*23)
# 2. 添加宿舍同学成绩
def addition():
    global df
    n = int(input("请输入需要添加的人数："))

    for i in range(n):
        print(f"\n输入第{i+1}位同学信息")

        sid = input("学号：")
        name = input("姓名：")
        score = float(input("成绩："))

        new_student = pd.DataFrame({
            "学号":[sid],
            "姓名":[name],
            "成绩":[score]
        })

        df = pd.concat([df,new_student],ignore_index=True)

    print("\n宿舍同学成绩添加成功！")

    # 保存更新后的数据
    df.to_csv(file_name,index=False,encoding='gbk')

# 3. 成绩统计
def statistics():
    avg_score = df["成绩"].mean()
    max_score = df["成绩"].max()
    min_score = df["成绩"].min()

    excellent = (df["成绩"] >= 90).sum()
    good = ((df["成绩"] >= 80) & (df["成绩"] < 90)).sum()
    medium = ((df["成绩"] >= 70) & (df["成绩"] < 80)).sum()
    pass_num = ((df["成绩"] >= 60) & (df["成绩"] < 70)).sum()
    fail = (df["成绩"] < 60).sum()

    result = f"""
    ========== 成绩统计 ==========
    学生总人数：{len(df)}
    
    平均成绩：{avg_score:.2f}
    最高成绩：{max_score}
    最低成绩：{min_score}
    
    优秀(>=90)：{excellent}人
    良好(80~89)：{good}人
    中等(70~79)：{medium}人
    及格(60~69)：{pass_num}人
    不及格(<60)：{fail}人
    """

    # 屏幕显示
    print(result)

# 写入文件
    with open(".venv/statictic.txt", "w", encoding="utf-8") as f:
        f.write(result)

    print("统计结果已保存到 statictic.txt")

 # 4. 排序并显示前10名
def sort():
    print("\n========== 前10名 ==========")

    top10 = df.sort_values(by="成绩",ascending=False).head(10)

    print(top10.to_string(index=False))

# 5. 学号查找
def search():
    search_id = input("\n请输入要查询的学号：")

    # 按成绩排序计算名次
    rank_df = df.sort_values(by="成绩",ascending=False).reset_index(drop=True)
    rank_df["班级名次"] = rank_df.index + 1

    student = rank_df[rank_df["学号"] == search_id]

    if len(student) > 0:
        print("\n查询结果：")

        print("学号：",student.iloc[0]["学号"])
        print("姓名：",student.iloc[0]["姓名"])
        print("班级名次：",student.iloc[0]["班级名次"])
        print("成绩：",student.iloc[0]["成绩"])
    else:
        print("未找到该学号！")

def start():
    while True:
        input_num = input("请输入您要操作的编号:")
        if input_num == "1":
            addition()
        elif input_num == "2":
            statistics()
        elif input_num == "3":
            sort()
        elif input_num == "4":
            search()
        elif input_num == "5":
            print("退出学生信息管理系统!")
            break
        else:
            printf("输入错误!")
if __name__ == '__main__':
    start()

