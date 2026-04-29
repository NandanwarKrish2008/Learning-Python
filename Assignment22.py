# Create class student that makes 3 marks and has method average()

class Student:
    def __init__(self, name, ListOfMarks):
        self.name = name
        self.ListOfMarks = ListOfMarks

    def average(self):
        sum = 0
        for eachValue in self.ListOfMarks:
            sum = sum + eachValue
        
        average = sum / 3
        print(f"Average is {average}")

student1 = Student("Krish", [99, 98, 97])

student1.average()