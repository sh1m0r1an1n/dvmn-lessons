import requests
import os
from dotenv import load_dotenv
from urllib.parse import urlparse


def shorten_link(token: str, url: str) -> str:
    params = {
        'url': url,
        'access_token': token,
        'v': '5.199'
    }
    url_method = 'https://api.vk.com/method/utils.getShortLink'

    response = requests.get(url_method, params=params)
    response.raise_for_status()
    response_data = response.json()

    if 'error' in response_data:
        raise ValueError(f"Ошибка API: {response_data['error']['error_msg']}")
    return response_data['response']['short_url']


def count_clicks(token: str, key: str) -> int:
    params = {
        'key': key,
        'interval': 'forever',
        'access_token': token,
        'v': '5.199'
    }
    url_method = 'https://api.vk.com/method/utils.getLinkStats'

    response = requests.get(url_method, params=params)
    response.raise_for_status()
    response_data = response.json()

    if 'error' in response_data:
        raise ValueError(f"Ошибка API: {response_data['error']['error_msg']}")
    stats = response_data['response']['stats']
    return stats[0]['views'] if stats else 0


def is_shorten_link(token: str, key: str) -> bool:
    params = {
        'key': key,
        'interval': 'forever',
        'access_token': token,
        'v': '5.199'
    }
    url_method = 'https://api.vk.com/method/utils.getLinkStats'

    response = requests.get(url_method, params=params)
    response.raise_for_status()
    return 'error' not in response.json()


def main():
    load_dotenv()
    token = os.environ['VK_TOKEN']

    url = input('Введите ссылку: ')
    key = urlparse(url).path.lstrip("/")

    try:
        if is_shorten_link(token, key):
            click_count = count_clicks(token, key)
            print('Количество кликов по ссылке: ', click_count)
        else:
            short_link = shorten_link(token, url)
            print('Сокращенная ссылка: ', short_link)

    except requests.exceptions.RequestException as error:
        print(f'Ошибка: {error}')


if __name__ == '__main__':
    main()
