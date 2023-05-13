# Generated by Django 3.2 on 2023-05-13 13:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='IngredientType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Тип ингредиента',
                'verbose_name_plural': 'Типы ингредиентов',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=255)),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=8)),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Заказы',
            },
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Роль',
                'verbose_name_plural': 'Роли',
            },
        ),
        migrations.CreateModel(
            name='Salad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
            ],
            options={
                'verbose_name': 'Салат',
                'verbose_name_plural': 'Салаты',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=255, unique=True)),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('password', models.CharField(max_length=255)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('bio', models.TextField()),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.role')),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
            },
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=8)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.order')),
            ],
            options={
                'verbose_name': 'Оплата',
                'verbose_name_plural': 'Оплаты',
            },
        ),
        migrations.AddField(
            model_name='order',
            name='salad',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.salad'),
        ),
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.user'),
        ),
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('photo', models.ImageField(upload_to='ingredient_photos')),
                ('price_per_unit', models.DecimalField(decimal_places=2, max_digits=8)),
                ('protein', models.FloatField()),
                ('fat', models.FloatField()),
                ('carbohydrates', models.FloatField()),
                ('energy', models.FloatField()),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.ingredienttype')),
            ],
            options={
                'verbose_name': 'Ингредиент',
                'verbose_name_plural': 'Ингредиенты',
            },
        ),
        migrations.CreateModel(
            name='Delivery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=255)),
                ('status', models.CharField(max_length=255)),
                ('delivery_fee', models.DecimalField(decimal_places=2, max_digits=8)),
                ('courier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.user')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.order')),
            ],
            options={
                'verbose_name': 'Доставка',
                'verbose_name_plural': 'Доставки',
            },
        ),
        migrations.CreateModel(
            name='Component',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weight', models.DecimalField(decimal_places=2, max_digits=8)),
                ('order', models.IntegerField()),
                ('ingredient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.ingredient')),
                ('salad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.salad')),
            ],
            options={
                'verbose_name': 'Компонент',
                'verbose_name_plural': 'Компоненты',
            },
        ),
    ]
