class Student:
    institute = "Alvas"
    student_count = 0

    def __init__(self, roll_no, name, section, marks):
        self.roll_no = roll_no
        self.name = name
        self.section = section
        self.marks = marks


    def get_stu_data(self):
        print("Student information : ", self.roll_no, self.name, self.section, self.marks)       

