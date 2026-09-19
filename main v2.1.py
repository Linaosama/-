# 学生成绩管理系统 v2.0
# 运行方式：python main.py，按菜单输入数字操作
# 数据结构：student 是列表，每个元素是一个字典
# 即 {"id": "学号(字符串)", "name": "姓名", "scores": {"科目": 分数(可包含多个科目)}}
def search_students(keyword, students):
    results = []
    for stu in students:
        if stu["id"] == keyword or stu["name"] == keyword:
            results.append(stu)
    return results

def ask_yes_no(prompt):
    while True:
        answer = input(prompt).strip()  #判断是否
        if answer == "是":
            return True
        elif answer == "否":
            return False
        else:
            print("输入无效，请输入'是'或'否'！")

def add_student_action(students):  # 添加学生
    text = input("请输入学号和姓名（用空格或逗号分隔）：")
    parts = text.replace(",", " ").replace("，", " ").split()
    if len(parts) != 2:
        print("格式错误，请按格式输入")
        return
    student_number = parts[0]
    name = parts[1]

    if len(search_students(student_number, students)) > 0:
        print("学生已存在，请重新输入！")
    else:
        students.append({"id": student_number, "name": name, "scores": {}})
        print("添加成功")

def record_score_action(students):  # 录入成绩
    student_num = input("请输入学生的学号：")

    found_student = search_students(student_num, students)
    if len(found_student) == 0:
        print("没有找到这个学生")
        return

    found_student = found_student[0]  # 取出唯一的学生字典

    subject = input("请输入科目：").strip()
    if subject in found_student["scores"]:
        print("这个科目的成绩已经录入，不能重复录入！")
        return

    score = int(input("请输入成绩："))
    if 0 <= score <= 150:
        found_student["scores"][subject] = score
        print("成绩录入成功")
        return
    print("成绩无效，请重新输入！")

def query_student_action(students):  # 查询学生
    keyword = input("请输入要查询学生的学号或姓名:").strip()

    results = search_students(keyword, students)

    if len(results) == 0:
        print("没有找到这个学生")
        return

    if len(results) > 1:
        print(f"提示：共检索到 {len(results)} 位同名学生：")

    for target in results:  # 先打印身份信息，没成绩也能看清学号和姓名
        print(f"学号：{target['id']}  姓名：{target['name']}")

        if len(target["scores"]) == 0:
            print("  暂无成绩")
        else:
            print(f"  {'科目':<10}{'分数':<6}")
            print("  " + "-" * 16)

            total_scores = 0
            for subject, score in target["scores"].items():
                print(f"  {subject:<10}{score:<6}")
                total_scores += score

            print(f"  {'总分':<10}{total_scores:<6}")
        print("=" * 25)

def del_student_action(students):  # 删除学生
    found_id = input("请输入要删除学生的学号:")

    target = search_students(found_id, students)

    if len(target) == 0:
        print("没有找到这个学生")
        return

    target = target[0]  # 取出要删除的学生字典

    if ask_yes_no(f"确定删除 {target['name']} 吗？(是/否)："):
        students.remove(target)
        print("删除学生成功！")
        return
    print(f"已取消删除学生:{target['name']}")

def show_all_students_action(students):  # 显示全部学生
    if len(students) == 0:
        print("暂无学生")
        return

    subjects = []  # 找出所有科目
    for stu in students:
        for subject in stu["scores"]:
            if subject not in subjects:
                subjects.append(subject)

    print(f"{'姓名':<10}{'学号':<15}", end="")  # 打印表头

    for subject in subjects:
        print(f"{subject:<10}", end="")

    print()
    print("-" * (25 + len(subjects) * 10))

    for stu in students:  # 每个学生打印一行
        print(f"{stu['name']:<10}{stu['id']:<15}", end="")
        for subject in subjects:
            if subject in stu["scores"]:
                print(f"{stu['scores'][subject]:<10}", end="")
            else:
                print(f"{'-':<10}", end="")
        print()

def main():
    students = []  # 数据列表放进 main 局部作用域，为了代码的安全性和隔离性

    while True:
        print("===== 学生成绩管理系统 =====")
        print("1.添加学生  2.录入成绩  3.查询学生")
        print("4.显示全部  5.删除学生  0.退出")
        choice = input("请选择：").strip()

        if choice == "1":
            add_student_action(students)
        elif choice == "2":
            record_score_action(students)
        elif choice == "3":
            query_student_action(students)
        elif choice == "4":
            show_all_students_action(students)
        elif choice == "5":
            del_student_action(students)
        elif choice == "0":
            print("感谢使用，再见！")
            break
        else:
            print("无效输入，请选择 0-5 之间的数字")

if __name__ == "__main__":  # 模块被 import 时不自动运行
    main()