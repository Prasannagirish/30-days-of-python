


'''name = input("Enter your name :")
print("Hi" + name)
birth_year = int(input("Enter your birthyear :"))
current_year = int(input("Enter current year :"))
age = current_year - birth_year
print(age)
name = 'Jennifer'
print(name[1:-1] )
# formatted'
first = 'John'
last = 'Smith'
msg = f'{first}[{last}] is a coder'
print(msg)
#string methods
course = "python for beginners"
print(len(course))
print(course.capitalize())
print(course.find('o'))
print(course.replace('Beginners','Absolute beginners'))
print('python'in course) 
# IF statements
is_hot = False
if is_hot:
    print("It is a hot day")
print("Enjoy your day")
price_of_house = 100000
credit = int(input("Enter credit score :"))
if credit >= 860:
    down_payment = 0.1*price_of_house
    print(f'Down payment :${down_payment}')
else:
    down_payment = 0.2*price_of_house
    print(f'Down payment :${down_payment}')
## Weight converter using if else
weight = int(input("Enter your weihght :"))
units = input("Enter L(pounds) or Kg(kilogram) :")
if units == 'kg' or 'Kg' or 'KG':
    weight_p = weight*2.2046
    print("Your weight in pounds is %d",(weight_p))
else :
    units == 'l' or 'L'
    weight_k = weight/2.2046
    print("Your weight in kilogerams is %d",(weight_k))
i = 1
while i<=6:
    print('*'*i)
    i=i+1
print("Done")
secret_number = 9
guess_count=0
guess_limit =3
while guess_count<guess_limit:
    guess = int(input("Enter your Guess :"))
    guess_count+=1
    if guess == secret_number:
        print("You won!")
        break
else: print("You lost!")'''
## Car game
started = False

while True:
    command = input("> ").lower()
    if command == "start":
        if started:
            print("Car aldready started")
        else :
            started = True
            print("Car started")
    elif command=="stop":
        if not started:
            print("Car aldready stopped")
        else:
            started = False
            print("Car stopped")
    elif command == "help":
        print('''
start - start the car 
stop - stop the car
quit - to quit''')
    elif command == "quit":
        break
    else :
        print("Sorry I don't understand that")