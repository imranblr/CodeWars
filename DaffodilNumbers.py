"""
Find the number of all daffodils

Version: 1.0
Author: Imran Khan
"""

myList = []
for n in range(100, 1000):
    mylist = [i for i in str(n)]
    if int(mylist[0])**3 + int(mylist[1])**3 + int(mylist[2])**3 == int(n):
        myList.append(n)
print(myList)