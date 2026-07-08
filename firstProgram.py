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
# a = input("enter value of a: ")
# print(a)
# username = input("enter your name: ")
# print("welcome", username)

# -> sum of 2 nums
# a = input("enter a: ")
# b = input("enter b: ")
# sum = a + b
# print(sum)  # a and b are string then they don't add instead give ab.

a = int(input("enter a: "))
b = int(input("enter b: "))
sum = a + b
print(sum)  # a and b are string then they don't add instead give ab.

