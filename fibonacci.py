n=int(input("enter a number"))
x=0
y=1
i=0
while i<n:
    print(x)
    total=x+y
    x=y
    y=total
    i+=1
