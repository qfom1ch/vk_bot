from slugify import slugify


def get_traffic(city: str):
    if city.lower() == 'москва':
        city = 'moscow'
    return f'https://2gis.ru/{slugify(city)}?traffic'
