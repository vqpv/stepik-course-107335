import re

result = re.split(r'[^\d]*([\+:=\*\/-])[^\d]*', input())

print(result)
