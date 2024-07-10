class Person: #parent 
    def display(self):
        print("I am a person")

class Student(Person):   #child classs: here the attribute of the person is extracted by the child class student
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def Print(self):
        print(f"The person name is {self.name} and the age of the person is {self.age}")

emp_obj=Student("ram","20")
emp_obj.Print()
emp_obj.display()