import re

result = re.finditer(r'[\d,]+ ₽', input(), 0)

for i in result:
    print(i.group())
