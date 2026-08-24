# LOOPS 

#1.For Loops

name = "Mamata"
for i in name:
    print(i)
    if(i == "t"):
        print("This is something special")

colors = ["Red","Yellow","Pink","Blue","Marron"]
for color in colors:
    print(color)
    for i in color:
        print(i)

fruits = ["Banana","Apple","orange","Mango","Grapes"]
for fruit in fruits:
    print(fruit) 
    for i in fruit:
        print(i)       

# Range Function

for i in range(7):
    print(i)             # output will be start zero value.
for k in range(10):
    print(k + 1)          # output will be start 1 to 10 value(not accept 0)
for m in range(1, 8):     # output will be show 1 to 7 value.
    print(m)

i = 0
while i < 100:
    # do_something()    # start (1 to 100)
    i += 1
    print(i)

for i in range(100):
    # do_something()
    print(i)

for i in range(2, 8, 3):                        # range(start, stop, step)
    print("The value of i is currently", i)     # starts at 2, stop before 8(not print 8), and increments by 3.

for i in range(2, 1):
    print("The value of i is currently", i)    # second argument must be greater than the first.

for i in range(1, 2):
    print(i)    


