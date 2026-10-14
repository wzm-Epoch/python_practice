"""
@File : 学生管理系统.py
@Author : 王子墨
@Description : 
@Date :2026/9/6
"""
def get_positive_age():
    """读取并返回正整数年龄；输入无效时返回 None。"""
    age_text = input("请输入年龄：").strip()
    try:
        age = int(age_text)
    except ValueError:
        print("年龄必须是正整数。")
        return None

    if age <= 0:
        print("年龄必须是正整数。")
        return None
    return age


def find_by_student_id(students, student_id):
    """按学号查找单个学生，找不到时返回 None。"""
    for student in students:
        if student["student_id"] == student_id:
            return student
    return None


def display_students(students):
    """统一显示学生信息。"""
    if not students:
        print("未找到学生信息。")
        return

    print("\n{:<12}{:<16}{:<6}".format("姓名", "学号", "年龄"))
    print("-" * 34)
    for student in students:
        print(
            "{:<12}{:<16}{:<6}".format(
                student["name"], student["student_id"], student["age"]
            )
        )



def add_student(students):
    name = input("请输入姓名：").strip()
    student_id = input("请输入学号：").strip()
    age = get_positive_age()

    if not name or not student_id:
        print("姓名和学号不能为空。")
        return
    if age is None:
        return
    if find_by_student_id(students, student_id):
        print("该学号已存在，添加失败。")
        return

    students.append({"name": name, "student_id": student_id, "age": age})
    print("学生信息添加成功。")


def delete_student(students):
    student_id = input("请输入要删除的学号：").strip()
    student = find_by_student_id(students, student_id)
    if student is None:
        print("未找到该学生信息。")
        return

    students.remove(student)
    print("学生信息删除成功。")


def update_student(students):
    student_id = input("请输入要修改的学号：").strip()
    student = find_by_student_id(students, student_id)
    if student is None:
        print("未找到该学生信息。")
        return

    name = input("请输入新姓名：").strip()
    age = get_positive_age()
    if not name:
        print("姓名不能为空。")
        return
    if age is None:
        return

    student["name"] = name
    student["age"] = age
    print("学生信息修改成功。")


def search_student(students):
    print("1. 按学号查找")
    print("2. 按姓名查找")
    choice = input("请选择查找方式：").strip()

    if choice == "1":
        student_id = input("请输入学号：").strip()
        student = find_by_student_id(students, student_id)
        display_students([student] if student else [])
    elif choice == "2":
        name = input("请输入姓名：").strip()
        matches = [student for student in students if student["name"] == name]
        display_students(matches)
    else:
        print("无效选项，请重新选择。")


def show_menu():
    print("\n===== 学生管理系统 =====")
    print("1. 添加学生信息")
    print("2. 删除学生信息")
    print("3. 修改学生信息")
    print("4. 查找学生信息")
    print("5. 退出系统")


def main():
    students = []
    actions = {
        "1": add_student,
        "2": delete_student,
        "3": update_student,
        "4": search_student,
    }

    while True:
        show_menu()
        choice = input("请选择操作：").strip()

        if choice == "5":
            print("已退出学生管理系统。")
            break

        action = actions.get(choice)
        if action:
            action(students)
        else:
            print("无效选项，请重新选择。")


if __name__ == "__main__":
    main()