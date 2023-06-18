# Generated by Django 4.2.1 on 2023-06-18 12:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_user_city_user_flat_user_house_user_phone_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='city',
        ),
        migrations.RemoveField(
            model_name='user',
            name='flat',
        ),
        migrations.RemoveField(
            model_name='user',
            name='house',
        ),
        migrations.RemoveField(
            model_name='user',
            name='street',
        ),
        migrations.CreateModel(
            name='CustomerAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=255, null=True)),
                ('street', models.CharField(max_length=255, null=True)),
                ('house', models.IntegerField(null=True)),
                ('flat', models.IntegerField(null=True)),
                ('users', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]