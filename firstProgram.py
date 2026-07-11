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
# -> infiinite loops
while True:
    print("hello world")
    
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