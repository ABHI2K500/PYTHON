N=int(input("Enter a Number:"))
for i in range(2,N):
    if N%i==0:
        print(" The given Number  is not prime")
        break
else:
    print(f"The Given Number {N}  is  prime")