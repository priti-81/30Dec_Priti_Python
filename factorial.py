n=int(input("enter a factorial no.: "))
i=1
total=1
while i<=n:
    total=total*n
    print(n,end="*")if n>1 else print(n,end="=")
    n-=1
print(total)
