import re

urls = re.finditer(r'(https?):\/\/([a-z\.]+(?:com|ru|org))[a-z0-9-_\/]*(\?[a-z=&0-9]+)?(#[a-z]+)?', input()) 

for url in urls:
    print(f'Полная ссылка: {url[0]}')
    print(f'Протокол: {url[1] if url[1] else "None"} | Домен: {url[2] if url[2] else "None"} | Параметры: {url[3] if url[3] else "None"} | Якорь: {url[4] if url[4] else "None"}')
    print()
