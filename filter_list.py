def filter_list(l):
    new_l = [x for x in l if type(x) == int]
    return new_l

lst = [1, 2, 3, '4', 'c', 'g', 7, '8', 9]

print(filter_list(lst))