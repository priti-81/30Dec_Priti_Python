n=input("enter words seperated by  comma: ") 
n1=n.split(",")
max=0
for ele in n1:
    if len(ele)>max:
        max=len(ele)
        s=ele
print("word with maximum length: ",s)
print("length is: ",len(s))