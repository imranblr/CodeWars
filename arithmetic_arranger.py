import re
def arithmetic_arranger(mylist, calc=False):
    if len(mylist) > 5:
        return "Error: Too many problems."
    for elems in mylist:
        myelems = re.split(' ', elems)
        if not myelems[0].isdigit() or not myelems[2].isdigit():
            return "Error: Numbers must only contain digits."
        if len(myelems[0]) > 4 or len(myelems[2]) > 4 :
            return "Error: Numbers cannot be more than four digits."
        sign = re.match(r'[\\+|\\-]{1}', myelems[1])
        if not sign:
            return "Error: Operator must be '+' or '-'."
        sp = len(myelems[0]) if len(myelems[0]) > len(myelems[2]) else len(myelems[2])
        print(myelems[0].rjust(sp+2, ' '), end='    ')
    print()
    splist=[]
    for elems in mylist:
        myelems = re.split(' ', elems)
        sp = len(myelems[0]) if len(myelems[0]) > len(myelems[2]) else len(myelems[2])
        splist.append(sp)
        print(myelems[1], myelems[2].rjust(sp, ' '), end='    ')
    print()
    for s in splist:
        print('-'*(s+2), end='    ')
    print()
    if calc:
        for elems in mylist:
            myelems = re.split(' ', elems)
            if myelems[1] is "+":
                result = int(myelems[0]) + int(myelems[2])
            else: result = int(myelems[0]) - int(myelems[2])
            sp = len(myelems[0]) if len(myelems[0]) > len(myelems[2]) else len(myelems[2])
            print(str(result).rjust(sp+2, ' '), end='    ')


def main():
    arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True)


if __name__=="__main__":
    main()
