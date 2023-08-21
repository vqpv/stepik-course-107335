import re

result = re.subn(r'\d', 'X', input())

print(result)
