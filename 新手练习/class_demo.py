class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.grades = {"math": 0, "Chinese": 0, "English": 0}

    def set_grade(self, course, grade):
        if course in self.grades:
            self.grades[course] = grade

    def print_grades(self):
        print(f"学生{self.name}(学号：{self.student_id})的成绩为")
        for course in self.grades:
            print(f"{course}:{self.grades[course]}")


chen = Student("小陈", "100816")
chen.set_grade("math", "92")
chen.set_grade("English", "85")
chen.set_grade("Chinese", "90")
chen.print_grades()
# 定义3个函数，第一个确定身份，第二个确定成绩，第三个打印信息
