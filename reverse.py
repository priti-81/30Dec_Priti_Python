n=input("enter words : ")
n1=n.split(' ')
for a in n1:
    if len(a)%4==0:
        a1=a[::-1]
        print(a1)