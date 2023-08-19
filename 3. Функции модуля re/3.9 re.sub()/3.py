import re

a, b, c = input().split()

result = re.sub(fr'({a[:-2]}[а-я]{{2,4}} {b[0]}\. {c[0]}\.)|({a[:-2]}[а-я]{{2,4}} {b[:-2]}[а-я]{{2,4}} {c[:-2]}[а-я]{{2,4}})', "ФИО", input())

print(result)
