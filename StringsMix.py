import itertools


def mix(s1, s2):
    def counting(l, r=0):
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
        if r is 1:
            return {k: v for k, v in sorted(d.items(), key=lambda item: item[1], reverse=True)}
        else:
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

    def output2(l1, l2, r):
        str1 = ""
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

        for x in l1:
            for y in l2:
                if x in l2.keys():
                    if x is y:
                        if l1[x] > l2[y]:
                            if r is 1: str1 += "2:" + x * l1[x] + "/"
                            else: str1 += "1:" + x * l1[x] + "/"
                            break
                        elif l2[y] > l1[x]:
                            if r is 1: str1 += "2:" + x * l2[y] + "/"
                            else: str1 += "1:" + x * l2[y] + "/"
                            break
                        elif l1[x] == l2[y]:
                            if x is y:
                                str1 += "=:" + x * l1[x] + "/"
                                break
                else:
                    if r is 1: str1 += "2:" + x * l1[x] + "/"
                    else: str1 += "1:" + x * l1[x] + "/"
                    break

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
        return str1[:-1]
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
        str2 = ""
        prev = ""
        same = 0
        repeat = []
        for x in list(l1.keys()):
            for y in list(l2.keys()):
                if same is 1 and prev != l1[x]:
                    str1 += str2
                    str2 =""
                    same = 0
                print("Repeat ->", repeat)
                print("String1 ->", str1)
                print("String2 ->", str2)
                print(l1)
                print(l2)
                print(x, l1[x], y, l2[y])
                if l1[x] > l2[y]:

                    if x not in repeat:
                        if same is 1:
                            str1 = "1:" + x * l1[x] + "/" + str2
                            print("this is executing..")
                            break
                        str1 += "1:" + x * l1[x] + "/"
                        repeat.append(x)
                        l1.pop(x)
                        last = l1[x]
                        break
                    if x in l2.keys():
                        repeat.append(x)
                        l2.pop(x)
                        #break
                elif l2[y] > l1[x]:
                    if y not in repeat:
                        if same is 1:
                            str1 = "2:" + y * l2[y] + "/" + str2
                            print("this is executing..")
                            break
                        str1 += "2:" + y * l2[y] + "/"
                        repeat.append(y)
                        l2.pop(y)
                        last = l1[x]
                        break
                    if y in l1.keys():
                        repeat.append(y)
                        l1.pop(y)
                        #break
                elif l1[x] == l2[y]:
                    if ord(y) > ord(x):
                        if x not in repeat:
                            if same is 1 and prev == l1[x]:
                                if y is list(l2)[-1] and prev == l1[x]:
                                    str1 += "2:" + y * l2[y] + "/" + str2
                                    break
                                str2 = "1:" + x * l1[x] + "/" + str2
                                print("this is executing..")
                                break
                            str1 += "1:" + x * l1[x] + "/"
                            repeat.append(x)
                            l1.pop(x)
                            if y is list(l2)[-1]:
                                str1 += "2:" + y * l2[y]
                            last = l1[x]
                            break
                        if x in l2.keys():
                            repeat.append(x)
                            l2.pop(x) #repeat.append(x)
                            #break
                    elif ord(x) > ord(y):
                        if y not in repeat:
                            if same is 1 and prev == l1[x]:
                                if x is list(l1)[-1] and prev == l1[x]:
                                    str2 = "2:" + y * l2[y] + "/" + str2

                                    # break
                                str1 += "1:" + x * l1[x] + "/" + str2
                                print("this is executing..")
                                break
                            str1 += "2:" + y * l2[y] + "/"
                            repeat.append(y)
                            l2.pop(y)
                            if x is list(l1)[-1]:
                                str1 += "1:" + x * l1[x]
                            last = l1[x]
                            break
                        if y in l1.keys():
                            repeat.append(y) #print("Removing Re-Occurances of ->", l1.pop(y))
                            l1.pop(y)
                            #break
                    elif x is y:

                        # if l1[x] == l1[l1.index(x) + 1] and x not in l2.keys():
                        #     print("Same values in the list")
                        # print(l1[l1.index(x) + 1])
                        if x not in repeat:
                            str2 += "=:" + x * l1[x] + "/"
                            # repeat.append(x)
                            same = 1
                            prev = l1[x]
                            print("previous is", prev, "same is ", same, "string2 is ", str2)
                            # repeat.append(y)
                            if x != list(l1)[-1] or y != list(l1)[-1]:
                                repeat.append(x)
                                repeat.append(y)
                                print("removed ->", l1.pop(x))
                                print("removed ->", l2.pop(y))
                                break
                            # if y != list(l1)[-1] :
                            #     print("removed ->", l2.pop(y))
                            # break





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

        # return str1


    # if len(l1) >= len(l2):
    #     print("l1 is longer list")
    #     return output(l1, l2)
    #
    # else:
    #     print("l2 is longer list")
    #     l1 = counting([x for x in s1], r=1)
    #     l2 = counting([x for x in s2], r=1)
    #     return output2(l2, l1, r=1)
    # l1 = counting([x for x in s1], r=1)
    # l2 = counting([x for x in s2], r=1)
    # return output2(l2, l1, r=1)

    return output(l1, l2)





# s1 = "my&friend&Paul has heavy hats! &"
# s2 = "my friend John has many many friends &"
# print(mix(s1, s2), "--> 2:nnnnn/1:aaaa/1:hhh/2:mmm/2:yyy/2:dd/2:ff/2:ii/2:rr/=:ee/=:ss")
#
# s1 = "mmmmm m nnnnn y&friend&Paul has heavy hats! &"
# s2 = "my frie n d Joh n has ma n y ma n y frie n ds n&"
# print(mix(s1, s2), "--> 1:mmmmmm/=:nnnnnn/1:aaaa/1:hhh/2:yyy/2:dd/2:ff/2:ii/2:rr/=:ee/=:ss")

s1="Are the kids at home? aaaaa fffff"
s2="Yes they are here! aaaaa fffff"
print(mix(s1, s2), "--> =:aaaaaa/2:eeeee/=:fffff/1:tt/2:rr/=:hh")

print(mix("Are they hereZaz", "yes, they are here"), "2:eeeee/2:yy/=:hh/=:rr")
# print(mix("Sadus:cpms>orqn3zecwGvnznSgacs", "MynwdKizfd$lvse+gnbaGydxyXzayp"),
#                        '2:yyyy/1:ccc/1:nnn/1:sss/2:ddd/=:aa/=:zz')
# print(mix("looping is fun but dangerous", "less dangerous than coding"),
#                        "1:ooo/1:uuu/2:sss/=:nnn/1:ii/2:aa/2:dd/2:ee/=:gg")
# print(mix(" In many languages", " there's a pair of functions"),
#                        "1:aaa/1:nnn/1:gg/2:ee/2:ff/2:ii/2:oo/2:rr/2:ss/2:tt")
# print(mix("Lords of the Fallen", "gamekult"), "1:ee/1:ll/1:oo")
# print(mix("codewars", "codewars"), "")
# print(mix("A generation must confront the looming ", "codewarrs"),
#                        "1:nnnnn/1:ooooo/1:tttt/1:eee/1:gg/1:ii/1:mm/=:rr")