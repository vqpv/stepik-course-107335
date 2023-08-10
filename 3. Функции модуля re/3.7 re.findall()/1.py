import re

result = re.findall(r'https://imgur.com/[a-zA-Z\d]{7}', input())

for url in result:
    print(url)
