def create_dict(lst1, lst2):
    return dict(zip(lst1, lst2))

arr1 = [1, 2, 3]
arr2 = ['a', 'b', 'c']

d = create_dict(arr1, arr2)
print(d)
