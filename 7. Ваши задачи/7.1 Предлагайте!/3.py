import re

def SPQR(m):
    num = int(m[0])
    result = ''
    lst = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]
    for arabic, roman in lst:
        result += num // arabic * roman
        num %= arabic
    return result

print(re.sub(r'[^0 .]\d*', lambda m: SPQR(m), input()))
