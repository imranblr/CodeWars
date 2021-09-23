def remov_nb(n):
    prod = 0
    ludo = []
    for j in range(1, n+1):
        for k in range(1, n):
            list = [x for x in range(1, n+1) if x != k and x != j]
            sum = 0
            # print("numbers ->", j, k, end=' ')
            prod = j * k
            # print("prod ->", prod)
            # print("popped list ->", list, end=' ')
            for m in list:
                sum += m
            # print("sum ->", sum)
            if prod == sum:
                ludo.append((j, k))
    return ludo

print(remov_nb(5), [])
print(remov_nb(26), [(15, 21), (21, 15)])
print(remov_nb(100), [])
print(remov_nb(101), [(55, 91), (91, 55)])