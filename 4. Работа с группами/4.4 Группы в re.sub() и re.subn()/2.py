import re

print(re.sub(r'\*(?P<word_2>[а-яА-ЯёЁa-zA-Z ]+)\*', r'<em>\g<word_2></em>',re.sub(r'\*\*(?P<word_1>[а-яА-ЯёЁa-zA-Z ]+)\*\*', r'<strong>\g<word_1></strong>', input())))
