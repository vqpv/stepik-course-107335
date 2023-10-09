import re


def find_repeated(text):
    result = re.search(r'\b([a-zA-Z]+)\b.*\b\1\b', text)
    return result[1] if result else None
    
print(find_repeated(input()))
