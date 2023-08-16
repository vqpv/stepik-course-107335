import re

result = re.split(r'Категория: [а-яА-ЯёЁ ]+\\n', input())

print(result)
