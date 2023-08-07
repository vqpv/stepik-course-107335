import re

result = re.finditer(r'\w+', input(), 0)

for i in result:
    print(i.group())
