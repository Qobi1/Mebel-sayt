import requests as re

from test_pro.settings import API_URL


def get_ctg(page):
    if not page:
        page = 1
    url = API_URL + f'category/?page={page}'
    ctgs = re.get(url)
    if ctgs.status_code == 200:
        return ctgs.json()
    return False


def ctg_get_one(pk=None, delete=None):
    url = API_URL + f'category/{pk or delete}'

    if delete:
        ctg = re.delete(url)
    else:
        ctg = re.get(url)
    if ctg.status_code == 200:
        return ctg.json()
    return False


