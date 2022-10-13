# Looping statements and Conditionals 
name = int(input("Enter your age "))
if name>18:
    print("Your old enough to drive")
else :
    diff = int(18-name)
    print("Wait for %d years to learn to drive" %(diff))

age = int(input("Enter your age :"))
age2 = int(input("Enter your friend's age :"))
if age>age2:
    difference = int(age-age2)
    print("You are %d years older than your friend" %(difference))
elif age<age2:
    difference2 = int(age2-age)
    print("Your friend is %d years older than you " %(difference2))

a = int(input("Enter number one :"))
b = int(input("Enter number two :"))
if a>b:
    print("A is greater than B")
elif a<b:
    print("B is greater than A")
elif a==b:
    print("A is equal to B")

g = int(input("Enter your Score :"))
if g in range (80,101):
    print("Your grade is A")
elif g in range(70,80):
    print("Your grade is B")
elif g in range (60,70):
    print("Your grade is C")
elif g in range(50,70):
    print("Your grade is D")
elif g in range(40,50):
    print("Your grade is F")
else: print("You failed your exam")

season = input("Enter month :")
if season == "September" or "October" or "November":
    print("The season is Autumn")
elif season == "December"or"January" or "February":
    print("The season is Winter")
elif season == "March"or"April"or"May":
    print("The season is Spring")
else: print("The season is Summer")

fruits = ['banana','orange','mango','lemon']
enter_fruit = input("Enter fruit name :")
if enter_fruit not in fruits:
    fruits.append(enter_fruit)
    print(fruits)
else: print("That fruit aldready exist in the list")

