import random as r
l=[]
a=0
for i in range(1,4):
    val=r.randint(10,15)
    l.append(val)
    for i in range(0,len(l)-1):
        if l[i]%5==0:
             a=l[i]
else:
        print("no")
print(l)
print(f"the multi of 5 is {a}")
        
    
