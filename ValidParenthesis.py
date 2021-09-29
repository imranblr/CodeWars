def valid_parentheses(string):
    left = 0
    right = 0
    # if list[0] == ')' : return False
    if string == "": return True
    for x in string:
        if x is '(':
            left += 1
        elif x is ')':
            right += 1
        if left < right: return False
    if left == 0 or right == 0 : return False
    if left == right: return True
    else: return False


print(valid_parentheses("  ("), False)
print(valid_parentheses(")test"), False)
print(valid_parentheses(""), True)
print(valid_parentheses("yf(la))(fy(mu)mqdp)()"), False)
print(valid_parentheses("hi(hi)()"), True)
print(valid_parentheses("hi())("), False)