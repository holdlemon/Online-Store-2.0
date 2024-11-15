from django.db import models

from users.models import User

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Категория', help_text='Введите название категории')
    description = models.TextField(verbose_name='Описание', help_text='Введите описание категории')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = [
            'name',
        ]

class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Продукт', help_text='Введите название продукта')
    description = models.TextField(verbose_name='Описание', help_text='Введите описание продукта')
    image = models.ImageField(upload_to='image/', blank=True, null=True, verbose_name='Изображение')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, related_name='products', verbose_name='Категория')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Стоимость')
    is_published = models.BooleanField(default=True, verbose_name="Статус публикации")
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, related_name='user_products', verbose_name='Владелец')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = [
            'name',
        ]
        permissions = [
            ('can_unpublish_product', 'Can unpublish product')
        ]