def descending_order(num):
    data_list = list(map(int, str(num)))
    new_list = []

    while data_list:
        maxi = data_list[0]
        for x in data_list:
            if x > maxi:
                maxi = x
        new_list.append(maxi)
        data_list.remove(maxi)

    string1 = []
    for y in new_list:
        string1.append(str(y))
    des_num = "".join(string1)

    return int(des_num)