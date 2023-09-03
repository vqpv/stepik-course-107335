import re


res_lambda = re.sub(r'\d+', lambda m: str(int(m[0]) ** 2), input())

print(res_lambda)
