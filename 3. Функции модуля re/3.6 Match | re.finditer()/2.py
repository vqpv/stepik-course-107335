import re

result = re.finditer(r'\b[a-zA-Zа-яА-ЯёЁ]{5}\b', input(), 0)

for i in result:
    print(i.group())
