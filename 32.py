class bank:
    def __init__(self,a,n,t,b):
        self.ac = a
        self.name = n
        self.type = t
        self.bal = b
    def depo(self,a1):
        self.bal += a1
        print("Balance:",self.bal)
    def widthdraw(self,a2):
        if self.bal<a2:
            print("Invalid")
        else:
            self.bal -= a2
            print("Balance:",self.bal)
    def disp(self):
        print("Acc No:",self.ac)
        print("Name:", self.name)
        print("Acc Type:", self.type)
        print("Acc Balance:", self.bal)
a=int(input("Enter acc no:"))
n=input("Enter name:")
t=input("Enter acc type:")
b=int(input("Enter balance:"))
obj1=bank(a,n,t,b)
obj1.disp()
a1=int(input("Enter the amount to deposite:"))
obj1.depo(a1)
a2=int(input("Enter the amount to widthdraw:"))
obj1.widthdraw(a2)
