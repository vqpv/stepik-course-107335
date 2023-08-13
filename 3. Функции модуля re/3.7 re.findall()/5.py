import re

result = re.findall(r'(?:(?<=<a class=\"link\" href=\")|(?<=<a target=\"_blank\" href=\")).*?(?=\")(?=.*?<\/a>)', input())

for url in result:
    print(url)
