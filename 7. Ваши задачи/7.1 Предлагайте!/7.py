import re


regex = re.fullmatch(r'(?:(?:(?:\b\d\b)|(?:\b[1-9]\d\b)|(?:\b[1-2][0-5]{2}\b))\.*){4}', input())

print(bool(regex))
