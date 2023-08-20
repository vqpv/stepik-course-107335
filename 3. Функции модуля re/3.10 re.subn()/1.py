import re

result = re.subn(r'[.?!,:]', '', input())

print(result[1])
