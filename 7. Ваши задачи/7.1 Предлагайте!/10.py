import re


s = input()

print(bool(re.match(r'(?=.*\d)[^_]{6,}', s) and s != s.lower() and s != s.upper()))
