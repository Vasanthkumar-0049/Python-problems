by = int(input("enter the birth year:"))
cy = int(input("enter the current year:"))
if cy>by:
    age = cy-by
    print(age)
else:
    by=100-by
    age=cy+by
    print(age)
