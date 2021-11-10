import math
def buddy(start, limit):
    buddy = {}
    bud = {}
    for i in range(start, limit+1):
        for j in range(1, int(math.sqrt(i) + 1)):
            if i % j == 0:
                buddy.setdefault(i, []).append(j)
        sbuddy = sum(buddy[i]) - 1
#         bud.setdefault(i, []).append(sbuddy)
        if sbuddy >= i and sbuddy >= start:
            for k in range(1, sbuddy):
                if sbuddy % k == 0:
                    bud.setdefault(i, []).append(k)
            sbud = sum(bud[i]) - 1
            if sbud == i : return [sbud, sbuddy]
    return "Nothing"

#     print(buddy, '\n', bud)

print(buddy(10, 50), [48, 75])
print(buddy(2177, 4357), "Nothing")
print(buddy(57345, 90061), [62744, 75495])
print(buddy(1071625, 1103735), [1081184, 1331967])