import requests
import os
from dotenv import load_dotenv
from urllib.parse import urlparse


def api_request(url_method: str, params: dict) -> dict:
    try:
        response = requests.get(url_method, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as error:
        print(f"Ошибка при запросе к API: {error}")
        return {}


def shorten_link(token: str, url: str) -> str:
    params = {
        'url': url,
        'access_token': token,
        'v': '5.199'
    }
    url_method = 'https://api.vk.com/method/utils.getShortLink'
    response_data = api_request(url_method, params)

    if 'response' in response_data:
        return response_data['response']['short_url']
    else:
        raise ValueError("Ошибка API: не удалось получить короткую ссылку")


def count_clicks(token: str, short_url_key: str) -> int:
    params = {
        'key': short_url_key,
        'interval': 'forever',
        'access_token': token,
        'v': '5.199'
    }
    url_method = 'https://api.vk.com/method/utils.getLinkStats'
    response_data = api_request(url_method, params)

    if 'response' in response_data:
        stats = response_data['response']['stats']
        return stats[0]['views'] if stats else 0
    else:
        raise ValueError("Ошибка API: не удалось получить данные о кликах")


def validate_url(url: str) -> bool:
    try:
        response = requests.get(url)
        response.raise_for_status()
        return True
    except requests.exceptions.HTTPError:
        return False


def is_shorten_link(url: str) -> bool:
    return urlparse(url).netloc == 'vk.cc'


def main():
    load_dotenv()
    token = os.getenv('VK_TOKEN')

    if not token:
        print("Токен VK отсутствует. Проверьте файл .env.")
        return

    url = input('Введите ссылку: ')

    if not validate_url(url):
        print("Некорректный URL. Попробуйте снова.")
        return

    try:
        if not is_shorten_link(url):
            short_link = shorten_link(token, url)
            print('Сокращенная ссылка: ', short_link)
        else:
            short_link = url
    except (requests.exceptions.RequestException, ValueError) as error:
        print(f'Ошибка при создании короткой ссылки: {error}')
        return

    parsed_url = urlparse(short_link)
    short_url_key = parsed_url.path.lstrip("/")

    try:
        if is_shorten_link(url):
            click_count = count_clicks(token, short_url_key)
            print(f'Количество кликов по ссылке: {click_count}')
    except (requests.exceptions.RequestException, ValueError) as error:
        print(f'Ошибка при подсчете кликов: {error}')


if __name__ == '__main__':
    main()
