
# problem 1 
def swap(lst):
    lst[0],lst[-1] = lst[-1],lst[0]
    return lst
lst = [1,2,3,4]
print(swap(lst))
# problem 2
def swap_2(lst,pos1,pos2):
    lst[pos1],lst[pos2] = lst[pos2],lst[pos1]
    return lst 
lst = [12,34,5,63,24.5,66]
print(swap_2(lst,3,4))
# problem 3 
lst = [1,2,3,4]
count = 0 
for i in lst:
    count+=1
print(count)
# problem 4
lst = [1,2,3,4]
count=1
for i in lst:
    count*=i
print(count)
# problem 5 
lst = [1,2,3,4]
count=0
for i in lst:
    count+=i
print(count)
lst = [56,1,3,4,2,5]
min = lst[0]
for i in lst:
    if min>i:
        min=i
    else :
        pass
print(min)
#problem 6
empty_lst = []
n=int(input("Enter number of inupts :"))
for i in range(n):
    num = int(input("Enter a number :")) 
    empty_lst.append(num)
max = empty_lst[0]
for i in empty_lst:
    if max<i:
        max=i
print(max)
#problem 7
lst = []
while True:
    n = int(input("Enter a number:"))
    lst.append(n)
    s = int(input("Do you want to continue?(yes-1 or no-0)"))
    if s == 0 :
        break
print(lst)
#problem 8
max = lst[0]
for i in lst:
    if max<i:
        max=i
print(max)
#problem 9 
list1 = [10, 20, 4, 45, 99]
mx = max(list1[0], list1[1])
secondmax = min(list1[0], list1[1])
n = len(list1)
for i in range(2,n):
	if list1[i] > mx:
		secondmax = mx
		mx = list1[i]
	elif list1[i] > secondmax and \
		mx != list1[i]:
		secondmax = list1[i]
	elif mx == secondmax and \
		secondmax != list1[i]:
		secondmax = list1[i]

print("Second highest number is : ",\
	str(secondmax))
#problem 10
lst1 = [1,-2,3,-4,5]
n = len(lst1)
for i in lst1:
    if i<0:
        lst1.remove(i)
print(lst1)

