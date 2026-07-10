# Our first Program start 

# print("hello \nworld", "good morning")
# print("with \n python")

# # Variables -> containrs

# _name = "vijay"
# age = 24
# PI = 3.14

# print(_name, age, PI)
# print("my age is:", age)

# # Data types

# print(type(_name))
# print(type(PI))

# num = 4
# isPrime = True
# print(type(isPrime))

# # style gudie -> snake_case
# tot_price = 100
# full_name = "rahul"
# # -> camel case
# totprice = 100
# # -> pascal case
# TotPrice = 100

# # Operators
# # -> arithmetic
# a = 9
# b = 5
# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b) #division
# print(a%b) #modulo
# print(a**b) #power

# # ->relational
# a = 5
# b = 3
# c = 5

# print(a>b)
# print(a != c)
# print(a == c)
# print(a >= b)

# # -> assignment
# a = 6
# a = a + 2
# a += 1 # a = a + 5
# a -= 5 # a = a- 5
# a *= 2 # a = a*2
# a /= 4 
# print(a)

# # -> relational
# var = False
# print(not var)
# print(not (5 > 8))
# print((5 > 3) and (3 > 2))
# print((5 > 3) and (1 > 2))
# print((5 > 3) or (1 > 2))
# print((2 > 3) or (1 > 2))

# # Type conversion
# # -> implicit conversion
# ans1 = 5 + 10.0
# print(ans1, type(ans1))
# # -> explicit casting
# ans2 = int(5 + 10.0)
# print(ans2, type(ans2))
# val = int("123")
# print(type(val))
# val = bool(-10)  # 0(zero) always False, and non-zero(even val is negative or poistive) always True
# print(val, type(val))

# # User input
# a = input("enter value of a: ")
# print(a)
# username = input("enter your name: ")
# print("welcome", username)

# # -> sum of 2 nums
# # a = input("enter a: ")
# # b = input("enter b: ")
# # sum = a + b
# # print(sum)  # a and b are string then they don't add instead give ab.

# a = int(input("enter a: "))
# b = int(input("enter b: "))
# sum = a + b
# print(sum)  # a and b are string then they don't add instead give ab.


# # conditional statements
# # -> if
# age = 34
# if age >= 18:
#     print("you can vote")
    
# # # -> else
# age = int(input("enter age: "))
# if age >= 18:
#     print("you can vote")
#     print("you can drive")
# else:
#     print("you can't vote")

# # -> elif
# color = input("enter color: ")
# if color == "red":
#     print("stop")
# elif color == "green":
#     print("go")
# elif color == "yellow":
#     print("wait")
# else:
#     print("wrong color for traffic lights")


# # -> persenoality check
# age = int(input("enter age: "))

# if (age < 13):
#     print("child")
# elif (age >= 13 and age < 18):
#     print("teenager")
# else:
#     print("adult")

# # -> login and password check (user authentcation)
# username = input("enter username: ")
# password = input("enter password: ")

# if (username == "admin" and password == "pass"):
#     print("LOGIN Successful!")
# elif (username != "admin"):
#     print("Wrong Username")
# else:
#     print("Wrong Password")
    
# # -> check multiple or not
# n = int(input("enter num: "))

# if (n % 5 == 0):
#     print("multiple of 5")
# else:
#     print("not multiple of 5")
    
# # Nesting
# username = input("enter username: ")
# password = input("enter password: ")

# if (username == "admin" and password == "pass"):
#     print("successs")
# else:
#     if (username != "admin"):
#         print("wrong username")
#     else:
#         print("wrong password")