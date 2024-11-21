'''
#reverse the string
string = input("enter the string:")
list_item = list(string)
list_item.reverse()
result = "".join(list_item)
print(result)
print()

#atural number:
n=int(input("enter the number:"))
for i in range(1,n+1):
    print(i)

#number pattern using a loop.
row = int(input("enter the number:"))
for x in range(1,row+1,1):
    for y in range(1,x+1):
        print(y,end=" ")
    print()
'''
#unique string
char = input("enter the string:")
unique = set(char)
print(unique)
