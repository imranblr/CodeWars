def count_salutes(hallway):
    _list = list(hallway)
    count = 0
    while _list:
        ludo = _list[0]
        if ludo == '>':
            for x in _list:
                if x == '<': count += 2
        _list.remove(ludo)
    return count

