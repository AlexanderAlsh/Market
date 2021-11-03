from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView

from .models import *
from django.core.paginator import Paginator



""" Страница с телефонами """


def phones(request):
    products = Smartphones.objects.all()
    paginator = Paginator(products, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'online_shop/smartphone.html', {'page_obj': page_obj})


def product_detail_phones(request, id):
    get_one = get_object_or_404(Smartphones, pk=id)
    return render(request, 'online_shop/detail.html', {'get_one': get_one})


class SmartFilter(ListView):
    template_name = 'online_shop/filter.html'

    def get_queryset(self):
        queryset = Smartphones.objects.filter(brand=self.request.GET.getlist('brand'))
        return queryset



""" Страница с телевизорами """


def television(request):
    if request.method == 'GET':
        products = Television.objects.all()
        paginator = Paginator(products, 6)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, 'online_shop/tv.html', {'page_obj': page_obj})


def product_detail_television(request, id):
    get_one = get_object_or_404(Television, pk=id)
    return render(request, 'online_shop/detail_tv.html', {'get_one': get_one})


""" Страница с пылесосами """


def cleaner(request):
    if request.method == 'GET':
        products = Cleaner.objects.all()
        paginator = Paginator(products, 6)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, 'online_shop/cleaner.html', {'page_obj': page_obj})


def product_detail_cleaner(request, id):
    get_one = get_object_or_404(Cleaner, pk=id)
    return render(request, 'online_shop/detail_cleaner.html', {'get_one': get_one})


""" Страница с ноутбуками """


def notebooks(request):
    if request.method == 'GET':
        products = Notebooks.objects.all()
        paginator = Paginator(products, 6)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, 'online_shop/notebook.html', {'page_obj': page_obj})


def product_detail_notebooks(request, id):
    get_one = get_object_or_404(Notebooks, pk=id)
    return render(request, 'online_shop/detail_notebook.html', {'get_one': get_one})


""" Страница с холодильниками """


def fridge(request):
    if request.method == 'GET':
        products = Fridge.objects.all()
        paginator = Paginator(products, 6)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, 'online_shop/fridge.html', {'page_obj': page_obj})


def product_detail_fridge(request, id):
    get_one = get_object_or_404(Fridge, pk=id)
    return render(request, 'online_shop/detail_fridge.html', {'get_one': get_one})


""" Страница с микроволновками """


def defrost(request):
    if request.method == 'GET':
        products = Defrost.objects.all()
        paginator = Paginator(products, 6)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, 'online_shop/defrost.html', {'page_obj': page_obj})


def product_detail_defrost(request, id):
    get_one = get_object_or_404(Defrost, pk=id)
    return render(request, 'online_shop/detail_defrost.html', {'get_one': get_one})


""" Страница с стриальными машинами """


def washing(request):
    if request.method == 'GET':
        products = Washing.objects.all()
        paginator = Paginator(products, 6)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, 'online_shop/washing.html', {'page_obj': page_obj})


def product_detail_washing(request, id):
    get_one = get_object_or_404(Washing, pk=id)
    return render(request, 'online_shop/detail_washing.html', {'get_one': get_one})


""" Другие страницы """


'''class ProductViewList(ListView):
    model = Smartphones
    template_name = "online_shop/smartphone.html"

    def get_queryset(self):
        queryset = Smartphones.objects.get(
            Q(category=self.request.GET.get('sim'))
        )
        return queryset'''


def catalog(request):
    menu_items = Catalog.objects.all()
    return render(request, 'online_shop/catalog.html', {
        "menu_items": menu_items,
    })


def index(request):
    products = Slider.objects.all()
    return render(request, 'online_shop/index.html', {'products': products})


def dostavka(request):
    return render(request, 'online_shop/dostavka.html')
