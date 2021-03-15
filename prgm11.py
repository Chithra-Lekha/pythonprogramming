a=int(input("enter 1st number"))
b=int(input("enter 2nd number"))
c=int(input("enter 3rd number"))
if a>b:
    if a>c:
        print(a,"is largest")
    else:
        print(c,"is largest")
elif b>c:
    print(b,"is largest")
else:
    print(c, "is largest")
