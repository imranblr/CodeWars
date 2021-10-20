def find_missing_number(numbers):
#     print(max(numbers))
#     maxi = max(numbers)
#     maxi = 0
#     for i in range(1, max(numbers)+1):
#         if i not in numbers: return i
#         else: maxi = i
#     return maxi+1
#     mylist= sorted(numbers)
#     print(mylist)
#     return "".join(list(str(x) for x in range(1, max(numbers)+1) if x not in mylist))
#     return list(set(range(mylist[0], mylist[-1])) - set(range(1, mylist[-1])))
#     x = set(range(mylist[0], mylist[-1]+1))
#     y = set(mylist)
#     z = (x-y)
#     print(z)
#     if len(z) != 0:
#         return list(z)[0]
#         print(list(z)[0])
#     elif 1 in mylist:
#         return int(mylist[-1])+1
#         print("if 1 is in list", int(mylist[-1])+1)
#     else:
#         return 1
#         print("if 1 is not in list")


    # mylist = sorted(numbers)
    # if 1 not in mylist: return 1
    # elif len(mylist) == mylist[-1]: return int(mylist[-1]) + 1
    # else: return list(set(range(1, mylist[-1])) - set(mylist))[0]


    if len(numbers) == 0: return 1
    s1 = set(numbers)
    l1 = list(s1)

    if 1 != l1[0]: return 1
    elif len(s1) == l1[-1]: return int(l1[-1]) + 1
    return list(set(range(1, l1[-1])) - s1)[0]

print(find_missing_number([2, 3, 4]), 1)
print(find_missing_number([1, 3, 4]), 2)
print(find_missing_number([1, 2, 4]), 3)
print(find_missing_number([1, 2, 3]), 4)