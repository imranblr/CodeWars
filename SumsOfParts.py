def parts_sums(ls):
    mylist=list(ls)
    keep=0
    keeplist=[]
    newlist=[]
    for x in mylist:
        keep+=x
        keeplist.append(keep)
    newlist.append(keep)
    for x in keeplist:
        newlist.append(keep-int(x))
    return newlist