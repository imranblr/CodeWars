def validate_word(word):
    dict = {}
    count = 0
    for x in word.lower():
        for i in range(len(word)):
            if x == list(word.lower())[i] :
                count += 1
        dict[x] = count
        count = 0
    # print(dict)
    f = None
    for y in dict.values():
        if f is None: f = y
        if f == y: continue
        else: return False
    return True

print(validate_word("abcabc"),True)
print(validate_word("Abcabc"),True)
print(validate_word("AbcabcC"),False)
print(validate_word("AbcCBa"),True)
print(validate_word("pippi"),False)
print(validate_word("?!?!?!"),True)
print(validate_word("abc123"),True)
print(validate_word("abcabcd"),False)
print(validate_word("abc!abc!"),True)
print(validate_word("abc:abc"),False)
