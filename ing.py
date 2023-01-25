n=input("enter words : ")
n1=n.split(' ')
for a in n1:
    if len(a)==3:
        print(a+'ing')
    if a.endswith('ing'):
        print(a[:-3]+'ly')
    if len(a)<3:
        print(a)