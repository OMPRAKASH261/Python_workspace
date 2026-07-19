## -> Ploymorphism
#-> Function Overrriding
class Employee:
    def get_designation(self):
        print("designation = Employee")
        
class Teacher(Employee):
    def get_designation(self):
        print("designation = Teacher")
        
t1 = Teacher()
t1.get_designation()


#-> Duck Typing
class Teacher():
    def get_designation(self):
        print("designation = Teacher")

class Accountant():
    def get_designation(self):
        print("designation = Accountant")
        
t1 = Teacher()
t1.get_designation()

acc1 = Accountant()
acc1.get_designation()