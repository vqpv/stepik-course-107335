import re

search = re.search(r't=[\d.+]+', input())

if search:
    print(search[0])
