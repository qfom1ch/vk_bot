import requests

from config import CURRENCY_TOKEN


def get_currency():
    url = (f'http://api.currencylayer.com/live?access_key={CURRENCY_TOKEN}&'
           f'currencies=RUB,EUR,JPY,GBP,AUD')
    request = requests.get(url)
    currency = dict(request.json())['quotes']
    return dict(currency)
