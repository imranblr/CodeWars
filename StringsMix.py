import itertools


def mix(s1, s2):
    def counting(l):
        d = {}
        for x in l:
            if ord(x) >= 97 and ord(x) <= 122:
                if x in d.keys():
                    d[x] = d[x] + 1
                else: d[x] = 1
        for i in list(d):
            if d[i] <= 1:
                d.pop(i)
        # return sorted(d.items())
        # return d
        result = {}
        # for k, v in itertools.groupby(d, lambda item: item[1]):
        #     result.extend(sorted(v))
        for k, v in sorted(list(d.items()), key=lambda t: (-1 * t[1], t[0])):
            result.update({k : v})

        # return {k: v for k, v in sorted(d.items(), key=lambda item: item[1], reverse=True)}
        return result

    print(counting([x for x in s1]))
    print(counting([x for x in s2]))
    l1 = counting([x for x in s1])
    l2 = counting([x for x in s2])

    # for x in list(l1):
    #     for y in list(l2):
    #         try :
    #             print(l1.popitem())
    #             print(l2.popitem())
    #         except:
    #             pass

    # def output(l1, l2, r):
    #     str1 = ""
    #     out = {}
        # for x in list(l1):
        #     for y in list(l2):
        #         print(l1[x], l2[y])
        #         if l2[y] > l1[x]:
        #             # out.update({y, l2[y]})
        #             str1 += "2:" + y * l2[y] + "/"
        #             print(l2[y], str1)
        #             try:
        #                 l2.popitem()
        #                 l2 = l2
        #             except: pass
        #         elif l1[x] > l2[y]:
        #             # out.update({x, l2[x]})
        #             str1 += "1:" + x * l1[x] + "/"
        #             print(l1[x], str1)
        #             try: l1.popitem()
        #             except:pass
        #         elif l1[x] == l2[y]:
        #             if x is y:
        #                 # out.update({x, l2[x]})
        #                 str1 += "=:" + x * l1[x] + "/"
        #                 print(str1)
        #                 try:
        #                     l1.popitem()
        #                     l2.popitem()
        #                 except: pass
        #             else:
        #                 # out.update({x, l2[x]})
        #                 str1 += "1:" + x * l1[x] + "/"
        #                 print(str1)
        #                 try: l1.popitem()
        #                 except: pass



        # for x in l1:
        #     for y in l2:
        #         if x in l2.keys():
        #             if x is y:
        #                 if l1[x] > l2[y]:
        #                     if r is 1: str1 += "2:" + x * l1[x] + "/"
        #                     else: str1 += "1:" + x * l1[x] + "/"
        #                     break
        #                 elif l2[y] > l1[x]:
        #                     if r is 1: str1 += "2:" + x * l2[y] + "/"
        #                     else: str1 += "1:" + x * l2[y] + "/"
        #                     break
        #                 elif l1[x] == l2[y]:
        #                     if x is y:
        #                         str1 += "=:" + x * l1[x] + "/"
        #                         break
        #         else:
        #             if r is 1: str1 += "2:" + x * l1[x] + "/"
        #             else: str1 += "1:" + x * l1[x] + "/"
        #             break

                # if l1[x] > l2[y]:
                #     if x is y:
                #         if r is 1 : str1 += "2:" + x * l1[x] + "/"
                #         else: str1 += "1:" + x * l1[x] + "/"
                #         break
                #     elif ord(x) > ord(y):
                #         if r is 1 : str1 += "2:" + x * l1[x] + "/"
                #         else: str1 += "1:" + x * l1[x] + "/"
                #         break
                #
                # elif l2[y] > l1[x]:
                #     if x is y:
                #         if r is 1: str1 += "2:" + x * l2[y] + "/"
                #         else: str1 += "1:" + x * l2[y] + "/"
                #         break
                #     elif ord(x) > ord(y):
                #         if r is 1 : str1 += "2:" + x * l1[x] + "/"
                #         else: str1 += "1:" + x * l1[x] + "/"
                #         break
                #
                # elif l1[x] == l2[y]:
                #     if x is y:
                #         str1 += "=:" + x * l1[x] + "/"
                #         break
        # print(str1)
        # return str1[:-1]
    # def listing(l1, l2, r):
    #     for x in l1:
    #         print(x, " -> ", l1[x])
    #     print(output(l1, l2, r))
    #     for y in l2:
    #         print(y, " -> ", l2[y])
    #
    # if len(l1) >= len(l2):
    #     print("l1 is longer list")
    #     listing(l1, l2, r=0)
    #
    # else:
    #     print("l2 is longer list")
    #     listing(l2, l1, r=1)

    # if len(l1) >= len(l2):
    #     print("l1 is longer list")
    #     return output(l1, l2, r=0)
    #
    # else:
    #     print("l2 is longer list")
    #     return output(l2, l1, r=1)
    # return output(l1, l2, r=0)
    # return output(l2, l1, r=1)

    def output(l1, l2):
        str1 = ""
        for x in list(l1.keys()):
            for y in list(l2.keys()):
                # print(str1)
                # print(x, l1[x], y, l2[y])
                if l1[x] > l2[y]:
                    if x in l2.keys():
                        if x is y:
                            str1 += "=:" + x * l1[x] + "/"
                            l1.pop(x)
                            l2.pop(y)
                    else:
                        str1 += "1:" + x * l1[x] + "/"
                        l1.pop(x)
                    break
                elif l2[y] > l1[x]:
                    if y in l1.keys():
                        if y is x:
                            str1 += "=:" + y * l2[y] + "/"
                            l1.pop(x)
                            l2.pop(y)
                    else:
                        str1 += "2:" + y * l2[y] + "/"
                        l2.pop(y)
                    # break
                elif l1[x] == l2[y]:
                    if x is y:
                        str1 += "=:" + x * l1[x] + "/"
                        l1.pop(x)
                        l2.pop(y)
                        break
                    else:
                        str1 += "1:" + x * l1[x] + "/"
                        l1.pop(x)
                        if x in l2.keys(): l2.pop(x)
                        break

                # if x in l2.keys():
                #     if x is y:
                #         if l1[x] > l2[y]:
                #             if r is 1: str1 += "2:" + x * l1[x] + "/"
                #             else: str1 += "1:" + x * l1[x] + "/"
                #             break
                #         elif l2[y] > l1[x]:
                #             if r is 1: str1 += "2:" + x * l2[y] + "/"
                #             else: str1 += "1:" + x * l2[y] + "/"
                #             break
                #         elif l1[x] == l2[y]:
                #             if x is y:
                #                 str1 += "=:" + x * l1[x] + "/"
                #                 break
                # else:
                #     if r is 1: str1 += "2:" + x * l1[x] + "/"
                #     else: str1 += "1:" + x * l1[x] + "/"
                #     break
        return str1[:-1]

    return output(l1, l2)





# print(mix("Are they hereZaz", "yes, they are here"), "2:eeeee/2:yy/=:hh/=:rr")
print(mix("Sadus:cpms>orqn3zecwGvnznSgacs", "MynwdKizfd$lvse+gnbaGydxyXzayp"),
                       '2:yyyy/1:ccc/1:nnn/1:sss/2:ddd/=:aa/=:zz')
# print(mix("looping is fun but dangerous", "less dangerous than coding"),
#                        "1:ooo/1:uuu/2:sss/=:nnn/1:ii/2:aa/2:dd/2:ee/=:gg")
# print(mix(" In many languages", " there's a pair of functions"),
#                        "1:aaa/1:nnn/1:gg/2:ee/2:ff/2:ii/2:oo/2:rr/2:ss/2:tt")
# print(mix("Lords of the Fallen", "gamekult"), "1:ee/1:ll/1:oo")
# print(mix("codewars", "codewars"), "")
# print(mix("A generation must confront the looming ", "codewarrs"),
#                        "1:nnnnn/1:ooooo/1:tttt/1:eee/1:gg/1:ii/1:mm/=:rr")