from django.contrib.auth.models import AbstractUser
from django.db import models
from slugify import slugify


class User(AbstractUser):
    """
    Пользователь
    """
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255, null=True)
    last_name = models.CharField(max_length=255, null=True)
    bio = models.TextField(null=True)
    phone = models.CharField(max_length=32, null=True)

    class Meta:
        ordering = ['username']
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username


class Role(models.Model):
    """
    Роль
    """
    name = models.CharField(max_length=255)
    users = models.ManyToManyField(User, related_name='role')
    slug = models.SlugField(max_length=255, unique=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'Роль'
        verbose_name_plural = 'Роли'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    @classmethod
    def create(cls, **kwargs):
        kwargs['slug'] = slugify(kwargs['name'])
        return cls.objects.create(**kwargs)

    def __str__(self):
        return self.name


class CustomerAddress(models.Model):
    """
    Адрес
    """
    users = models.ForeignKey('User', on_delete=models.CASCADE)
    city = models.CharField(max_length=255, null=True)
    street = models.CharField(max_length=255, null=True)
    house = models.IntegerField(null=True)
    flat = models.IntegerField(null=True)

    class Meta:
        ordering = ['street']
        verbose_name = 'Адрес'
        verbose_name_plural = 'Адреса'

    def __str__(self):
        address_parts = []
        if self.city:
            address_parts.append(self.city)
        if self.street:
            address_parts.append(self.street)
        if self.house:
            address_parts.append(str(self.house))
        if self.flat:
            address_parts.append(str(self.flat))

        return ', '.join(address_parts)
