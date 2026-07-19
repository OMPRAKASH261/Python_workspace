# Our first Program start 

print("hello \nworld", "good morning")
print("with \n python")

# Variables -> containrs

_name = "vijay"
age = 24
PI = 3.14

print(_name, age, PI)
print("my age is:", age)

# Data types

print(type(_name))
print(type(PI))

num = 4
isPrime = True
print(type(isPrime))

# style gudie -> snake_case
tot_price = 100
full_name = "rahul"
# -> camel case
totprice = 100
# -> pascal case
TotPrice = 100

# Operators
# -> arithmetic
a = 9
b = 5
print(a+b)
print(a-b)
print(a*b)
print(a/b) #division
print(a%b) #modulo
print(a**b) #power

# ->relational
a = 5
b = 3
c = 5

print(a>b)
print(a != c)
print(a == c)
print(a >= b)

# -> assignment
a = 6
a = a + 2
a += 1 # a = a + 5
a -= 5 # a = a- 5
a *= 2 # a = a*2
a /= 4 
print(a)

# -> relational
var = False
print(not var)
print(not (5 > 8))
print((5 > 3) and (3 > 2))
print((5 > 3) and (1 > 2))
print((5 > 3) or (1 > 2))
print((2 > 3) or (1 > 2))

# Type conversion
# -> implicit conversion
ans1 = 5 + 10.0
print(ans1, type(ans1))
# -> explicit casting
ans2 = int(5 + 10.0)
print(ans2, type(ans2))
val = int("123")
print(type(val))
val = bool(-10)  # 0(zero) always False, and non-zero(even val is negative or poistive) always True
print(val, type(val))

# User input
a = input("enter value of a: ")
print(a)
username = input("enter your name: ")
print("welcome", username)

# -> sum of 2 nums
# a = input("enter a: ")
# b = input("enter b: ")
# sum = a + b
# print(sum)  # a and b are string then they don't add instead give ab.

a = int(input("enter a: "))
b = int(input("enter b: "))
sum = a + b
print(sum)  # a and b are string then they don't add instead give ab.


# conditional statements
# -> if
age = 34
if age >= 18:
    print("you can vote")
    
# # -> else
age = int(input("enter age: "))
if age >= 18:
    print("you can vote")
    print("you can drive")
else:
    print("you can't vote")

# -> elif
color = input("enter color: ")
if color == "red":
    print("stop")
elif color == "green":
    print("go")
elif color == "yellow":
    print("wait")
else:
    print("wrong color for traffic lights")


# -> persenoality check
age = int(input("enter age: "))

if (age < 13):
    print("child")
elif (age >= 13 and age < 18):
    print("teenager")
else:
    print("adult")

# -> login and password check (user authentcation)
username = input("enter username: ")
password = input("enter password: ")

if (username == "admin" and password == "pass"):
    print("LOGIN Successful!")
elif (username != "admin"):
    print("Wrong Username")
else:
    print("Wrong Password")
    
# -> check multiple or not
n = int(input("enter num: "))

if (n % 5 == 0):
    print("multiple of 5")
else:
    print("not multiple of 5")
    
# Nesting
username = input("enter username: ")
password = input("enter password: ")

if (username == "admin" and password == "pass"):
    print("successs")
else:
    if (username != "admin"):
        print("wrong username")
    else:
        print("wrong password")
        
# Match case
color = input("enter color: ")
match color:
    case "Green":
        print("go")
    case "Yellow":
        print("look")
    case "Red":
        print("stop")
    case _:
        print("wrong color!")

# loops
# # -> infiinite loops
# while True:
#     print("hello world")
    
# -> finite loop

count = 1 #iterator/counter variable
while (count <= 5):
    print("hello world", count)
    count += 1

print("after loop, count =", count)

# -> 1 to 5
i = 1  # iterator
while (i <= 5):
    print(i)
    i += 1

# -> 5 to 1
i = 5
while (i >= 1):
    print(i)
    i -= 1


# mulitplication table of any num

n = int(input("enter num: "))
# i = 1
# while (i <= 10):
#     print(n * i)
#     i += 1

# -> if start form 0
i = 0
while (i < 10):
    print(n * (i+1))
    i += 1

# -> break
i = 1
while (i <= 10):
    if (i % 6 == 0):
        break
    print(i)
    i += 1
print("outside loop now......")

# -> continue
i = 1
while (i <= 10):
    if (i % 3 == 0):
        i += 1
        continue # skip multiple of 3
    print(i)
    i += 1
print("outside loop.....")

# For Loop
string = "hello"
# in => membership operator (check presence)
for var in string:
    print(var)

# check o is in string or not   
string = "hello"
if 'o' in string:
    print("o exists in string")

# print AI 5 times   
for i in range(5):  # 0 to n-1
    # print(i)
    print("AI")

# count the no of words   
word = "artificial intelligence"
count = 0
for ch in word:
    if(ch == 'i'):
        count += 1
print("count of i =", count)

# Range() funciion
for i in range(5):
    print(i)
for i in range(1, 6):
    print(i)
