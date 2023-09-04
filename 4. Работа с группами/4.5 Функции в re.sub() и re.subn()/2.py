import re


res_lambda = re.sub(r'\b[аА][а-яА-ЯёЁ]*\b', lambda m: f"удалено({len(m[0])})", input())

print(res_lambda)
