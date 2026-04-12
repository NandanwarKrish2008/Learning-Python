class Student:
    school_name = "XYZ High School"
    def __init__(self, name, course):
        # print("Whenever the new object is created I'm called automatically")
        # print(self)
        self.name = name
        self.course = course
        print(self.name)
        print(self.course)

student1 = Student("Krish", "AI/ML") #init method will be called by default automatically
# print(f"student1: {student1}")

student2 = Student("Rahul", "B.Tech")
# print("student2: ", student2)