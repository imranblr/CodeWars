def zeros(n):
    prod = 1
    l = []
    for i in range(1, n+1):
        prod *= i
    l[:0] = str(prod)
    l.reverse()
    count = 0
    for x in l:
        if x == '0':
            count += 1
        else:
            break
    return count



print(zeros(0), 0, "Testing with n = 0")
print(zeros(6), 1, "Testing with n = 6")
print(zeros(30), 7, "Testing with n = 30")