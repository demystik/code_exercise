def uniq_add(my_list = []):
    sum = 0
    new_list = []
    for i in my_list:
        if i not in new_list:
            new_list.append(i)
    for i in new_list:
        sum = sum + i
    return sum