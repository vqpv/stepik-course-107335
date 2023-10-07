import re


def RUB(m):
    num = float(m[0][1:].replace(",", "."))
    rubs = num * 59.5
    if rubs.is_integer():
        rubs = int(rubs)
        result = f'{str(rubs)} руб'
    else:
        result = f'{str(round(rubs, 2)).replace(".", ",")} руб'
    return result

def SM(m):
    if "дюйм" in m[0]:
        num = float(m[0][:-5].replace(",", "."))
    else:
        num = float(m[0][:-1].replace(",", "."))
    sm = num * 2.54
    if sm.is_integer():
        sm = int(sm)
        result = f'{result} см'
    else:
        result = f'{str(round(sm, 2)).replace(".", ",")} см'
    return result

regex = re.sub(r'[$]\d+[,\d]*', lambda m: RUB(m), input())
regex = re.sub(r'([\d]+[,\d]*)( дюйм[аов]|\")', lambda m: SM(m), regex)

print(regex)
