# print("Hello World!")

# x=5
# y=3.14
# name="alice"
is_student=True

# sum = x+y
# product = x*y
# division = x/y

# greeting = "Hello, " + name

# print(x, y, name, is_student, sum, product, division, greeting)

# if is_student:
#     print("Welcome, student!")
# else: print("Welcome, guest!")

# for i in range(5):
#     print(i)

# count = 0
# while count < 5:
#     print(count)
#     count += 1

# def greet(name):
#     return f"Hello, {name}!"
# print(greet("Bob"))

#lists
# fruits = ["apple", "banana", "cherry"]
# print(fruits[0])
# fruits.append("date")
# print(fruits[3])

#dictionaries 
# student = {
#     "name" : "Alice",
#     "age" : 25,
#     "is_student": True
# }
# print (student["name"])

#modules and libraries
# import math
# print (math.sqrt(16))
# import random
# print (random.randint(1,10))

#file handling
    #Writing
# with open ("test.txt", "w") as file:
#     file.write("hello, file!")

#     #Read
# with open ("test.txt", "r") as file:
#     print(file.read())

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def bark(self):
        return f"{self.name} says woof!"
    
my_dog = Dog("Rex", 2)
print(my_dog.bark())

