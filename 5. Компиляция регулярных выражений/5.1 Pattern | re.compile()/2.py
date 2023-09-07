import re


pattern = re.compile(r'\b[a-z]+\b')
result = pattern.search(input(), pos=int(input()), endpos=int(input()))

if result:
    print(result[0])
