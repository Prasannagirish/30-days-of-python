a = int(input("Enter number :"))
a=0 
for i in range (0,11):
    print(a)
    a=a+1

for i in range(0,16):
      print(i,'x',i,'=',i*i)

list = ['Python','Numpy','Pandas','Django','Flask']
for x in list:
    print(x)
list = [i for i in range(0,101,2)]
print(list)

list1 = [i for i in range(0,101) if i%2!=0]
print(list1)

list3 = [i for i in range (0,101) ]
print (list3)
total=0
for ele in range(0,len(list3)):
    total = total+list3[ele]
print("Sum of all elements = ",total)

list4 = [i for i in range(0,101) if i%2==0]
print(list4)
total_sum_of_evens = 0
for ele in range(0,len(list4)):
    total_sum_of_evens = total_sum_of_evens+list4[ele]
print("Total sum of evens :",total_sum_of_evens)

list5 = [i for i in range(0,101) if i%2!=0]
print(list5)
total_sum_of_odds = 0
for ele in range(0,len(list5)):
    total_sum_of_odds = total_sum_of_odds+list5[ele]
print("Total sum of odds :",total_sum_of_odds)

