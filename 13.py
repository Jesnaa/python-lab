list1 =[]
n=int(input("Enter the limit:"))
print("Enter the list of first names:")
for i in range(0,n):
    ele=input()
    list1.append(ele)
print(list1)
c=0
for i in list1:
     if "a" in i:
        c=c+1
print("The number of a in list are:",c)