# Given a list of tuples with info(name, subject):
# # 1. list all unique course 
# # 2. list students enrolled in English
# # 3. create dictionary (student, set of courses)

info = [
    ("Alice", "Math"),
    ("Bob", "Science"),
    ("Alice", "Science"),
    ("Charlie", "Math"),
    ("Bob", "Math"),
    ("Alice", "English"),
    ("Charlie", "English")
]

courses_set = set()
# quesinon 1
for tup in info:
    courses_set.add(tup[1]) #courses
print(courses_set)

# for name,course in info:
#     print(name, course)

# question 2  
for name, course in info:
    if(course == "English"):
        print(name)
        
# Queestion 3
dict = {}
for name, course in info:
    if(dict.get(name) == None):
        dict.update({name: set()})
        dict[name].add(course)
    else:
        dict[name].add(course)
        
print(dict)        