"""
django-salatik - A Django powered salad delivery system.

(c) Copyright 2023 Yuri Pilov. All Rights Reserved. See LICENSE for details.

models.py - Model (and hence database) definitions.
        This is the core of the application structure.
"""

from django.db import models
from django.contrib.auth import get_user_model
from slugify import slugify
from random import randint
from django.utils.translation import gettext as _

User = get_user_model()


class IngredientType(models.Model):
    """
    Тип ингредиента
    """
    name = models.CharField(
        _('Due on'),
        max_length=100,
        unique=True,
    )

    slug = models.SlugField(
        _('Due on'),
        max_length=50,
        unique=True,
        help_text=_('This slug is used when building ticket ID\'s. Once set, '
                    'try not to change it or system may get messy.'),
        )

    is_available = models.BooleanField(
        _('Due on'),
        default=True,
        )

    created_at = models.DateTimeField(
        _('Due on'),
        auto_now_add=True,
        )

    updated_at = models.DateTimeField(
        _('Due on'),
        auto_now=True,
        )

    class Meta:
        verbose_name = 'Тип ингредиента'
        verbose_name_plural = 'Типы ингредиентов'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    @classmethod
    def create(cls, **kwargs):
        kwargs['slug'] = slugify(kwargs['name'])
        return cls.objects.create(**kwargs)

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    """
    Ингредиент
    """
    name = models.CharField(
        _('Due on'),
        max_length=255,
        )

    slug = models.SlugField(
        _('Due on'),
        max_length=255,
        unique=True,
        )

    photo = models.ImageField(
        _('Due on'),
        upload_to='ingredient_photos',
        null=True,
        blank=True,
        )

    type = models.ForeignKey(
        'IngredientType',
        on_delete=models.CASCADE
        )

    price_per_unit = models.DecimalField(
        _('Due on'),
        default=0,
        max_digits=8,
        decimal_places=2,
        )

    protein = models.FloatField(
        _('Due on'),
        default=0,
        null=True,
        blank=True,
        )

    fat = models.FloatField(
        _('Due on'),
        default=0,
        null=True,
        blank=True,
        )

    carbohydrates = models.FloatField(
        _('Due on'),
        default=0,
        null=True,
        blank=True,
        )

    energy = models.FloatField(
        _('Due on'),
        default=0,
        null=True,
        blank=True,
        )

    is_available = models.BooleanField(
        _('Due on'),
        default=True,
        )

    created_at = models.DateTimeField(
        _('Due on'),
        auto_now_add=True,
        )

    updated_at = models.DateTimeField(
        _('Due on'),
        auto_now=True,
        )

    class Meta:
        verbose_name = 'Ингредиент'
        verbose_name_plural = 'Ингредиенты'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    @classmethod
    def create(cls, **kwargs):
        name = kwargs.get('name')
        slug = slugify(name)
        while IngredientType.objects.filter(slug=slug).exists():
            # Если значение slug уже существует, добавляем
            # случайное число к нему
            random_number = randint(1, 100)
            slug = f"{slug}-{random_number}"

        kwargs['slug'] = slug
        return cls.objects.create(**kwargs)

    def __str__(self):
        return self.name


class Salad(models.Model):
    """
    Салат
    """
    name = models.CharField(
        _('Due on'),
        max_length=255,
        )

    slug = models.SlugField(
        _('Due on'),
        max_length=255,
        unique=True,
        )

    description = models.TextField()

    is_available = models.BooleanField(
        _('Due on'),
        default=True,
        )

    created_at = models.DateTimeField(
        _('Due on'),
        auto_now_add=True,
        )

    updated_at = models.DateTimeField(
        _('Due on'),
        auto_now=True,
        )

    creator = models.ForeignKey(
        User,
        on_delete=models.CASCADE
        )

    class Meta:
        verbose_name = 'Салат'
        verbose_name_plural = 'Салаты'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    @classmethod
    def create(cls, **kwargs):
        name = kwargs.get('name')
        slug = slugify(name)
        while IngredientType.objects.filter(slug=slug).exists():
            random_number = randint(1, 100)
            slug = f"{slug}-{random_number}"

        kwargs['slug'] = slug
        return cls.objects.create(**kwargs)

    def __str__(self):
        return self.name


class Component(models.Model):
    """
    Компонент
    """
    salad = models.ForeignKey(
        'Salad',
        on_delete=models.CASCADE
        )

    slug = models.SlugField(
        _('Due on'),
        max_length=255,
        unique=True,
        )

    ingredient = models.ForeignKey(
        'Ingredient',
        on_delete=models.CASCADE
        )

    weight = models.DecimalField(
        _('Due on'),
        max_digits=8,
        decimal_places=2,
        )

    order = models.IntegerField()

    is_available = models.BooleanField(
        _('Due on'),
        default=True,
        )

    created_at = models.DateTimeField(
        _('Due on'),
        auto_now_add=True,
        )

    updated_at = models.DateTimeField(
        _('Due on'),
        auto_now=True,
        )

    class Meta:
        verbose_name = 'Компонент'
        verbose_name_plural = 'Компоненты'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    @classmethod
    def create(cls, **kwargs):
        name = kwargs.get('name')
        slug = slugify(name)
        while IngredientType.objects.filter(slug=slug).exists():
            random_number = randint(1, 100)
            slug = f"{slug}-{random_number}"

        kwargs['slug'] = slug
        return cls.objects.create(**kwargs)

    def __str__(self):
        return f'{self.ingredient} ({self.salad})'


class Order(models.Model):
    """
    Заказ
    """
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
        )

    salad = models.ForeignKey(
        'Salad',
        on_delete=models.CASCADE
        )

    status = models.CharField(
        _('Due on'),
        max_length=255,
        )

    total_price = models.DecimalField(
        _('Due on'),
        max_digits=8,
        decimal_places=2,
        )

    created_at = models.DateTimeField(
        _('Due on'),
        auto_now_add=True,
        )

    updated_at = models.DateTimeField(
        _('Due on'),
        auto_now=True,
        )

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return f'Заказ #{self.id}'


class Payment(models.Model):
    """
    Оплата
    """
    order = models.ForeignKey(
        'Order',
        on_delete=models.CASCADE
        )

    amount = models.DecimalField(
        _('Due on'),
        max_digits=8,
        decimal_places=2,
        )

    timestamp = models.DateTimeField(
        _('Due on'),
        auto_now_add=True,
        )

    class Meta:
        verbose_name = 'Оплата'
        verbose_name_plural = 'Оплаты'

    def __str__(self):
        return f'Оплата #{self.id}'


class Delivery(models.Model):
    """
    Доставка
    """
    order = models.ForeignKey(
        'Order',
        on_delete=models.CASCADE
        )

    courier = models.ForeignKey(
        User,
        on_delete=models.CASCADE
        )

    address = models.CharField(
        _('Due on'),
        max_length=255,
        )

    status = models.CharField(
        _('Due on'),
        max_length=255,
        )

    delivery_fee = models.DecimalField(
        _('Due on'),
        max_digits=8, 
        decimal_places=2,
        )

    created_at = models.DateTimeField(
        _('Due on'),
        auto_now_add=True,
        )

    updated_at = models.DateTimeField(
        _('Due on'),
        auto_now=True,
        blank=True,
        null=True,)

    class Meta:
        verbose_name = 'Доставка'
        verbose_name_plural = 'Доставки'

    def __str__(self):
        return f'Доставка #{self.id}'
