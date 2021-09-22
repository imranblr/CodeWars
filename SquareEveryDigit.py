def square_digits(num):
    _list=list(map(int, str(num)))
    newlist=[]
    for x in _list:
        newlist.append(str(x*x))
    return int("".join(newlist))