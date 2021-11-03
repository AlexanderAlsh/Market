import datetime
from django.db import models


class Smartphones(models.Model):
    """ Смартфоны """
    title = models.CharField(max_length=100, null=False, verbose_name='Название')
    content = models.TextField(null=False, verbose_name='Описание')
    price = models.IntegerField(null=False, verbose_name='Цена товара')
    image = models.ImageField(verbose_name='Фото', blank=True)
    diag = models.IntegerField(verbose_name='Диагональ экрана')
    brand = models.CharField(max_length=100, null=False, verbose_name='Производитель')
    SIM = models.IntegerField(verbose_name='Кол-во симкарт')
    category = models.CharField(max_length=100, default='smartphones', verbose_name='Категория')

    created_at = models.DateTimeField(default=datetime.datetime.now())

    class Meta:
        verbose_name = 'Смартфон'
        verbose_name_plural = 'Смартфоны'


class Television(models.Model):
    """ Телевизоры """
    title = models.CharField(max_length=100, null=False, verbose_name='Название')
    content = models.TextField(null=False, verbose_name='Описание')
    price = models.IntegerField(null=False, verbose_name='Цена товара')
    image = models.ImageField(verbose_name='Фото', blank=True)
    diag = models.IntegerField(verbose_name='Диагональ экрана')
    brand = models.CharField(max_length=100, null=False, verbose_name='Производитель')
    category = models.CharField(max_length=100, default='Television', verbose_name='Категория')

    created_at = models.DateTimeField(default=datetime.datetime.now())

    class Meta:
        verbose_name = 'Телевизор'
        verbose_name_plural = 'Телевизоры'


class Cleaner(models.Model):
    """ Пылесос """
    title = models.CharField(max_length=100, null=False, verbose_name='Название')
    content = models.TextField(null=False, verbose_name='Описание')
    price = models.IntegerField(null=False, verbose_name='Цена товара')
    image = models.ImageField(verbose_name='Фото', blank=True)
    brand = models.CharField(max_length=100, null=False, verbose_name='Производитель')
    category = models.CharField(max_length=100, default='Cleaner', verbose_name='Категория')

    created_at = models.DateTimeField(default=datetime.datetime.now())

    class Meta:
        verbose_name = 'Пылесос'
        verbose_name_plural = 'Пылесосы'


class Notebooks(models.Model):
    """ Ноутбуки """
    title = models.CharField(max_length=100, null=False, verbose_name='Название')
    content = models.TextField(null=False, verbose_name='Описание')
    price = models.IntegerField(null=False, verbose_name='Цена товара')
    image = models.ImageField(verbose_name='Фото', blank=True)
    diag = models.IntegerField(verbose_name='Диагональ экрана')
    brand = models.CharField(max_length=100, null=False, verbose_name='Производитель')
    category = models.CharField(max_length=100, default='notebooks', verbose_name='Категория')
    CPU = models.CharField(max_length=100, null=False, verbose_name='Процессор')
    GPU = models.CharField(max_length=100, null=False, verbose_name='Процессор')

    created_at = models.DateTimeField(default=datetime.datetime.now())

    class Meta:
        verbose_name = 'Ноутбук'
        verbose_name_plural = 'Ноутбуки'


class Fridge(models.Model):
    """ Холодильники """
    title = models.CharField(max_length=100, null=False, verbose_name='Название')
    content = models.TextField(null=False, verbose_name='Описание')
    price = models.IntegerField(null=False, verbose_name='Цена товара')
    image = models.ImageField(verbose_name='Фото', blank=True)
    brand = models.CharField(max_length=100, null=False, verbose_name='Производитель')
    category = models.CharField(max_length=100, default='fridge', verbose_name='Категория')

    created_at = models.DateTimeField(default=datetime.datetime.now())

    class Meta:
        verbose_name = 'Холодильник'
        verbose_name_plural = 'Холодильники'


class Defrost(models.Model):
    """ Микровлоновки """
    title = models.CharField(max_length=100, null=False, verbose_name='Название')
    content = models.TextField(null=False, verbose_name='Описание')
    price = models.IntegerField(null=False, verbose_name='Цена товара')
    image = models.ImageField(verbose_name='Фото', blank=True)
    brand = models.CharField(max_length=100, null=False, verbose_name='Производитель')
    category = models.CharField(max_length=100, default='defrost', verbose_name='Категория')

    created_at = models.DateTimeField(default=datetime.datetime.now())

    class Meta:
        verbose_name = 'Микроволновка'
        verbose_name_plural = 'Микроволновки'


class Washing(models.Model):
    """ Стиральные машины """
    title = models.CharField(max_length=100, null=False, verbose_name='Название')
    content = models.TextField(null=False, verbose_name='Описание')
    price = models.IntegerField(null=False, verbose_name='Цена товара')
    image = models.ImageField(verbose_name='Фото', blank=True)
    brand = models.CharField(max_length=100, null=False, verbose_name='Производитель')
    category = models.CharField(max_length=100, default='washing', verbose_name='Категория')

    created_at = models.DateTimeField(default=datetime.datetime.now())

    class Meta:
        verbose_name = 'Стиральная машина'
        verbose_name_plural = 'Стиральные машины'


class Catalog(models.Model):
    """ Меню категорий """
    title = models.CharField(max_length=100, null=False, verbose_name='Название')
    image = models.ImageField(verbose_name='Фото', blank=True)
    url = models.CharField(max_length=100, null=False, verbose_name='Ссылка')

    def __str__(self):
        return str(self.title)

    class Meta:
        verbose_name = 'Пункт меню'
        verbose_name_plural = 'Пункты меню'


class Slider(models.Model):
    """ Слайдер на главном экране """
    title = models.CharField(max_length=100, null=False, verbose_name='Название')
    content = models.CharField(max_length=100, null=False, verbose_name='Краткое описание')
    url = models.CharField(max_length=100, null=False, verbose_name='Ссылка')
    image = models.ImageField(verbose_name='Фото', blank=True)

    class Meta:
        verbose_name = 'Слайдер'
        verbose_name_plural = 'Слайдеры'

'''
class Cart(models.Model):
    """ Корзина """
    products = models.ManyToManyField('CartProduct', blank=True, related_name='related_cart')
    final_price = models.IntegerField(default=0, verbose_name='Общая цена')

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'



class CartProduct(models.Model):
    """ Объект корзины """
    product = models.ForeignKey(Content, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1, blank=True)
    final_price = models.IntegerField(verbose_name='Общая цена', blank=True)

    def save(self, *args, **kwargs):
        self.final_price = self.quantity * self.product.price
        super().save(*args, **kwargs)

    def __str__(self):
        return "Объект: {} (для корзины)".format(self.product.title)

    class Meta:
        verbose_name = 'Объект корзины'
        verbose_name_plural = 'Объекты корзины'
        
        
class Order(models.Model):
    """ Заказ """
    products = models.ManyToManyField('OrderItem', blank=True, related_name='related_order')
    billid = models.CharField(max_length=200)
    comment = models.TextField(default='BagleyEcommerce')
    final_price = models.IntegerField(default=1)
    paid = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'


class OrderItem(models.Model):
    """ Предмет заказа """
    product = models.ForeignKey(Content, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1, blank=True)
    final_price = models.IntegerField(verbose_name='Общая цена', blank=True)

    def save(self, *args, **kwargs):
        self.final_price = self.quantity * self.product.price
        super().save(*args, **kwargs)

    def __str__(self):
        return "Объект: {} (заказ)".format(self.product.title)

    class Meta:
        verbose_name = 'Объект заказа'
        verbose_name_plural = 'Объекты заказа'''''