def disemvowel(string):
    _size=len(string)
    _newstring=[]
    vowels=['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    for i in range(_size):
        if string[i] not in vowels:_newstring.append(string[i])
    return str("".join(_newstring))