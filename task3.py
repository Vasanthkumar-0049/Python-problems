'''
n = int(input("Enter the number:"))
for i in range(1,n+1):
    inc = i
    dec = n-1
    for j in range(1,i+1):
        print(inc,end=" ")
        inc = inc + dec
        dec = dec-1
    print()

n = int(input("enter the number:"))
for i in range(1,n+1):
        for j in range(1,i+1):
            print(chr(j+64),end=" ")
        print()
'''
n = int(input("enter the number:"))
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==j or i+j==n+1:
            print(j,end=" ")
        else:
            print(" ",end=" ")
    print()
    
