import re

if seed := re.match(r'([a-z]+[^\d,.] ?){12,24}', input()):
    print("возможно, это seed-фраза")
