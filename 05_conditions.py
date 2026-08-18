""" 
05_Condition
Topic covered:
- Making decisions in Python 
- If statements
- Elif and Else statements
- Conditional 

"""



# a = int(input("Enter your age:"))
# print("Your age is:", a)

# conditional operators
#  <, >, <=, >=, ==, !=
# print(a>18)
# print(a<=18)
# print(a>=18)
# print(a==18)
# print(a!=18)

# if-else and elif conditions

bananaPrice = 50
budget = 30

if(bananaPrice <= budget):
    print("Alexa, add 1 Dozen Bananas to the cart.")
else:
    print("Alexa, do not add bananas to the cart.")    

num = int(input("Enter the value of num: "))
if (num < 0):
    print("Number is negative.")
elif (num == 0):
    print("Number is Zero.") 
else:
    print("Number is Positive.")   



