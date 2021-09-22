def calc(x):
    total1=""
    total2=""
    sum1=0
    sum2=0
    for i in list(x):
        total1+=str(ord(i))
    for j in list(total1):
        if j == '7': total2+='1'
        else: total2+=str(j)
    for k in list(total1): sum1+=int(k)
    for k in list(total2): sum2+=int(k)
    return (sum1-sum2)