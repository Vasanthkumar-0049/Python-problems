'''
import math
x=56.999
print(math.floor(x))
print(math.ceil(x))
print(dir(math))
'''
n1 = int(input())
n2 = int(input())
r=0
while n1>0:
    if n1%2!=0 and n2%2!=0:
        r*=2
    print(r)

