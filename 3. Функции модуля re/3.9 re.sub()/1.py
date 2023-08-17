import re

result = re.sub(r'[aeioyuAEIOUауоыиэяюёеАУОЫИЭЯЮЁЕ]', "!", input())

print(result)
