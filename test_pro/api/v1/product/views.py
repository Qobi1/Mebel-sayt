from rest_framework.decorators import parser_classes
from rest_framework.generics import GenericAPIView
from rest_framework.exceptions import NotFound
from .serializer import ProductSerializer
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK

from app1.models import Product
from .services import *


class ProductView(GenericAPIView):
    serializer_class = ProductSerializer
    permission_classes = (AllowAny, )

    def get_object(self, pk=None):
        try:
            root = Product.objects.get(pk=pk)

        except:
            raise NotFound('Product object topilmadi')
        return root

    def get(self, requests, *args, **kwargs):
        if 'pk' in kwargs and kwargs['pk']:
            response = get_one(requests, kwargs['pk'])
        else:
            response = get_list(requests)

        return Response(response, status=HTTP_200_OK, content_type='application/json')

    def post(self, requests, *args, **kwargs):
        data = requests.data
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        root = serializer.create(serializer.data)
        root.image = data['image']
        root.save()
        response = get_one(requests, root.id)
        return Response(response, status=HTTP_200_OK, content_type='application/json')

    def put(self, requests, *args, **kwargs):
        data = requests.data
        root = self.get_object(kwargs['pk'])
        serializer = self.get_serializer(data=data, instance=root, partial=True)
        serializer.is_valid(raise_exception=True)
        root = serializer.save()
        response = get_one(requests, root.id)
        return Response(response, status=HTTP_200_OK, content_type='application/json')

    def delete(self, requests, *args, **kwargs):
        root = self.get_object(kwargs['pk'])
        root.delete()
        response = {'result': f'{root} object deleted'}
        return Response(response, status=HTTP_200_OK, content_type='application/json')


