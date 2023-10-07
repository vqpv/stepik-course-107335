import re


string = input()

print(re.sub(r'.{5}$', re.match(r'.{1,5}', string)[0], string))
