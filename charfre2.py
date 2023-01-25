string=(input("enter any string: "))

for i in string:
    frequency = string.count(i)
    #print (str(i), " : ", str (frequency), end=", ")
    print(i,':',frequency,end=',') 