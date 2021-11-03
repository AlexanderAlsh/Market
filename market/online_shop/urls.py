from django.urls import path

from . import views


urlpatterns = [
    path('', views.index),
    path('catalog/', views.catalog, name='catalog'),
    path('smartphones/', views.phones, name='smartphones'),
    path('detail/<int:id>', views.product_detail_phones),
    path('television/', views.television, name='television'),
    path('detail_tv/<int:id>', views.product_detail_television),
    path('сleaners/', views.cleaner, name='сleaners'),
    path('detail_сleaner/<int:id>', views.product_detail_cleaner),
    path('notebooks/', views.notebooks, name='notebooks'),
    path('detail_notebook/<int:id>', views.product_detail_notebooks),
    path('fridge/', views.fridge, name='fridge'),
    path('detail_fridge/<int:id>', views.product_detail_fridge),
    path('defrost/', views.defrost, name='defrost'),
    path('detail_defrost/<int:id>', views.product_detail_defrost),
    path('washing/', views.washing, name='washing'),
    path('detail_washing/<int:id>', views.product_detail_washing),
    path('dostavka/', views.dostavka),
    #path('filter/', views.ProductViewList.as_view(), name='filter')
    path('list/', views.SmartFilter.as_view(), name='list')

]
