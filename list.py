l1=[]
l2=[]
n=int(input("enter number of elements in your list"))
for i in range(n):
    digit=int(input("enter a number"))
    l1.append(digit)
for i in range(len(l1)-1):
    if l1[i] not in l2:
        l2.append(l1[i])
print(l2.sort(reverse=True))