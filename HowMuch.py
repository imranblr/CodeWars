def howmuch(m, n):
    if m > n:
        start = n
        end = m
    else:
        start = m
        end = n
    bmax = int(end / 7)
    cmax = int(end / 9)
    list_elements = []
    l =[]

    for i in range(start, end + 1):
        for j in range(1, bmax + 1):
            if i - (7 * j) == 2:
                for k in range(1, cmax + 1):
                    if i - (9 * k) == 1:
                        item = 'M: @M'
                        item = item.replace('@M', str(i))
                        l.append(item)
                        item = 'B: @B'
                        item = item.replace('@B', str(j))
                        l.append(item)
                        item = 'C: @C'
                        item = item.replace('@C', str(k))
                        l.append(item)
                        list_ = [x[:] for x in l]
                        l.clear()
                        list_elements.append(list_)
    return list_elements
    # return '[{}]'.format(elements)



print(howmuch(1, 100), [["M: 37", "B: 5", "C: 4"], ["M: 100", "B: 14", "C: 11"]])
# print(howmuch(1000, 1100), [["M: 1045", "B: 149", "C: 116"]])
# print(howmuch(10000, 9950), [["M: 9991", "B: 1427", "C: 1110"]])
# print(howmuch(0, 200), [["M: 37", "B: 5", "C: 4"], ["M: 100", "B: 14", "C: 11"], ["M: 163", "B: 23", "C: 18"]])
# print(howmuch(2950, 2950), [])
# print(howmuch(20000, 20100), [["M: 20008", "B: 2858", "C: 2223"], ["M: 20071", "B: 2867", "C: 2230"]])