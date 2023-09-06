import re


res_lambda = re.sub(r'\d+', lambda m: str(int(m[0]) // 3) if int(m[0]) % 3 == 0 else m[0], input())

print(res_lambda)
