import re


match = re.search(r"(\d+[₽$])", input())

if match:
    print(match.expand(r"Цена данного товара \1"))
