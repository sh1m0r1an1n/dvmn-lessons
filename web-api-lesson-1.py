import requests


def main():
    cities = ['Лондон', 'аэропорт Шереметьево', 'Череповец']
    params = {
        'nTqM': '',
        'lang': 'ru'
    }
    for city in cities:
        url = f'https://wttr.in/{city}'
        response = requests.get(url, params=params)
        response.raise_for_status()
        print(response.text)


if __name__ == '__main__':
    main()
