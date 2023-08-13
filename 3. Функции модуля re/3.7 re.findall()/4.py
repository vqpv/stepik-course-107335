import re

result = re.findall(r'((?:(?:[0-1][0-9])|(?:[2][0-3])):(?:[0-5][0-9]))', input())

for t in result:
    print(t)
