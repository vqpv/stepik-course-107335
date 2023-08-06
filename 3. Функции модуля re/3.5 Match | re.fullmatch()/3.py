import re

print(bool(re.fullmatch('\+?[\d]+([( )-]{0,2}[\d]{3,}){2}([( )-]{0,2}[\d]{2,}){2}', input())))
