def longest_consec(strarr, k):
    if len(strarr)==0 or k>len(strarr) or k<=0:return ""
    if k == 1:_len=len(strarr)
    else:_len=int(len(strarr)-1)
    mylist = [ [] for _ in range(_len) ]
    _list=[]
    for x in strarr: _list.append(x)
    temp=''
    for j in range(_len):
        ludo=_list[0]
        if len(_list)>(k-1):
            for i in range(k):
                temp+=_list[i]
        mylist[j].append(temp)
        _list.remove(ludo)
        temp=''
    flatlist=[item for elem in mylist for item in elem]
    return (max(flatlist, key=len))