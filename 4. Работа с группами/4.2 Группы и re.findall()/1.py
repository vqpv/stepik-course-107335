import re

result = re.findall(r'<\/?([a-z\d]+).*?>', input())

print(result)
