y = {'jomol': 20, 'maya': 30,'manu': 28, 'rumy': 33}
l = list(y.items())
dict = dict(l)
print("Dictionary", dict)
l.sort()
print('Ascending order is', l)
l = list(y.items())
l.sort(reverse=True)
print('Descending order is', l)
