n=input("enter any words: ")
n1=n.split(' ')
for a in n1:
    n1[n1.index(a)]=a[1]+a[0]+a[2:]
print(n1)