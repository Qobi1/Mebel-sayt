import requests as re

from test_pro.settings import API_URL


def get_product(page):
    if not page:
        page = 1
    url = API_URL + f'product/?page={page}'
    ctgs = re.get(url)
    if ctgs.status_code == 200:
        return ctgs.json()
    return False

