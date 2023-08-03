import re

if string := re.match(r'.+(?=@)', input()):
    print(string[0])
