def zero_plentiful(arr):
    count = 0
    sets = 0
    for x in arr:
        if x is 0:
            count += 1
        elif count >= 4:
            sets += 1
            count = 0
        elif count >= 1 and count < 4:
            return 0
    szero = [x for x in arr if x is 0]

    if len(szero) is len(arr):
        return int(count / 4)
    elif count >= 4:
        sets += 1
        return sets
    elif count == 0:
        return sets
    else:
        return 0


print(zero_plentiful([3]),0)
print(zero_plentiful([0,0,0,0,0,0]),1)