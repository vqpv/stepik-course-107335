import re

result = re.sub(r'<[^>]*>', "", input())

print(result)
