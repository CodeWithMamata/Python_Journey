"""
File: 02_fundamentals.py

Topic Covered:
- Variables
- Data Types (int, float, str, bool)
- Basics Operators 


"""

# 1. Variables And Data Types

a = "Mamata mourya"
print(a)
a1 = 129
a2 = 9
a3 = 1.9

# a4 = 6 + 2i  (normal Complex number: 6 + 2i But in python representation: complex(6,2))

a4 = complex(6,2)
print(a4)

print(a1 + a2)
b = True
c = None

print("Type of a is", type(a))
print("Type of a1 is", type(a1))
print("Type of b is", type(b))
print("Type of c is", type(c))
print("Type of a3 is ", type(a3))
print("Type of a4 is", type(a4))

list1 = [5, 2.4, [-6,9], ["Banana","Apple"]]
print(list1)

tuple1 = (("parrot", "saparrow"), ("lion", "tiger") )
print(tuple1)

dict1 = {"name": "sakshi", "age": "49", "canvote": "True"}
print(dict1)

# combine text and variables using "+"
var = "3.8.5"
print(var)
print("Python version: " + var)

# assign new value 
var = 1
print(var)
var = var + 1
print(var)

# evaluates the length of the hypotenuse using Pythagorean theoremc = √ a^2 + b^2 
a = 3.0
b = 4.0
c = (a ** 2 + b ** 2) ** 0.5
print("c =", c)

''' Practice
    find the total appples value : ?
'''
harry = 5
mary = 5
john = 6

print(harry, mary, john,)

total_apples = harry + mary + john
print(total_apples)



