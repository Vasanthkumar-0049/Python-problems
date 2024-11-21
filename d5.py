'''
username = str(input("Enter the user Name:"))
password = int(input("Enter the Password:"))

if username == "vasanth" and password == 12345:
               print("login Sucessfully")
elif username != "vasanth" and password == 12345:
    print("pls enter valid username")
elif username == "vasanth" and password != 12345:
    print("pls enter valid password")
else:
    print("Invalid")




lab1 =int(input("enter lab1 numbers:"))
lab2 =int(input("enter lab2 numbers:"))
lab3 =int(input("enter lab3 numbers:"))
num = int(input("enter number of students:"))


if num>=lab1 and num>=lab2 and num<=lab3:
    print("lab3 avilable")
elif num>lab1 and num>lab3:
    print("lab2 avilable")
elif num>lab2 and num>lab1:
    print("lab3 avilable")
elif num>lab2 and num>lab3:
    print("lab2 avilable")
elif num>lab3 and num>lab2:
    print("lab1 available")
elif num>lab3 and num>lab1:
    print("lab2 avilable")
    

num = int(input("enter the number:"))
if num%2==0:
    print("even")
else:
    print("odd")
                  
num1 = int(input("enter the number1:"))
num2 = int(input("enter the number2:"))
if num1 > num2:
    print("num1 is greater than num2")
else:
    print("num2 is greater than num1")

char = str(input("enter the string"))
p =char[::-1]
if char == p:
    print("it is palindrome")
else:
    print("it is not palindrome")

list_item = input("Enter the numbers:").split()
max_num = -1
for num in list_item:
    if int(num)%3==0 and int(num)>max_num:
        max_num = int(num)
if max_num == -1:
    print("there is no number divisible by 3")
else:
    print(max_num)



num1 = int(input("enter the number1:"))
num2 = int(input("enter the number2:"))
pro = num1*num2
sum = num1+num2
if pro >=1000:
    print(sum)
else:
    print(pro)

sum = 0
for x in range(1,21):
    sum +=x
    print(sum)

string = str(input("enter the string"))
x = list(string)
for i in x[0::1]:
             print(i)
'''
char = str(input("enter the string"))   #vasanth

if char == char[::-1]:    #vasanth == htnasav
    print("it is palindrome")
else:
    print("it is not palindrome")

