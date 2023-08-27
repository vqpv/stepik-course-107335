import re

result = re.findall(r'([\d]+):([a-zA-Z\d]+):([a-z\d]+)', input())

print(result)
