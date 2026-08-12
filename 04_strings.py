# Topic: String

name = "Mamata"
friend = "annu"
anotherFriend = "Harshdha"

print("Hello , " + name )
print("HEllo , " + friend)
print("Hello , " + anotherFriend)

apple = ''' He said, 
hii harry 
hey I am good
"I want to eat an apple"'''
print(apple)
print(name[0])
print(friend[0])

print("lets use a for loop\n")
for chr in name:
    print(chr)


# Practice Question


#x = int(input("Enter a number: "))    # The user enters 3
#print(x * "5")

#y = input("Enter a number: ") # The user enters 2
#print(type(y))


names = "Mamata Mourya, Pratham"
print(names[0:6])
print(len(names))

fruit = "Mango"
len1 = len(fruit)
print("mango is a", len1 , "letter words.")

fruit = "Banana"
bananalen = len(fruit)
print(bananalen)
print(fruit[0:5])
print(fruit[:5])
print(fruit[1:5])
print(fruit[0:-4])
print(fruit[-1:-3])

# Quick Quiz

nm = "Harry"
print(nm[-4:-2])


# String are immutable
name = "mamata mourya !!"
print(name.upper())
print(name.lower())
print(name.capitalize())
print(name.rstrip("!"))
print(name.replace("mamata", "Aashish"))
print(name.split(" "))

str1 = "Welcome to python Journey!!!"
print(str1.center(25))
