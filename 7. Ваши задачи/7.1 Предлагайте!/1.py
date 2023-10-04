import re


result = re.findall(r'[A-Z][a-z]*|\d+', input())

print('_'.join(result).lower())
