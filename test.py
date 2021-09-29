arr = [1, 2, 3, 4]
arr_num = int(len(arr)/4)
f = lambda A, n=4: [A[i:i+n] for i in range(0, len(A), 4)]
list = f(arr)
print(list)
for i in list:
    print(i, len(i))
    for x in i:
        print(x)
# count=0
# key=96
# pos=0
# list = ['0', '0']
# # list =[]
# count = 0
#
# def counting(key, count, list):
#     if key < 27:
#         charac = count % 26
#         pos = int(count / 26)
#         print(key, charac, pos, end='')
#         list[pos] = chr(charac+96)
#         return list
#     # counting(key, pos, count, list)
# # def trc(n):
# #     return(int(str(n), base = 36))
#
# def trc(n):
#     charac = ""
#     prev = ""
#     # print("n ->", n)
#     if (n == 0): pass
#     if (n >= 1 and n <= 26): return chr(n+96) #print(chr(n+96), end='')
#     # if n %26 is 0: return prev + chr(n+96)
#     # return charac
#     else:
#         charac = str(trc(int(n / 26)))
#         x = n % 26
#         # print("x ->", x)
#         if x == 0: x = 26 #return chr(ord(charac) -1) + 'z'
#         if (x <= 26): charac += chr(x+96) #print(chr(x+96), end='')
#     return charac
#
# for i in range(1, 474550):
#     print(trc(i), "")
#     # print("")



