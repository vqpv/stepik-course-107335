import re

print(re.sub(r'(его|её|их|Его|Её|Их)[а-яА-ЯёЁ]+', r'\1', input()))
