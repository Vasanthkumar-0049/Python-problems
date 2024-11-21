'''
row = int(input("enter the number:"))
for i in range(0,row+1):
    for j in range(i,-1,-1):
        print(j+1,end=" ")
    print()

row = int(input("enter the number:"))
for i in range(row,0,-1):
    for j in range(i,0,-1):
        print(j,end=" ")
    print()

    
row = int(input("enter the number:"))
for i in range(1,row+1):
    for j in range(row,i-1,-1):
        print(j,end=" ")
    print()

row = int(input("enter the number:"))
for i in range(1,row+1):
    for j in range(1,i+1):
        r = j%2
        if r==0:
            print(0,end=" ")
        else:
            print(1,end=" ")
    print()


row = int(input("entre the number:"))
for i in range(1,row+1):
    for j in range(1,row+1):
        print(j,end=" ")
    print()


row = int(input("enter the number:"))
for i in range(1,row+1):
    for j in range(1,i+1):
        r = j%2
        if r==0:
            print(1,end=" ")
        else:
            print(0,end=" ")
    print()

n=int(input("enter the number:"))
for i in range(1,n+1):
    for j in range(1,n+1):
        print(j,end=" ")
    print()

n=int(input("enter the number:"))
for i in range(n,0,-1):
    for j in range(n,i-1,-1):
        if(i==1 or j==n or i==j):
            print(j,end=" ")
        else:
            print(" ",end=" ")
    print()


n= int(input("enter the string:"))
for i in range(1,n+1):
    for j in range(1,n+1):
        if(i==1 or j==1 or i==n or j==n):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

num = int(input("enter the number:"))
for i in range(1,n+1):
    for s in range(i,n):
        print(" ",end=" ")
    for k in range(1,n+1):
        if(i==n or k==i or k==1):
                print(k,end=" ")
        else:
                print(" ",end=" ")
    print()
'''
st = str(input("Enter the Student type:")).upper()
tf = float(input("Enter tuition fee:"))
bf = float(input("Enter bus fee:"))
hf = float(input("Enter hostel fee:"))
if st == "MSDS":
    sum = tf+bf
    print("the fees to be paid by the student is Rs.",sum)
elif st == "MSH":
    sum = tf+hf
    print("the fees to be paid by the student is Rs.",sum)
elif st == "MGSDS":
    sum = 150/100*tf+bf
    print("the fees to be paid by the student is Rs.",sum)
elif st == "MGSH":
    sum = 150/100*tf+hf
    print("the fees to be paid by the student is Rs.{:.0f}".format(sum))

