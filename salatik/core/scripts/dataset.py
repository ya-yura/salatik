from core.models import IngredientType, Ingredient
from django.core.management.base import BaseCommand
import random
# python manage.py runscript dataset


def get_or_create_ingredient_type(name):
    try:
        ingredient_type = IngredientType.objects.get(name=name)
    except IngredientType.DoesNotExist:
        ingredient_type = IngredientType.objects.create(name=name)
    return ingredient_type


def run():
    additional_type = get_or_create_ingredient_type('Дополнительные ингредиенты')
    garnish_type = get_or_create_ingredient_type('Гарнир')
    protein_type = get_or_create_ingredient_type('Белок')
    fruit_type = get_or_create_ingredient_type('Фрукты')
    vegetable_type = get_or_create_ingredient_type('Овощи')
    sauce_type = get_or_create_ingredient_type('Соусы и заправки')
    seasoning_type = get_or_create_ingredient_type('Приправы и специи')
    seafood_type = get_or_create_ingredient_type('Морепродукты')
    nuts_seeds_type = get_or_create_ingredient_type('Семена и орехи')
    dried_fruits_type = get_or_create_ingredient_type('Сухие фрукты')
    cheese_type = get_or_create_ingredient_type('Сыры')
    pickled_vegetables_type = get_or_create_ingredient_type('Маринованные овощи')
    grains_legumes_type = get_or_create_ingredient_type('Зерновые и бобовые')
    texture_additives_type = get_or_create_ingredient_type('Добавки для текстуры')
    green_vegetables_type = get_or_create_ingredient_type('Зеленые овощи')
    spicy_additives_type = get_or_create_ingredient_type('Добавки для остроты')
    other_vegetables_type = get_or_create_ingredient_type('Другие овощи')

    additional_ingredients = [
        {
            'name': 'Грецкие орехи',
            'protein': 15,
            'fat': 65,
            'carbohydrates': 14,
            'energy': 654,
            'is_available': True,
        },
        {
            'name': 'Кедровые орехи',
            'protein': 13,
            'fat': 68,
            'carbohydrates': 14,
            'energy': 673,
            'is_available': True,
        },
        {
            'name': 'Семена льна',
            'protein': 18,
            'fat': 42,
            'carbohydrates': 28,
            'energy': 534,
            'is_available': True,
        },
        {
            'name': 'Семена подсолнечника',
            'protein': 20,
            'fat': 52,
            'carbohydrates': 20,
            'energy': 584,
            'is_available': True,
        },
        {
            'name': 'Семена горчицы',
            'protein': 26,
            'fat': 36,
            'carbohydrates': 29,
            'energy': 508,
            'is_available': True,
        },
        {
            'name': 'Пармезан',
            'protein': 33,
            'fat': 29,
            'carbohydrates': 4,
            'energy': 431,
            'is_available': True,
        },
        {
            'name': 'Чеддер',
            'protein': 25,
            'fat': 33,
            'carbohydrates': 1,
            'energy': 403,
            'is_available': True,
        },
        {
            'name': 'Голубой сыр',
            'protein': 21,
            'fat': 28,
            'carbohydrates': 2,
            'energy': 353,
            'is_available': True,
        },
        {
            'name': 'Изюм',
            'protein': 3,
            'fat': 0.5,
            'carbohydrates': 74,
            'energy': 299,
            'is_available': True,
        },
        {
            'name': 'Курага',
            'protein': 5,
            'fat': 0.5,
            'carbohydrates': 50,
            'energy': 213,
            'is_available': True,
        },
        {
            'name': 'Чернослив',
            'protein': 2,
            'fat': 0.5,
            'carbohydrates': 64,
            'energy': 240,
            'is_available': True,
        },
    ]

    for additional_data in additional_ingredients:
        if not Ingredient.objects.filter(
                name=additional_data['name']
        ):
            additional_data['type'] = additional_type
            additional_data['price_per_unit'] = random.randint(30, 180)
            ingredient = Ingredient.objects.create(**additional_data)


# Создание записей для соусов и заправок
    sauces = [
       {
           'name': 'Оливковое масло',
           'protein': 0,
           'fat': 100,
           'carbohydrates': 0,
           'energy': 900,
           'is_available': True,
       },
       {
           'name': 'Бальзамический уксус',
           'protein': 0,
           'fat': 0,
           'carbohydrates': 17,
           'energy': 70,
           'is_available': True,
       },
       {
           'name': 'Лимонный сок',
           'protein': 1,
           'fat': 0,
           'carbohydrates': 3,
           'energy': 15,
           'is_available': True,
       },
       {
           'name': 'Горчица',
           'protein': 5,
           'fat': 9,
           'carbohydrates': 6,
           'energy': 136,
           'is_available': True,
       },
       {
           'name': 'Мед',
           'protein': 0,
           'fat': 0,
           'carbohydrates': 82,
           'energy': 304,
           'is_available': True,
       },
    ]

    for sauce_data in sauces:
        if not Ingredient.objects.filter(
                name=sauce_data['name']
        ):
            sauce_data['type'] = sauce_type
            sauce_data['price_per_unit'] = random.randint(30, 180)
            ingredient = Ingredient.objects.create(**sauce_data)


