finalyear = int(input("enter the final year:"))
for year in range(2021 , finalyear):
    if(0 == year %4)and(0 != year %100)or(0 == year ):
        print(year)