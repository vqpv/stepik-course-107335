import re, sys


text = ''.join(sys.stdin.readlines())

print(re.findall(r'(?<=start).+(?=end)', text, flags=re.S))
