import re

for i in range(5):
    string = input()
    search = re.search(r'(?<=Activation key: )([A-Z\d]{5}(-[A-Z\d]{5}){4})', string)
    if search:
        print(search.group())
        break
