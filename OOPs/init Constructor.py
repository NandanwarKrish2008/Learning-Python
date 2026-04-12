class Student:
    school_name = "XYZ High School"
    def __init__(self):
        print("Whenever the new object is created I'm called automatically")
        print(self)


student1 = Student() #init method will be called by default automatically
student2 = Student()