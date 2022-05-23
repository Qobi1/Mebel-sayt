from collections import OrderedDict
from contextlib import closing

from django.db import connection

from api.v1.sqlpaginator import SqlPaginator
from test_pro.settings import PAGINATE_BY


def dictfetchall(cursor):
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]


def dictfetchone(cursor):
    row = cursor.fetchone()
    if row is None:
        return False
    columns = [col[0] for col in cursor.description]
    return dict(zip(columns, row))


def get_list(requests):
    params = requests.query_params.getlist('ctg')
    print('>>>>>>>', params)

    if params:
        extra_sql = 'where '
        for i in params:
            if i == params[-1]:
                extra_sql += f"( content like '%{i}%')"
            else:
                extra_sql += f"( content like '%{i}%') or"

    else:
        extra_sql = ''
    page = requests.query_params.get('page', 0)

    sql = f"""Select * from app1_category {extra_sql}
              order by id 
              limit %s OFFSET %s"""

    offset = (int(page) - 1) * PAGINATE_BY

    with closing(connection.cursor()) as cursor:
        cursor.execute(sql, [PAGINATE_BY, offset])
        result = dictfetchall(cursor)

    with closing(connection.cursor()) as cursor:
        cursor.execute(f'SELECT count(1) as cnt from app1_category {extra_sql}')
        root = dictfetchone(cursor)
    if root:
        cnt = root['cnt']
    else:
        cnt = 0

    sqlpaginator = SqlPaginator(requests, page=page, per_page=PAGINATE_BY, count=cnt)
    pagging = sqlpaginator.get_paginated_response(per_page=PAGINATE_BY, current_page=page)
    return OrderedDict([
        ('items', result),
        ('meta', pagging),
    ])


def get_one(requests, pk):
    sql = "Select * from app1_category where id=%s"
    with closing(connection.cursor()) as cursor:
        cursor.execute(sql, [pk])
        result = dictfetchone(cursor)
    return result

