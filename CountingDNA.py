def duplicate_count(text):
    count = 0
    tsize = len(text)
    dup = []
    for i in range(tsize):
        k = i + 1
        for j in range(k, tsize):
            if text[i].lower() == text[j].lower() and text[i].lower() not in dup:
                dup.append(text[i].lower())
                count += 1
    return count
