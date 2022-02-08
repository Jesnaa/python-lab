a=[]
for i in range(0,10):
    if  i<5:
        for j in range(1,i+1):
            a.append("*")
        print(str(a).replace("[","").replace("]","").replace(",","").replace("'","").replace("'",""))
        a=[]
    else:
        i=10-i-1
        for j in range(0,i+1):
            a.append("*")
        print(str(a).replace("[", "").replace("]", "").replace(",", "").replace("'", "").replace("'", ""))
        a = []
