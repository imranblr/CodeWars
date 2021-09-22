def iq_test(numbers):
    datalist = numbers.split()
    evencount=0
    oddcount=0
    evenpos=0
    oddpos=0
    for i in range(len(datalist)):
        if (int(datalist[i]) % 2) == 0:
            evencount+=1
            evenpos=i+1
        else:
            oddcount+=1
            oddpos=i+1
    if evencount == 1: return evenpos
    else: return oddpos