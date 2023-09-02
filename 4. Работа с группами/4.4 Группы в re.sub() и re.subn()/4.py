import re

print(re.sub(r'([\d]{2}[./])([\d]{2}[./])([\d]{4})', r'\2\1\3', input()))
