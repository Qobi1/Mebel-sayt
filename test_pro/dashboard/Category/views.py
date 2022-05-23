from django.shortcuts import render, redirect

from app1.models import Category
from .forms import CategoryForm
from .services import *


def list(requests, page=None):

    ctgs = get_ctg(page)
    if ctgs and ctgs['items']:
        ctg = ctgs['items']
    else:
        return False

    meta = ctgs['meta']
    a = meta['count'] // meta['per_page']

    if meta['count'] % meta['per_page']:
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
    return render(requests, 'dashboard/Category/list.html', ctx)


def ctg_detail(requests, pk=None, delete=None):
    ctg = ctg_get_one(pk=pk, delete=delete)
    if delete:
        return redirect('dashboard_ctg_list')
    ctx = {
        'ctg': ctg
    }

    return render(requests, 'dashboard/Category/details.html', ctx)


def add(requests, pk=None):
    try:
        instance = Category.objects.get(id=pk)
    except:
        instance = None
    form = CategoryForm(instance=instance)
    if requests.POST:
        forms = CategoryForm(requests.POST, requests.FILES, instance=instance)
        if forms.is_valid():
            forms.save()
            return redirect('dashboard_ctg_list')
        else:
            print('Error ', forms.errors)
    ctx = {
        'form': form
    }
    return render(requests, 'dashboard/Category/forms.html', ctx)

