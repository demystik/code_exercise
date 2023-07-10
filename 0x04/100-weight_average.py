def weight_average(my_list=[]):
    if my_list is None:
        return 0
    else:
        num, den = 0, 0
        for tup in my_list:
            num = num + (tup[0] * tup[1])
            den = den + tup[1]
        res = num / den
    return res
