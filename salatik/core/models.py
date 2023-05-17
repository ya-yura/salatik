from django.db import models
from django.contrib.auth import get_user_model
from django.utils.text import slugify

User = get_user_model()


class IngredientType(models.Model):
    """
    Тип ингредиента
    """
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Тип ингредиента'
        verbose_name_plural = 'Типы ингредиентов'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    """
    Ингредиент
    """
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    photo = models.ImageField(upload_to='ingredient_photos')
    type = models.ForeignKey('IngredientType', on_delete=models.CASCADE)
    price_per_unit = models.DecimalField(max_digits=8, decimal_places=2)
    protein = models.FloatField()
    fat = models.FloatField()
    carbohydrates = models.FloatField()
    energy = models.FloatField()
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Ингредиент'
        verbose_name_plural = 'Ингредиенты'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Salad(models.Model):
    """
    Салат
    """
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    description = models.TextField()
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Салат'
        verbose_name_plural = 'Салаты'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Component(models.Model):
    """
    Компонент
    """
    salad = models.ForeignKey('Salad', on_delete=models.CASCADE)
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    ingredient = models.ForeignKey('Ingredient', on_delete=models.CASCADE)
    weight = models.DecimalField(max_digits=8, decimal_places=2)
    order = models.IntegerField()
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Компонент'
        verbose_name_plural = 'Компоненты'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.ingredient} ({self.salad})'


class Order(models.Model):
    """
    Заказ
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    salad = models.ForeignKey('Salad', on_delete=models.CASCADE)
    status = models.CharField(max_length=255)
    total_price = models.DecimalField(max_digits=8, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return f'Заказ #{self.id}'


class Payment(models.Model):
    """
    Оплата
    """
    order = models.ForeignKey('Order', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Оплата'
        verbose_name_plural = 'Оплаты'

    def __str__(self):
        return f'Оплата #{self.id}'


class Delivery(models.Model):
    """
    Доставка
    """
    order = models.ForeignKey('Order', on_delete=models.CASCADE)
    courier = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    delivery_fee = models.DecimalField(max_digits=8, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Доставка'
        verbose_name_plural = 'Доставки'

    def __str__(self):
        return f'Доставка #{self.id}'