# Создание записей ингредиентов - гарнир
    garnishes = [
       {
           'name': 'Киноа',
           'protein': 4,
           'fat': 2,
           'carbohydrates': 21,
           'energy': 120,
           'is_available': True,
       },
       {
           'name': 'Гречка',
           'protein': 13,
           'fat': 3,
           'carbohydrates': 72,
           'energy': 343,
           'is_available': True,
       },
       {
           'name': 'Чечевица',
           'protein': 24,
           'fat': 1,
           'carbohydrates': 60,
           'energy': 336,
           'is_available': True,
       },
       {
           'name': 'Картофель жареный',
           'protein': 3,
           'fat': 16,
           'carbohydrates': 41,
           'energy': 319,
           'is_available': True,
       },
       {
           'name': 'Картофель отварной',
           'protein': 2,
           'fat': 0,
           'carbohydrates': 17,
           'energy': 77,
           'is_available': True,
       },
       {
           'name': 'Рис белый',
           'protein': 2,
           'fat': 0,
           'carbohydrates': 29,
           'energy': 130,
           'is_available': True,
       },
       {
           'name': 'Рис коричневый',
           'protein': 2,
           'fat': 1,
           'carbohydrates': 23,
           'energy': 111,
           'is_available': True,
       },
    ]

    for garnish_data in garnishes:
        if not Ingredient.objects.filter(
                name=garnish_data['name']
        ):
            garnish_data['type'] = garnish_type
            garnish_data['price_per_unit'] = random.randint(30, 180)
            ingredient = Ingredient.objects.create(**garnish_data)


# Создание записей ингредиентов - белок
    proteins = [
        {
            'name': 'Куриное филе жареное',
            'protein': 31,
            'fat': 3,
            'carbohydrates': 0,
            'energy': 165,
            'is_available': True,
        },
        {
            'name': 'Куриное филе запеченное',
            'protein': 31,
            'fat': 3,
            'carbohydrates': 0,
            'energy': 165,
            'is_available': True,
        },
        {
            'name': 'Креветки',
            'protein': 24,
            'fat': 1,
            'carbohydrates': 0,
            'energy': 99,
            'is_available': True,
        },
        {
            'name': 'Тунец свежий',
            'protein': 30,
            'fat': 3,
            'carbohydrates': 0,
            'energy': 144,
            'is_available': True,
        },
        {
            'name': 'Тунец консервированный',
            'protein': 26,
            'fat': 8,
            'carbohydrates': 0,
            'energy': 184,
            'is_available': True,
        },
        {
            'name': 'Фета',
            'protein': 14,
            'fat': 21,
            'carbohydrates': 4,
            'energy': 264,
            'is_available': True,
        },
        {
            'name': 'Тофу',
            'protein': 15,
            'fat': 8,
            'carbohydrates': 3,
            'energy': 144,
            'is_available': True,
        },
    ]

    for protein_data in proteins:
        if not Ingredient.objects.filter(
                name=protein_data['name']
        ):
            protein_data['type'] = protein_type
            protein_data['price_per_unit'] = random.randint(30, 180)
            ingredient = Ingredient.objects.create(**protein_data)


# Создание записей ингредиентов - фрукты
    fruits = [
        {
            'name': 'Клубника',
            'protein': 0.7,
            'fat': 0.3,
            'carbohydrates': 7.7,
            'energy': 32,
            'is_available': True,
        },
        {
            'name': 'Малина',
            'protein': 1.2,
            'fat': 0.7,
            'carbohydrates': 11.9,
            'energy': 53,
            'is_available': True,
        },
        {
            'name': 'Черника',
            'protein': 0.7,
            'fat': 0.4,
            'carbohydrates': 12.6,
            'energy': 57,
            'is_available': True,
        },
        {
            'name': 'Груши',
            'protein': 0.4,
            'fat': 0.1,
            'carbohydrates': 15,
            'energy': 57,
            'is_available': True,
        },
        {
            'name': 'Яблоки',
            'protein': 0.3,
            'fat': 0.4,
            'carbohydrates': 14,
            'energy': 52,
            'is_available': True,
        },
        {
            'name': 'Апельсины',
            'protein': 0.9,
            'fat': 0.2,
            'carbohydrates': 9,
            'energy': 43,
            'is_available': True,
        },
        {
            'name': 'Авокадо',
            'protein': 2,
            'fat': 14.7,
            'carbohydrates': 8.5,
            'energy': 160,
            'is_available': True,
        },
    ]

    for fruit_data in fruits:
        if not Ingredient.objects.filter(
                name=fruit_data['name']
        ):
            fruit_data['type'] = fruit_type
            fruit_data['price_per_unit'] = random.randint(30, 180)
            ingredient = Ingredient.objects.create(**fruit_data)


# Создание записей ингредиентов - овощи
    vegetables = [
       {
           'name': 'Томаты (вишневые, черри, грушевидные и т.д.)',
           'protein': 0.9,
           'fat': 0.2,
           'carbohydrates': 3.9,
           'energy': 18,
           'is_available': True,
       },
       {
           'name': 'Огурцы',
           'protein': 0.7,
           'fat': 0.1,
           'carbohydrates': 2.8,
           'energy': 15,
           'is_available': True,
       },
       {
           'name': 'Перец (сладкий, горький)',
           'protein': 0.9,
           'fat': 0.1,
           'carbohydrates': 3,
           'energy': 20,
           'is_available': True,
       },
       {
           'name': 'Морковь (сырая, запеченная)',
           'protein': 0.8,
           'fat': 0.1,
           'carbohydrates': 7.5,
           'energy': 35,
           'is_available': True,
       },
       {
           'name': 'Капуста (белокочанная, цветная)',
           'protein': 1.8,
           'fat': 0.1,
           'carbohydrates': 5.5,
           'energy': 25,
           'is_available': True,
       },
    ]

    for vegetable_data in vegetables:
        if not Ingredient.objects.filter(
                name=vegetable_data['name']
        ):
            vegetable_data['type'] = vegetable_type
            vegetable_data['price_per_unit'] = random.randint(30, 180)
            ingredient = Ingredient.objects.create(**vegetable_data)


class Command(BaseCommand):
    def handle(self, *args, **options):
        run()
