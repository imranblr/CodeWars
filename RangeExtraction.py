def solution(args):
    _list=[x for x in args]
    mylist=[]
    alist=[]
    count=0
    flist=[]

    def consec(item1, item2):
        if item2-item1==1:
            if item1 not in alist: alist.append(item1)
            alist.append(item2)
            return True
        else: return False

    _list.append(0)
    # print(_list)

    for i in range(len(_list)-1):
        # print('iter', i)
        if consec(_list[i], _list[i+1]):
            count+=1
        elif count==1:
            mylist.append(alist[0])
            alist.clear()
            mylist.append(_list[i])
            # print('consec_count', count)
            count = 0
        elif count>=2:
            ludo=str(alist[0])+'-'+str(alist[-1])
            mylist.append(ludo)
            alist.clear()
            # print('consec_count', count, 'item', _list[i])
            count=0
        else:
            mylist.append(_list[i])
            # print('nonconsec items: ', _list[i])
            count=0
    # print(alist)
    # print(mylist)
    for x in mylist:
        flist.append(str(x).strip())
    # print(','.join(map(str, flist)))
    return (','.join(map(str, flist)))

solution([-6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20]);

# TODO: complete solution
