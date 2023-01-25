n=input("enter words seperated by  comma: ") 
n1=n.split(",")
list1=max(n1,key=len)
print("maximum length is: ",len(list1))