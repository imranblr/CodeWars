def alphanumeric(password):
    decision = False
    for x in password:
        if x.isalnum(): decision = True
            # print(x)
        else: return False
    return decision


print(alphanumeric("hello world_"), False)
print(alphanumeric("PassW0rd"), True)
print(alphanumeric("rqqft9WAEJURuTo^F1Xwbk"), False)