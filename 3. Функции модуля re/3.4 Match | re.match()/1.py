import re

if word := re.match(r'[a-zA-Z]+', input()):
    print("Первое слово в предложении:", word[0])
