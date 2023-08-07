import re

print(bool(re.fullmatch('(-?\d*x(\^\d+)?)?((\+|\-)\d*x(\^\d+)?)*((\+|\-)\d+)?', input())))
