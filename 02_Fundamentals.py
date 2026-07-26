"""
File: 02_fundamentals.py

Topic Covered:
- Variables
- Data Types 
- Basics Operators 
- type casting


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


'''
Lab Task: Evaluate the algebraic expression: 3x^3 - 2x^2 + 3x -1
Note: "x" must be of type float.
The result should be assigned to y.
'''

# Sample Input
x = 0
x = 1
x = -1

x = 0
x = float(x)
y = 3 *x**3 - 2 *x**2 + 3 *x - 1
print("y =", y)

x = 1
x = float(x)
y = 3 *x**3 - 2 *x**2 + 3 *x - 1
print("y =", y)

x = -1
x = float(x)
y = 3 *x**3 - 2 *x**2 + 3 *x - 1
print("y =", y)

# Used to variable in various type.
var = 2
print(var)

var = 3
print(var)

var += 1
print(var)

var = "007"
print("Agent " + var)


a = '1'
b = "2"
print(a + b)

# 2. Operators   (+ ,- ,* ,** ,/ ,// ,% )

print(2 + 2)     # addition of two numbers
print(3 - 2)     # subtraction of two numbers
print(3 * 6)     # multiplication of two numbers
print(3 ** 2)    # exponential
print(5 / 2)     # Division operators
print(15 // 7)   # floor Division
print(10 % 5)    # Modulus

# floor division
print(6 // 4)
print(6. // 4)

print(-6 // 4)
print(6. // -4)


# Exercise

m = 5 
n = 6

ans1 = n + m
print("Addition of ans1 is :", ans1)

ans2 = n - m 
print("Subtraction of ans2 is :", ans2)

ans3 = n * m
print("multiplication of ans3 is :",  ans3)

ans4 = n / m
print("division of ans4 is :", ans4)

ans5 = n // m
print("floor division of ans5 is :",  ans5)

ans6 = n % m
print("modulus of ans6 is :", ans6)

ans7 = n ** m
print("exponential of ans7 is :", ans7)


# operators and their priorities

# for example: 2 + 3 * 5

print(2 + 3 * 5)       # answer are:17 because "*" has a higher priority than "+". 

# Operators and their bindings(same side of equal priority)

print(9 % 6 % 2)       # we calculate to ans in left-right side.
print(2 ** 2 ** 3)     # the exponentiation operator uses right-sided binding.
print(2 * 3 % 5)       # both operator are same priority then python evaluates using left- right side
print((5 * ((25 % 13) + 100) / (2 * 13)) // 2)

print((-2 / 4), (2 / 4), (2 // 4), (-2 // 4))

# 3. Type Casting

a = "1"
b = "2"
print(a + b)         # its always print their output as a jaisa likha hai vysa hi print hoga ex: print(a + b): 12 not a print 3.
print(int(a) + int(b))   # its convert the sting into integer values.

string = "12"
number = 3

string_number = int(string)
sum = number + string_number
print("sum of the both numbers is:", sum) 

# implicit TypeCasting 
c = 2.8
d = 4
print(c + d)

a = 7
print(type(a))
b = 3.0
print(type(b))

c = a + b           # python automatically convert c to float as it is float addition
print(c)
print(type(c))

# how to used input function:

z = input("Enter your name: ")
print("My Name is: ", z)

'''x = input("Enter your first number:")
y = input("Enter your second number:")
print(x + y)       # its always print string 
print(int(x) + int(y))'''


# Arithmetric operators using input function.

a = input("Enter your first value: ")
b = input("Enter your second value: ")

print(a + b)
print(a * b)
print(a % b)
print(a ** b)
print(a // b)   # agr ye operator ko as a string ke tarah used krege to answer hmesa error aayga.

print(int(a) + int(b))
print(int(a) - int(b))
print(int(a) * int(b))
print(int(a) / int(b))
print(int(a) % int(b))
print(int(a) ** int(b))
print(int(a) // int(b))   # its print always their original value because it used to int data type.













