from django.urls import path
from .views import *
from .Category import views as ctg_view
from .Product import views as product_view

urlpatterns = [
    path('', home, name="home"),
    path('ctg/list/', ctg_view.list, name='dashboard_ctg_list'),
    path('ctg/list/<int:page>/', ctg_view.list, name='dashboard_ctg_list_page'),
    path('ctg/detail/<int:pk>/', ctg_view.ctg_detail, name='dashboard_ctg_detail'),
    path('ctg/edit/<int:pk>/', ctg_view.add, name='dashboard_ctg_edit'),
    path('ctg/<int:delete>/', ctg_view.ctg_detail, name='dashboard_ctg_delete'),
    path('ctg/add/', ctg_view.add, name='dashboard_ctg_add'),


    path('product/list/', product_view.list, name='dashboard_product_list'),
    path('product/list/<int:page>', product_view.list, name='dashboard_product_list_page'),

]

