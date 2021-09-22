def spin_words(sentence):
    mylist=sentence.split(' ')
    newlist=[]
    for x in mylist:
        if len(x) >= 5: newlist.append(x[::-1])
        else: newlist.append(x)
    return (" ".join(newlist))