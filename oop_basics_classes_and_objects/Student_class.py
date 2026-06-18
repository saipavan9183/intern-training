class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def study(self):
        print(f"{self.name} from Grade {self.grade} is studying for exams.")


# Student objects
s1 = Student("Pavan", 9)
s2 = Student("Surender", 8)

s1.study()
s2.study()