def not_str(s):
    sub = s[0:3]
    if 'not' == sub:
        return s
    else:
        return 'not '+s
print(not_str("candy"))
