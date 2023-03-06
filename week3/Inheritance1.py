class Person():
    
    def __init__(self, name, id):
        self.name = name
        self.id = id
        
    def display(self):
        print(self.name, self.id)
        
emp = Person("Arnur", 102)
emp.display()

class Employee(Person):
    def print_emp(self):
        print('Eployee class called')
    
employee_details = Employee("Bakhyt", 103)
employee_details.display()
employee_details.print_emp()
        