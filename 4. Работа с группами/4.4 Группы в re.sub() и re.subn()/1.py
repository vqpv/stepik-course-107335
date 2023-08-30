import re

print(re.sub(r'(?P<word>[а-яА-ЯёЁ]+) (?P=word)', r'\g<word>', input()))
