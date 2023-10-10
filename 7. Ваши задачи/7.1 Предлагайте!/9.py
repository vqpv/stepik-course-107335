import re


def is_prime(num):
    return len([i for i in range(1, num + 1) if num % i == 0]) == 2

regex = re.findall(r'x+', input())

print(*[j for j in regex if is_prime(len(j))])
