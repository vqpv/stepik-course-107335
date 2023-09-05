import re


res_lambda = re.sub(r'[ap]m', lambda m: {"am": "pm", "pm": "am"}[m[0]], input())

print(res_lambda)
