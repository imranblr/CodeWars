def compute_sum(n):
    sum=0
    mylist=[]
    for x in range(n+1):
        if x <= 9:sum+=x
        else:
            mylist=list(map(int, str(x)))
            for y in mylist:
                sum+=y
    return sum