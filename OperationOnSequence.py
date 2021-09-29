# def solve(arr):
#     mylist=[]
#     sum=0
#     total=1
#     lol=1
#     myarr=[]
#     for y in arr:
# #         if y.isdigit():
#         myarr.append(y)
#         lol*=int(y)
#
#     for x in range(len(myarr)):
#         if len(myarr) != 0:
#             ludo1=myarr[0]
#             ludo2=myarr[1]
#             for i in range(2):sum+=int(myarr[i])**2
#             mylist.append(sum)
#             myarr.remove(ludo1)
#             myarr.remove(ludo2)
#             sum = 0
#     for z in mylist: total*=z
#
#     squares = [x * x for x in range(1, lol)]
#     for i in squares:
#         for x in squares:
#             if i + x == total:
#                 return [squares.index(x)+1, squares.index(i)+1]
# import math
def solve(arr):
    def reduce(array):
        final = []
        prod = 1
        sec = 0
        for x in array:
            sec += 1
            if sec == 1:
                elem1 = x * x
            elif sec == 2:
                elem2 = x * x
                sum = elem1 + elem2
                prod *= sum
                sec = 0
        sqr = int((prod ** (0.5)))

        # print("The product is ->", prod)
        # for y in range(sqr, int(sqr / 2), -int(sqr/10)):
        def f2(sqr, prod):
            for y in range(sqr, int(sqr / 2), -1):
                elem3 = y * y
                dif = prod - elem3
                # print("elem3 ->", y, "srqt ->", sqr, "dif ->", dif)
                sqr2 = int(dif ** (0.5))
                # for z in range(sqr2, 1, -int(sqr2/2)):
                for z in range(sqr2, int(sqr2 / 2), -1):
                    elem4 = z * z
                    # print("elem4 ->", z)
                    if elem3 + elem4 == prod: return [y, z]

    # for i in range(len(final)):
    #     for j in i:
        final.append(f2(sqr, prod))
        return [j for sub in final for j in sub]

        # print(final)
    while True:
        f = lambda A, n=4: [A[i:i + n] for i in range(0, len(A), 4)]
        if len(arr) > 2:
            list = f(arr)
            list_2 = []
            for item in list:
                list_2.append(reduce(item))
            arr = [j for sub in list_2 for j in sub]
            print(arr)
        else:
            return arr

    # iter = int(len(arr) / 4)
    # iter -= 1

    # print(list_2)
    # list_3 = [j for sub in list_2 for j in sub]
    # print(list_3)
    # # print(reduce(list_3))
    # return reduce(list_3)
    # if iter is not 0:
    #     return reduce(list_2)
    #     iter -= 1

a1 = [1, 3, 1, 2, 1, 5, 1, 9]
print(solve(a1), [250, 210])
a2 = [2, 1, 3, 4]
print(solve(a2), [2, 11])
a3 = [3, 9, 8, 4, 6, 8, 7, 8, 4, 8, 5, 6, 6, 4, 4, 5]
print(solve(a3), [13243200, 25905600])

