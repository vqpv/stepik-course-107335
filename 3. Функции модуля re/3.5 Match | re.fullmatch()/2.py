import re

print(bool(re.fullmatch('[a-zA-Z\d@#$%^&*\(\)_\-\+!?]{8,}', input())))
