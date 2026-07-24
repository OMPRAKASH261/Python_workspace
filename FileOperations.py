# # -> Reading 'r'
# f = open("sample.txt", "r") #file object
# data = f.read()
# print(data)
# print(type(data))
# f.close()


# # ->> read file line by line
# data = f.readline() # read file line by by line
# print(data)  # print first line
# f.close()
# data = f.readline()
# print(data)  # print second line
# f.close()


# # -> writing 'w'
# f = open("sample.txt", "w") #file object
# f.write("Text to overwrite \n the complete data.")
# f.close()


# # -> append 'a'
# f = open("sample.txt", "a")
# f.write("\n New text being appended \n to the file")
# f.close()


# # -> 'x' -> create a new file, if alreay exist give error
# f = open("smaple2.txt", "x")
# f.write("Some random text")
# f.close()


# # -> 'r+' -> pointer at start
# f = open("sample.txt", "r+")
# f.write("123")
# print(f.read())
# f.close()


# # -> 'a+' -> pointer at end
# f = open("sample.txt", "a+")
# f.write("456")
# print(f.read())
# f.close()


# ## -> 'w+' -> remove all the element and print new element in file
# f = open("smaple2.txt", "w+")
# f.write("hello")
# print(f.read())
# f.close()

## -> with keyword
with open("sample.txt", "r") as f:
    data = f.read()
    print(data)
    print(len(data))