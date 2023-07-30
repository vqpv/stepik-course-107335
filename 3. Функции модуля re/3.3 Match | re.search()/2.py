import re

for i in range(1, 4):
    string = input()
    search = re.search(r'[кК]од', string)
    if search:
        print(i, search.start())
        break
else:
    print("код не найден")
