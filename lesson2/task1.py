def create_dict(lst1, lst2):
    if len(lst1) > len(lst2):
        while len(lst1) > len(lst2):
            lst2.append(None)
    return dict(zip(lst1, lst2))

arr1 = [1, 2, 3, 4, 5]
arr2 = ['a', 'b', 'c']

d = create_dict(arr1, arr2)
print(d)
