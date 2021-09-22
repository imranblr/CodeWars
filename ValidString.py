def valid_word(seq, word):
    mySeq = []
    myWord = word
    myWord1 = word
    myWord2 = word
    for x in seq:
        if x in myWord:
            if len(x) == len(myWord):
                return True
            else:
                myWord = myWord.replace(x, '')
    if len(myWord) == 0: return True

    seq.sort(key=len)
    for x in seq: mySeq.append(x)
    for x in mySeq:
        if x in myWord1:
            if len(x) == len(myWord1):
                return True
            else:
                myWord1 = myWord1.replace(x, '')
    if len(myWord1) == 0:
        return True
    else:
        seq.sort(key=len, reverse=True)
        for x in seq:
            if x in myWord2:
                if len(x) == len(myWord2):
                    return True
                else:
                    myWord2 = myWord2.replace(x, '')
        if len(myWord2) == 0:
            return True
        else:
            return False