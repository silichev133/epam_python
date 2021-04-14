a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
set_a = set(a) #convert list to set to remove duplicates
set_b = set(b)
c = set_a.intersection(set_b) #can also use operator '&' like here 'set_a & set_b'

print(list(c))
