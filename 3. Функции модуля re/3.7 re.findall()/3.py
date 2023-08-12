import re

result = re.findall(r'(?:\d{4}\.\d{2}\.\d{2})|(?:\d{2}\.\d{2}\.\d{4})|(?:\d{4}\/\d{2}\/\d{2})|(?:\d{2}\/\d{2}\/\d{4})', input())

for date in result:
    print(date)
