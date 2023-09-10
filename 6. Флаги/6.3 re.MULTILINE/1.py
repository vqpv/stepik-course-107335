import re, sys


text = ''.join(sys.stdin.readlines())

test1 = re.findall(r'^[\^\$]+$', text, flags=re.MULTILINE)

print(test1)
