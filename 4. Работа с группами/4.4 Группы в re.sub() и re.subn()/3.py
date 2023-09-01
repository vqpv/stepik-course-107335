import re

print(re.sub(r'((\d+.){4}:[\d]+)', r'http://\1', input()))
