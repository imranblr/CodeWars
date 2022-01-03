"""
Reverse of a positive integer

Version: 0.1
Author: Imran Khan
"""

num = int(input("Please Enter an Integer Number :"))
numLen = len(str(num))
mylist = [0] * numLen
# print(mylist)
for i in range(numLen):
    mylist[i] = num % 10
    num //= 10
print(''.join([str(x) for x in mylist]))