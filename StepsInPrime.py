def step(g, m, n):
    prime_list = [2, 3, 5, 7, 11]
    fprime = False
    sprime = False
    for num in range(m, n):
        #         if [x % y != 0 for y in prime_list]:
        #         print(num)
        for i in range(2, num):
            if (num % i) == 0:
                # print(num, i)
                fprime = False
                break
            else:
                fprime = True
        if fprime is True:
            for j in range(2, (num + g)):
                if (num + g) % j == 0:
                    #                         print(j)
                    sprime = False
                    break

                else:
                    sprime = True
            if sprime is True: return [num, num + g]

#         if x % 5 != 0:
#                 print(x)
#                 if (x+g) % 2 !=0 and (x+g) % 3 != 0 and (x+g) % 5 != 0 and (x+g) % 7 != 0 and (x+g) % 11 != 0:
#                     print(x+g)

print(step(2,100,110), [101, 103])
print(step(4,100,110), [103, 107])
print(step(2,5,5), None)
print(step(6,100,110), [101, 107])
print(step(8,300,400), [359, 367])
print(step(10,300,400), [307, 317])
