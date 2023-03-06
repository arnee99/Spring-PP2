# Python program to demonstrate
# hybrid inheritance

class School:
    def __init__(self, schoolName):
        self.schoolName = schoolName
    def function1(self):
        print("This function is in school.")
        
class Student1(School):
    def __init__(self, studentName1, schoolName):
        self.studentName1 = studentName1
        super().__init__(schoolName)
        
    def function2(self):
        print("This function is in Student #1.")
        
class Student2(School):
    def __init__(self, studentName2, schoolName):
        self.studentName2 = studentName2
        super().__init__(schoolName)
    
    def function3(self):
        print("This function is in Student #2.")
        
class Student3(Student1, Student2):
    def __init__(self, studentName1, studentName2, 
                studentName3, schoolName):
        self.studentName3 = studentName3
        super(Student3, self).__init__(studentName1, schoolName)
    
    def function4(self):
        print("This function is student #3.")
        
        
obj = Student3("S1", "S2", "S3", "SomeSchool")
obj.function1()
obj.function2()
obj.function4()