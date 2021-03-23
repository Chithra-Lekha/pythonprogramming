y = {'swathi': 61, 'arya': 18, 'chithra': 31}

l = list(y.items())
l.sort()   
print('Ascending order is', l)

l = list(y.items())
l.sort(reverse=True)
print('Descending order is', l)
