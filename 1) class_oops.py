class student:
    def stud(self):
        self.name=input()
        self.rollno=int(input())
        self.percentage=int(input())
    def display(self):
        print("Name:",self.name)
        print("Roll no:",self.rollno)
        print("Percentage:",self.percentage)


p1=student()
p1.stud()
p1.display()
