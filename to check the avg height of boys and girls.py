ngirls=int(input("enter the number of girls in your classroom"))
nboys=int(input("enter the number of boys in your classroom"))
sumg=0
for i in range(0,ngirls):
    heightg=float(input("enter height of the student"))
    sumg=sumg+heightg
print("avg height of girls=",int(sumg/ngirls))
sumb=0
for i in range(0,nboys):
    heightb=float(input("enter height of the student"))
    sumb=sumb+heightb
print("avg height of boys=",int(sumb/nboys))
