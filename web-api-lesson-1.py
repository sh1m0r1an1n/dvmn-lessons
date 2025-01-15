import requests
from urllib.parse import quote


def main():
    city = input('Введите местоположение: ')
    url = f'https://wttr.in/{quote(city)}?nTqM&lang=ru'

    try:
        response = requests.get(url)
        response.raise_for_status()
        response.encoding = 'utf-8'
        print(response.text)
    except requests.exceptions.RequestException as error:
        print(f"Ошибка при запросе: {error}")


if __name__ == '__main__':
    main()
