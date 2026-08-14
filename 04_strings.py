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
name = "mamata mourya !! mamata"
print(name.upper())
print(name.lower())
print(name.capitalize())
print(name.rstrip("!"))
print(name.replace("mamata", "Aashish"))
print(name.split(" "))

str1 = "Welcome to python Journey!!!"
print(str1.center(25))
print(len(str1))
print(name.count("mamata"))
print(str1.endswith("000"))
print(str1.endswith("!!!"))
print(str1.endswith("to", 4, 10))

str2 = "he's name is pratham. He is an honest man."
print(str2.find("is"))
print(str2.find("ishh"))     # find method mai kuch bhi wrong likha to vo return -1 krega.
#print(str2.index("ishh"))    # index method are return the error for wrong letter in string

str3 = "WelcomeToTheConsole"
print(str3.isalnum())  # if any character, punctuation or numbers(0-9) are present ,then it return False
str1 = "hello world"
print(str1.islower())   # is return True if all chr. are lower case else it return False.
str4 = "Hello World"
print(str4.istitle())   # it used to first letter will be capitalized & use Title.
str1 = "Python is a interpreted language"   # check the if string start with given value then return True else False.
print(str1.startswith("Python"))

str1 = "Python is a interpreted language"
print(str1.swapcase())    # This method use to convert upper case to lower case & lower case to upper.
str2 = "he's name is pratham. He is an honest man."
print(str2.title())   # it's capitalizes each starting words
