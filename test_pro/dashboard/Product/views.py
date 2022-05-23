from django.shortcuts import render
from .services import *


def list(requests, page=None):

    product = get_product(page)
    if product and product['items']:
        ctg = product['items']
    else:
        return False

    meta = product['meta']
    a = meta['count'] // meta['per_page']

    if meta['count'] // meta['per_page']:
        a += 1

    number = [i for i in range(1, a + 1)]

    next = int(meta['current_page']) + 1
    prev = int(meta['current_page']) - 1

    if next > a:
        next = None
    if prev == 0:
        prev = None

    ctx = {
        'ctgs': ctg,
        'number': number,
        'next': next,
        'prev': prev
    }
    return render(requests, 'dashboard/Product/list.html', ctx)

