
from django.db import models


class User(models.Model):
    """
    Пользователь
    """
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    bio = models.TextField()
    role = models.ForeignKey('Role', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username


class Role(models.Model):
    """
    Роль
    """
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Роль'
        verbose_name_plural = 'Роли'

    def __str__(self):
        return self.name


class IngredientType(models.Model):
    """
    Тип ингредиента
    """
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Тип ингредиента'
        verbose_name_plural = 'Типы ингредиентов'

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    """
    Ингредиент
    """
    name = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='ingredient_photos')
    type = models.ForeignKey('IngredientType', on_delete=models.CASCADE)
    price_per_unit = models.DecimalField(max_digits=8, decimal_places=2)
    protein = models.FloatField()
    fat = models.FloatField()
    carbohydrates = models.FloatField()
    energy = models.FloatField()

    class Meta:
        verbose_name = 'Ингредиент'
        verbose_name_plural = 'Ингредиенты'

    def __str__(self):
        return self.name


class Salad(models.Model):
    """
    Салат
    """
    name = models.CharField(max_length=255)
    description = models.TextField()

    class Meta:
        verbose_name = 'Салат'
        verbose_name_plural = 'Салаты'

    def __str__(self):
        return self.name


class Component(models.Model):
    """
    Компонент
    """
    salad = models.ForeignKey('Salad', on_delete=models.CASCADE)
    ingredient = models.ForeignKey('Ingredient', on_delete=models.CASCADE)
    weight = models.DecimalField(max_digits=8, decimal_places=2)
    order = models.IntegerField()

    class Meta:
        verbose_name = 'Компонент'
        verbose_name_plural = 'Компоненты'

    def __str__(self):
        return f'{self.ingredient} ({self.salad})'


class Order(models.Model):
    """
    Заказ
    """
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    salad = models.ForeignKey('Salad', on_delete=models.CASCADE)
    status = models.CharField(max_length=255)
    total_price = models.DecimalField(max_digits=8, decimal_places=2)

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
    courier = models.ForeignKey('User', on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    delivery_fee = models.DecimalField(max_digits=8)

    class Meta:
        verbose_name = 'Доставка'
        verbose_name_plural = 'Доставки'

    def __str__(self):
        return f'Доставка #{self.id}'
