import requests
import json
from config import keys


class APIException(Exception):
    pass


class CurrencyConverter:
    @staticmethod
    def get_price(base: str, quote: str, amount: str):

        if base == quote:
            raise APIException(f'Невозможно перевести одинаковые валюты {base}.')

        try:
            base_ticker = keys[base]
        except KeyError:
            raise APIException(f'Не удалось обработать валюту {base}.')

        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise APIException(f'Не удалось обработать валюту {quote}.')

        try:
            amount = float(amount)
        except ValueError:
            raise APIException(f'Не удалось обработать количество {amount}.')



        r = requests.get(
            f'https://currate.ru/api/?get=rates&pairs={base_ticker}{quote_ticker}&key=69e919c754f9b477a8a679c08fc58069')
        total_base = json.loads(r.content)['data'][base_ticker + quote_ticker]

        return float(total_base) * amount
