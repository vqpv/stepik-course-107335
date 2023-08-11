import re

result = re.findall(r'\b[a-zA-Z\d\-_]+@[a-zA-Z\d]+\.[a-zA-Z\d]{1,3}\b', input())

for mail in result:
    print(mail)
