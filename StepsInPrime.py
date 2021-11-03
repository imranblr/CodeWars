import math
def step(g, m, n):
    mylist = []
    p = False
    for pn in range(m, n):
        for i in range(2, int(math.sqrt(pn))+1):
            if (pn % i) == 0:
                p = False
                break
            else: p = True
        if p is True:
            mylist.append(pn)
            for x in mylist:
                if pn - x == g: return [x, pn]


# def step(g, m, n):
#
#     fprime = False
#     sprime = False
#     for num in range(m, n):
#         for i in range(2, num):
#             if (num % i) == 0:
#                 # print(num, i)
#                 fprime = False
#                 break
#             else:
#                 fprime = True
#         if fprime is True:
#             for j in range(2, (num + g)):
#                 if (num + g) % j == 0:
#                     #                         print(j)
#                     sprime = False
#                     break
#
#                 else:
#                     sprime = True
#             if sprime is True: return [num, num + g]


print(step(2,100,110), [101, 103])
print(step(4,100,110), [103, 107])
print(step(2,5,5), None)
print(step(6,100,110), [101, 107])
print(step(8,300,400), [359, 367])
print(step(10,300,400), [307, 317])
