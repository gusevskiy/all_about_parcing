import requests

cookies = {
    # '34f480ee50e464f35420ed3252a75b5a': '445ca36bc1d2b2e497406e03e96bc12f',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/116.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive',
    # 'Cookie': '34f480ee50e464f35420ed3252a75b5a=445ca36bc1d2b2e497406e03e96bc12f',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-User': '?1',
}

response = requests.get('https://ormaton.ru/contacts/nn', cookies=cookies, headers=headers)

#  save result as file
with open('result.html', 'w', encoding='utf-8') as file:
    file.write(response.text)