for i in range(1, 10, 2): # odd no
    print(i)
for i in range(2, 11, 2): # even no
    print(i)

# Funtions
def hello(): #fnx definiton
    print("hello")
    print("from python")
hello()  #fnx call
hello()  #fnx call

# funciion definition
def sum(a, b): #parameters
    s = a + b
    return s

print(sum(3, 4)) #fnx call  (3, 4) are arguments

# non-defaut variabe always in start, default variable can't in start
def sum(a, b = 1):
    return a + b

print(sum(5))
print(sum(4, 5))

# lambda function
sum = lambda a,b: a+b
print(sum(5,6))

avg = lambda a,b: (a+b)/2
print(avg(4,5))


# Strings -> immutable cant we change
word = "python"
print(len(word))

word1 = "I love"
word2 = "python"
word3 = "programing"
sentence = word1 + " " + word3
print(word1 + " " + word2) #concatenate
print(sentence)

word = "hello" 
print(word[2])  # indexing

word = "Delhi"
for ch in word:
    print(ch)

# slicing
word = "I study from ApnaCollege"
print(word[13:25])
print(word[17:])
print(word[13:len(word)])
print(word[:len(word)])
print(word[:])

word = "Python"
print(word[-4:-2])

# Formatting
a = 5
b = 10
sum = a + b
# normal formatting
print("sum is {}".format(sum)) #normal format
print("language is {}".format("python"))
print("sum of {} & {} is {}".format(a, b, sum))

# index based formatting
print("sum of {1} & {0} is {2}".format(a, b, sum))

# value based formatting -> resuse the variable
print("values of vars {a} & {b}".format(a=5, b=10))

# f-strings
a = 5
b = 10

print(f"sum of {a} & {b} is {a + b}")
print(f"avg of {a} & {b} is {(a + b)/2}")


# Lists
marks = [99, 89, 100, 35, 93, "abc", 49.03]
print(marks)
print(len(marks))
print(marks[2])
marks[2] = 79
print(marks)

# -> Slicing in list
marks = [99, 89, 100, 35, 93, "abc", 49.03]
print(marks[0:5]) #indexing
print(marks[:5])
print(marks[5:len(marks)])
print(marks[5:])
print(marks[-5:-2]) #negative indexing
print(marks[: : -1]) #Reverse list


# Method->function in list
nums = [1, 2, 3]
nums.append(4)
print(nums)
nums.insert(2, 10)
print(nums)
nums.sort()
print(nums)
nums.sort(reverse=True)
print(nums)
nums.reverse()
print(nums)

# loops
nums = [1, 2, 3, 5, 19, 7]
for val in nums:
    print(val)
    
    
nums = [1, 2, 3, 10, 4] # linear search
x = 10
idx = 0
for val in nums:
    if(val == x):
        print(f"{x} found at idx={idx}")
        break
    idx += 1
    
    
# Tuples -> immutable sequence of values
tup = (1, 2, 3, 4, 5, "abc", 3.14)
print(tup)
print(type(tup))
print(len(tup))
print(tup[2])

tup = (4)
tup1 = (4,)
tup2 = ("abc")
tup3 = ("abc",)
print(type(tup))
print(type(tup1))
print(type(tup2))
print(type(tup3))

tup = (1, 2, 3, 4, 5)
print(tup[:3])
 
tup = (1, 2, 3, 4, 6) # loop
for val in tup:
    print(val)
    
tup = (1, 2, 3, 4, 5)
sum = 0
for val in tup:
    sum += val
    
print(f"sum of vals is {sum}")


# Methods
tup = (1, 2, 2, 3, 2, 4)
print(tup.index(2))  #index -> returns 1st occurence idx
print(tup.count(2))  #count -> counts total occurences

# Dictionary
info = {
    "name": "Omprakash",
    "cgpa": 9.0,
    "subjects": ["math", "science"],
    3.14: "PI"
}
print(type(info))
print(info["name"])
print(info[3.14])
info["cgpa"] = 9.4
print(info["cgpa"])

# -> Method
info = {
    "name": "Omprakash",
    "cgpa": 9.0,
    "subjects": ["math", "science"],
    3.14: "PI"
}
print(info.keys())
dict_keys = info.keys()
dict_keys1 = list(info.keys()) #convert into list
print(dict_keys)
print(dict_keys1)
print(type(dict_keys1))

dict_vals = list(info.values())
dict_vals1 = info.values()
print(dict_vals)
print(dict_vals1)

print(info.items())

print(info.get("cgpa"))
print(info.get("cgpa2"))
print("End of code")

# print(info["cgpa2"]) #wrong key -> give error
# print("End of code")

info.update({
    "city": "Delhi"
})
print(info)

# sets
s = {1, 2, 2, 2, 3}
print(s)
print(type(s))
print(len(s))


empty_set = {}
print(type(empty_set))
empty_set = set()
print(type(empty_set))

s.add(6)
print(s)
s.remove(1)
print(s)
s.clear()
print(s)
s = {1, 2, 3}
print(s)
s.pop()
print(s)

