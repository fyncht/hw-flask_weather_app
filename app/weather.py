import requests
from cachetools.func import ttl_cache
from dotenv import load_dotenv
import os

load_dotenv()  # загружаем переменные окружения из .env файла

API_KEY = os.getenv('OPENWEATHER_API_KEY')


@ttl_cache(maxsize=100, ttl=600) # кэшируем результаты на 10 минут
def fetch_weather(city):
    URL = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'
    try:
        response = requests.get(URL)
        response.raise_for_status()  # проверка на ошибки HTTP
        data = response.json()
        return data['main']['temp']
    except requests.exceptions.HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')  # логгирование или другие действия
    except Exception as err:
        print(f'An error occurred: {err}')
    return None  # Возвращаем None или подходящее значение по умолчанию


