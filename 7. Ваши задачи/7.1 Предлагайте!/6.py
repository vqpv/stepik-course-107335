import re


consonants = '[bcdfghjklmnpqrstvwxyz]'
vowels = '[aeiouy]'

pattern = re.compile(fr'\b(?:{consonants}{vowels})+{consonants}*\b|\b(?:{vowels}{consonants})+{vowels}*\b', flags=re.I)

print(*pattern.findall(input()))
