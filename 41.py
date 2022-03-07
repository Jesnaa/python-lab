import csv
field_name=['no','company','car model']
car=[{'no': 1, 'company':'ferrari', 'car model':'gh'},
     {'no':2,'company':'bmw','car model':'x5'},
     {'no':3,'company':'maruti','car model':'swift'},
     {'no': 4, 'company': 'audi', 'car model': 'rush'},
     {'no': 5, 'company': 'toyota', 'car model': 'fortuner'}]
with open('b.csv','w')as csvfile:
     write=csv.DictWriter(csvfile,fieldnames=field_name)
     write.writeheader()
     write.writerows(car)
with open('b.csv', newline='') as csvfile:
    d=csv.reader(csvfile,delimiter='|')
    for r in d:
       print(','.join(r))