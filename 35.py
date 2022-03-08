class Time:
  def __init__(self, h, m, s):
      self._h1 = h
      self._m1 = m
      self._s1 = s
def __add__(self, x):
      sum1 = self._h1 + x._h1
      sum2 = self._m1 + x._m1
      sum3 = self._s1 + x._s1
      if sum3 >= 60:
       sum3 = sum3 - 60
       sum2 =sum2 + 1
      if sum2 >= 60:
         sum2 = sum2 - 60
         sum1 = sum1 + 1
      print(sum1, ":", sum2,":", sum3);
print("TIME 1")
h1 = int(input("Enter the hour in time1:"))
m1 = int(input("Enter the minute in time1:"))
s1 = int(input("Enter the second in time1:"))
obj1 = Time(h1, m1, s1)
print("TIME 2")
h2 = int(input("Enter the hour in time2:"))
m2 = int(input("Enter the minute in time2:"))
s2 = int(input("Enter the second in time2:"))
obj2 = Time(h2, m2, s2)
print("The sum of both time are:",obj1 + obj2)
obj1 + obj2
