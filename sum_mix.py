def sum_mix(lst):
    num_lst = []
    for num in lst:
        if type(num) == int:
            num_lst.append(num)
        elif type(num) == str:
            num_lst.append(int(num))

    total = 0
    for i in num_lst:
        total += i

    return total

