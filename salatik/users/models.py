from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext as _


class User(AbstractUser):
    """
    Пользователь
    """
    username = models.CharField(
        _('Due on'),
        max_length=255,
        unique=True,
        )

    email = models.EmailField(
        _('Due on'),
        max_length=255,
        unique=True,
        )

    password = models.CharField(
        _('Due on'),
        max_length=255,
        )

    first_name = models.CharField(
        _('Due on'),
        max_length=255,
        null=True,
        blank=True,
        )

    last_name = models.CharField(
        _('Due on'),
        max_length=255,
        null=True,
        blank=True,
        )

    bio = models.TextField(
        _('Due on'),
        null=True,
        blank=True,
        )

    phone = models.CharField(
        _('Due on'),
        max_length=32,
        null=True,
        blank=True,
        )

    active = models.BooleanField(
        _('Due on'),
        default=False,
        )

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
    name = models.CharField(
        _('Due on'),
        max_length=255,
        )

    users = models.ManyToManyField(
        User,
        related_name='role'
        )

    slug = models.SlugField(
        _('Due on'),
        max_length=255,
        unique=True,
        )

    class Meta:
        ordering = ['name']
        verbose_name = 'Роль'
        verbose_name_plural = 'Роли'

    def __str__(self):
        return self.name


class CustomerAddress(models.Model):
    """
    Адрес
    """
    user = models.ForeignKey(
        'User',
        on_delete=models.CASCADE
        )

    city = models.CharField(
        _('Due on'),
        max_length=255,
        null=True,
        )

    street = models.CharField(
        _('Due on'),
        max_length=255,
        null=True,
        )

    house = models.IntegerField(
        _('Due on'),
        null=True,
        )

    flat = models.IntegerField(
        _('Due on'),
        null=True,
        )

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