s1 = {1, 2, 3, 4, 5}
s2 = {4, 5, 6, 8, 10}
print(s1.union(s2))
print(s1.intersection(s2))


# OOP (Object oriented Programming)
class Student:
    subject = "Python"
    college = "ABC"
    year = "4th year"
stu1 = Student()
stu2 = Student()
print(stu1)
print(type(stu1))
print(stu1.subject, stu1.college, stu1.year)
print(stu2.subject, stu2.college, stu2.year)


# -> Constructor
class Student:
    def __init__(self):
        print("constructor was called...")
    
stu1 = Student()
stu2 = Student()
stu3 = Student()

## -> Type - (default, parameterized)
class Student:
    # in python we cannot create multiple contrutor in one class.
    def __init__(self):  # default
        print("obj is being construted..")
        
    def __init__(self, name, cgpa):  # Parameterized
        self.name = name
        self.cgpa = cgpa

    def get_cgpa(self):  
        return self.cgpa
stu1 = Student("Rahul", 9.0)
stu2 = Student("Uravashi", 8.4)
stu3 = Student("Shardha", 9.2)

print(stu1.name, stu1.cgpa)
print(stu2.name)
print(stu3.cgpa)


print(stu1.get_cgpa())
print(f"{stu1.name} has cgpa = {stu1.get_cgpa()}")

# -> Attributes - (class, instance)
class Student:
    college_name = "ABC college" #class
    PI = 3.1

    def __init__(self, name, gpa):
        self.name = name  # instance
        self.gpa = gpa
        self.PI = 3.14
     
stu1 = Student("Rahul", 9.3)   

print(stu1.name)
# print(Student.name) # give error
print(Student.college_name)
print(stu1.college_name)

print(stu1.PI)
print(Student.PI)

## -> Methods
class Laptop:
    storage_type = "ssd"
    
    def __init__(self, RAM, storage):
        self.RAM = RAM
        self.storage = storage
    
    @classmethod
    def get_storage_type(cls):
        print(f"storage type = {cls.storage_type}")
        
    def get_info(self):  # instance method
        print(f"laptop has {self.RAM} RAM & {self.storage} {self.storage_type}")
        
    @staticmethod
    def calc_discount(price, discount):
        final_price = price - (discount * price/100)
        print(f"discounted price = {final_price}")

l1 = Laptop("16gb", "512gb")

# -> instance method
l1.get_info()
# ->class method
Laptop.get_storage_type()
l1.get_storage_type()
# -> Static method
l1.calc_discount(40000, 10)


## OOP Pilars
# -> Encapsulation
class BankAccount:
    def __init__(self, name, balance):
        self.name = name  #public
        self.__balance = balance #private - data mangling
        
    def get_balance(self):  #getter
        return self.__balance
    
    def set_balance(self, newBalance):  #setter
        self.__balance = newBalance
        
acc1 = BankAccount("Rahul Kumar", 10_000)

acc1.set_balance(200_000)
print(acc1.name, acc1.get_balance())
print(acc1.name, acc1._BankAccount__balance) #private data can access directly


## -> Inheritance

# -> Single level inheritance
class Employee:
    start_time = "10am"
    end_time = "6pm"
    
    def change_time(self, new_end_time):
        self.end_time = new_end_time

class Teacher(Employee):
    def __init__(self, subject):
        self.subject = subject
        
class AdminStaff(Employee):
    def __init__(self, role):
        self.role = role
    
t1 = Teacher("Math")

print(t1.subject, t1.start_time, t1.end_time)

t1.change_time("5pm")
print(t1.subject, t1.start_time, t1.end_time)

staff1 = AdminStaff("manger")
print(staff1.role, staff1.start_time, staff1.end_time)
    
    
# -> Multilevel Inheritance
class Employee:
    start_time = "10am"
    end_time = "6pm"

class AdminStaff(Employee):
    def __init__(self, role):
        self.role = role

class Accountant(AdminStaff):
    def __init__(self, salary, role):
        super().__init__(role)
        self.salary = salary
        
acc1 = Accountant(25_000, "CA")
print(acc1.role, acc1.salary, acc1.start_time, acc1.end_time)


# -> Multiple inheritance
class Teacher:
    def __init__(self, salary):
        self.salary = salary

class Student:
    def __init__(self, gpa):
        self.gpa = gpa

class TA(Teacher, Student):
    def __init__(self, salary, gpa, name):
        super().__init__(salary)
        Student.__init__(self, gpa)
        self.name = name

ta1 = TA(15_000, 9.3, "Omprakash")
print(ta1.name, ta1.gpa, ta1.salary)


## -> Abstraction
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass
    
class Lion(Animal):
    def make_sound(self):
        print("Roar!")
        
class Cow(Animal):
    def make_sound(self):
        print("Moo!")

lion = Lion()
lion.make_sound()

cow = Cow()
cow.make_sound()


## -> Ploymorphism
#-> Function Overrriding
class Employee:
    def get_designation(self):
        print("designation = Empoyee")
        
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