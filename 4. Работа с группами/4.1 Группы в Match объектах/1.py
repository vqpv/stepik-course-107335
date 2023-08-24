import re

result = re.findall(r'<p[^><]*?>(.*?)<\/p>', input())

print(*result, sep="\n")
