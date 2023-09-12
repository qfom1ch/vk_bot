import requests
from bs4 import BeautifulSoup
from slugify import slugify


def get_afisha(city: str, *, tomorrow=False):
    if city.lower() == 'москва':
        city = 'msk'

    if tomorrow is True:
        url = (f'https://www.afisha.ru/{slugify(city).lower()}/events/'
               f'na-zavtra/')
    else:
        url = (f'https://www.afisha.ru/{slugify(city).lower()}/events/'
               f'na-segodnya/')

    name_events = []
    res_type_events = []
    res_lnks = []

    request = requests.get(url)
    soup = BeautifulSoup(request.text, 'html.parser')
    events = soup.find_all("div", class_="mQ7Bh", limit=5)
    for event in events:
        name_events.append(str(event)[19:-6])

    types_events = soup.find_all("span", class_="MVlCc", limit=5)
    for type_event in types_events:
        res_type_events.append(str(type_event)[49:-7])

    links = soup.find_all("a", class_="vcSoT b6DKO jkBWH f5gWK", limit=5)
    len_name = [len(name) for name in name_events]
    name_count = 0
    for link in links:
        res_lnks.append(
            'https://www.afisha.ru' + str(link)[77:-len_name[name_count] - 31])
        name_count += 1

    return list(zip(name_events, res_type_events, res_lnks))
