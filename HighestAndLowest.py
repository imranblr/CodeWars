def high_and_low(numbers):
    datalist = numbers.split()
    newlist=[]
    while datalist:
        maxi= datalist[0]
        for x in datalist:
            if int(x) > int(maxi):
                maxi = x
        newlist.append(maxi)
        datalist.remove(maxi)
    _num=newlist[0]+' '+newlist[-1]
    return _num