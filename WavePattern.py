def draw(waves):
    height = max(waves)
    str1 = ""
    str2 = None

    for i in range(1, height + 1):
        for x in waves:
            if x >= i:
                str1 += '■'
            else:
                str1 += '□'

        if str2 is not None:
            str2 = str1 + '\n' + str2
        else:
            str2 = str1

        str1 = ""
    str3 = """
    {}
    """.format(str2).strip()
    #     print(repr(str2))
    return str3

wave1 = """
□□□■
□□■■
□■■■
■■■■
""".strip()

wave2 = """
□□■■□□
□■■■■□
■■■■■■
""".strip()

wave3 = """
□□□□□□□□□□□□■
□□□□□□□□□□□■■
□□□□□□□□□□■■■
□□□□□□□□□■■■■
□□■■□□□□■■■■■
□■■■■□□■■■■■■
■■■■■■■■■■■■■
""".strip()

wave4 = """
□□□□□■□□□□□□□
■□□□□■■□□□■□□
■□□□■■■■□□■□□
■■□□■■■■□■■□□
■■□■■■■■■■■■□
■■■■■■■■■■■■■
""".strip()

wave5 = """
■□■□■□■□
""".strip()

print(draw([1,2,3,4]), wave1)
print(draw([1,2,3,3,2,1]), wave2)
print(draw([1,2,3,3,2,1,1,2,3,4,5,6,7]), wave3)
print(draw([5,3,1,2,4,6,5,4,2,3,5,2,1]), wave4)
print(draw([1,0,1,0,1,0,1,0]), wave5)