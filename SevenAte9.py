def seven_ate9(str_):
    prev = 0
    sprev = 0
    word = ""
    count = len(str_)
    for x in str_:
        if x.isdigit():
            # if prev == 7 and count != 1 and int(x) == 9:
            #     next = 9
            #     continue
            # if prev == 7 and next == 9 and int(x) == 7:
            #     word += x
            #     continue
            # elif prev == 7 and next == 9:
            #     word += '9'
            #
            # prev = int(x)
            if prev == 7 and int(x) == 9 and count != 1:
                sprev = 9
                continue
            if prev == 7 and int(x) == 9 and count == 1:
                sprev = 0
                word += x
                continue
            if sprev == 9 and int(x) == 7:
                word += x
                sprev = 0
                continue

            if sprev == 9:
                word += '9' + x
                sprev = 0
                continue

            prev = int(x)
        else:
            prev = x

        word += x
    #         count -= 1

    return word

print(seven_ate9('165561786121789797'),'16556178612178977')
print(seven_ate9('797'),'77')
print(seven_ate9('7979797'),'7777')



