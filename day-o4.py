# Adding two numbers
num1 = 34
num2 = 35
sum = num1+num2
print(sum)
nume1 = input('First number :')
nume2 = input('Second number :')
sums = float(nume1)+float(nume2)
print("The sum of {0} and {1} is {2}".format(nume1,nume2,sums))
# Maximum of two numbers
def maximum(a,b):
    if a>=b:
        return a
    else:
        return b
a = 5
b = 55
print(maximum(a,b))
a = 4**33
b = 3**44
maximum = max(a,b)
print(maximum)
# Factorial of numbers
def factorial(n):
    return 1 if (n==1 or n==0) else n*factorial(n-1)
num = 10
print(factorial(num))
# Simple interest
prin = int(input("Enter Prinicpal:"))
rate = int(input("Enter interest rate :"))
time = int(input("Enter time :"))
interest = ((prin)*(rate)*time)/100
print(interest)
# Compound interest
p = int(input("Enter principal :"))
t = int(input("Enter time :"))
r = int(input("Enter rate :"))
a = p*(1+(r/100))**t
interest = a-p
print(interest)
# Calculating area of circle 
r = int(input("Enter radius :"))
pi = 3.142
area = pi*(r**2)
print(area)
# Checking whether a given number is prime or not 
pn = int(input("Enter number :"))
if pn >1:
    for i in range (2,int(pn/2)+1):
        if (pn%i == 0):
             print(pn,"is not a prime number")
    else:
        print(pn,"is a prime number")
else:
    print(pn,"is not a prime number")
# Checking if a number is a fibonacci number
import math
from re import I
def isps(x):
    s =int(math.sqrt(x))
    return s*s == x
def isFibonacci(n):
    return isps(5*n*n+4) or isps(5*n*n-4)
for i in range(1,11):
    if(isFibonacci(i) == True):
        print(i,"is a fibonacci number")
    else:
        print(i,"is not a fibonacci number")
## Sum of n squares
def sumofsquares(n):
    sum = 0
    for i in range(1,n+1):
        sum = sum + i*i
    return sum
n = input("Enter number :")
print(sumofsquares(n))



