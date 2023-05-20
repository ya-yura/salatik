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

    seasonings = [
       {
           'name': 'Соль',
           'protein': 0,
           'fat': 0,
           'carbohydrates': 0,
           'energy': 0,
           'is_available': True,
       },
       {
           'name': 'Перец черный',
           'protein': 10,
           'fat': 3,
           'carbohydrates': 64,
           'energy': 296,
           'is_available': True,
       },
       {
           'name': 'Перец красный',
           'protein': 12,
           'fat': 3,
           'carbohydrates': 63,
           'energy': 289,
           'is_available': True,
       },
       {
           'name': 'Орегано',
           'protein': 9,
           'fat': 4,
           'carbohydrates': 69,
           'energy': 306,
           'is_available': True,
       },
       {
           'name': 'Базилик',
           'protein': 3,
           'fat': 1,
           'carbohydrates': 23,
           'energy': 22,
           'is_available': True,
       },
       {
           'name': 'Кориандр',
           'protein': 21,
           'fat': 4,
           'carbohydrates': 35,
           'energy': 279,
           'is_available': True,
       },
    ]

    for seasoning_data in seasonings:
        if not Ingredient.objects.filter(name=seasoning_data['name']):
            seasoning_data['type'] = seasoning_type
            seasoning_data['price_per_unit'] = random.randint(30, 180)
            ingredient = Ingredient.objects.create(**seasoning_data)

    seafoods = [
        {
            'name': 'Мидии',
            'protein': 24,
            'fat': 2,
            'carbohydrates': 4,
            'energy': 126,
            'is_available': True,
        },
        {
            'name': 'Крабовое мясо',
            'protein': 18,
            'fat': 1,
            'carbohydrates': 0,
            'energy': 84,
            'is_available': True,
        },
        {
            'name': 'Кальмары',
            'protein': 18,
            'fat': 0.6,
            'carbohydrates': 2,
            'energy': 92,
            'is_available': True,
        },
        {
            'name': 'Морской окунь',
            'protein': 18,
            'fat': 2,
            'carbohydrates': 0,
            'energy': 97,
            'is_available': True,
        },
        {
            'name': 'Лосось',
            'protein': 20,
            'fat': 13,
            'carbohydrates': 0,
            'energy': 208,
            'is_available': True,
        },
    ]

    for seafood_data in seafoods:
        if not Ingredient.objects.filter(name=seafood_data['name']):
            seafood_data['type'] = seafood_type
            seafood_data['price_per_unit'] = random.randint(30, 180)
            ingredient = Ingredient.objects.create(**seafood_data)

    nuts_seeds = [
        {
            'name': 'Арахис',
            'protein': 26,
            'fat': 49,
            'carbohydrates': 16,
            'energy': 567,
            'is_available': True,
        },
        {
            'name': 'Тыквенные семечки',
            'protein': 24,
            'fat': 45,
            'carbohydrates': 18,
            'energy': 559,
            'is_available': True,
        },
        {
            'name': 'Кешью',
            'protein': 18,
            'fat': 44,
            'carbohydrates': 30,
            'energy': 553,
            'is_available': True,
        },
        {
            'name': 'Миндаль',
            'protein': 21,
            'fat': 49,
            'carbohydrates': 22,
            'energy': 575,
            'is_available': True,
        },
        {
            'name': 'Семена чиа',
            'protein': 17,
            'fat': 31,
            'carbohydrates': 42,
            'energy': 486,
            'is_available': True,
        },
    ]

    for nuts_seeds_data in nuts_seeds:
        if not Ingredient.objects.filter(name=nuts_seeds_data['name']):
            nuts_seeds_data['type'] = nuts_seeds_type
            nuts_seeds_data['price_per_unit'] = random.randint(30, 180)
            ingredient = Ingredient.objects.create(**nuts_seeds_data)

    dried_fruits = [
        {
            'name': 'Клюква',
            'protein': 0.4,
            'fat': 0.1,
            'carbohydrates': 9.6,
            'energy': 43,
            'is_available': True,
        },
        {
            'name': 'Изюм',
            'protein': 2.5,
            'fat': 0.4,
            'carbohydrates': 79,
            'energy': 299,
            'is_available': True,
        },
        {
            'name': 'Вишня',
            'protein': 1,
            'fat': 0.3,
            'carbohydrates': 12,
            'energy': 50,
            'is_available': True,
        },
        {
            'name': 'Чернослив',
            'protein': 2.3,
            'fat': 0.4,
            'carbohydrates': 38,
            'energy': 155,
            'is_available': True,
        },
        {
            'name': 'Абрикосы',
            'protein': 0.5,
            'fat': 0.1,
            'carbohydrates': 3.9,
            'energy': 15,
            'is_available': True,
        },
    ]

    for dried_fruits_data in dried_fruits:
        if not Ingredient.objects.filter(name=dried_fruits_data['name']):
            dried_fruits_data['type'] = dried_fruits_type
            dried_fruits_data['price_per_unit'] = random.randint(30, 180)
            ingredient = Ingredient.objects.create(**dried_fruits_data)

    cheeses = [
        {
            'name': 'Моцарелла',
            'protein': 22,
            'fat': 17,
            'carbohydrates': 2.2,
            'energy': 254,
            'is_available': True,
        },
        {
            'name': 'Гауда',
            'protein': 25,
            'fat': 31,
            'carbohydrates': 0.6,
            'energy': 356,
            'is_available': True,
        },
        {
            'name': 'Рокфор',
            'protein': 21,
            'fat': 32,
            'carbohydrates': 2,
            'energy': 369,
            'is_available': True,
        },
        {
            'name': 'Чеддер',
            'protein': 25,
            'fat': 33,
            'carbohydrates': 1.3,
            'energy': 404,
            'is_available': True,
        },
        {
            'name': 'Брынза',
            'protein': 14,
            'fat': 17,
            'carbohydrates': 0.5,
            'energy': 216,
            'is_available': True,
        },
    ]

    for cheese_data in cheeses:
        if not Ingredient.objects.filter(name=cheese_data['name']):
            cheese_data['type'] = cheese_type
            cheese_data['price_per_unit'] = random.randint(30, 180)
            ingredient = Ingredient.objects.create(**cheese_data)

    pickled_vegetables = [
        {
            'name': 'Маринованный огурец',
            'protein': 0,
            'fat': 0,
            'carbohydrates': 1,
            'energy': 4,
            'is_available': True,
        },
        {
            'name': 'Каперсы',
            'protein': 2,
            'fat': 0,
            'carbohydrates': 2,
            'energy': 11,
            'is_available': True,
        },
        {
            'name': 'Маслины',
            'protein': 0.8,
            'fat': 15,
            'carbohydrates': 3.8,
            'energy': 145,
            'is_available': True,
        },
        {
            'name': 'Перец чили',
            'protein': 1.9,
            'fat': 0.2,
            'carbohydrates': 9.5,
            'energy': 40,
            'is_available': True,
        },
        {
            'name': 'Лук красный маринованный',
            'protein': 0.5,
            'fat': 0,
            'carbohydrates': 2.9,
            'energy': 15,
            'is_available': True,
        },
    ]

    for vegetable_data in pickled_vegetables:
        if not Ingredient.objects.filter(name=vegetable_data['name']):
            vegetable_data['type'] = pickled_vegetables_type
            vegetable_data['price_per_unit'] = random.randint(30, 180)
            ingredient = Ingredient.objects.create(**vegetable_data)

    grains_legumes = [
        {
            'name': 'Чечевица',
            'protein': 24,
            'fat': 1,
            'carbohydrates': 60,
            'energy': 336,
            'is_available': True,
        },
        {
            'name': 'Фасоль',
            'protein': 22,
            'fat': 1,
            'carbohydrates': 60,
            'energy': 341,
            'is_available': True,
        },
        {
            'name': 'Горох',
            'protein': 22,
            'fat': 1,
            'carbohydrates': 60,
            'energy': 316,
            'is_available': True,
        },
        {
            'name': 'Киноа',
            'protein': 14,
            'fat': 6,
            'carbohydrates': 64,
            'energy': 368,
            'is_available': True,
        },
        {
            'name': 'Рисовые лапши',
            'protein': 8,
            'fat': 2,
            'carbohydrates': 77,
            'energy': 361,
            'is_available': True,
        },
    ]

    for grain_legume_data in grains_legumes:
        if not Ingredient.objects.filter(name=grain_legume_data['name']):
            grain_legume_data['type'] = grains_legumes_type
            grain_legume_data['price_per_unit'] = random.randint(30, 180)
            ingredient = Ingredient.objects.create(**grain_legume_data)

    texture_additives = [
        {
            'name': 'Хрустящие крошки хлеба',
            'protein': 8,
            'fat': 5,
            'carbohydrates': 40,
            'energy': 220,
            'is_available': True,
        },
        {
            'name': 'Кунжут',
            'protein': 17.7,
            'fat': 49.7,
            'carbohydrates': 23.4,
            'energy': 567,
            'is_available': True,
        },
        {
            'name': 'Криспы (рисовые)',
            'protein': 7,
            'fat': 1,
            'carbohydrates': 87,
            'energy': 391,
            'is_available': True,
        },
        {
            'name': 'Криспы (кукурузные)',
            'protein': 7,
            'fat': 1,
            'carbohydrates': 84,
            'energy': 380,
            'is_available': True,
        },
        {
            'name': 'Картофельные чипсы',
            'protein': 6,
            'fat': 35,
            'carbohydrates': 53,
            'energy': 536,
            'is_available': True,
        },
        {
            'name': 'Гранола',
            'protein': 11,
            'fat': 7,
            'carbohydrates': 61,
            'energy': 379,
            'is_available': True,
        },
    ]

    for additive_data in texture_additives:
        if not Ingredient.objects.filter(name=additive_data['name']):
            additive_data['type'] = texture_additives_type
            additive_data['price_per_unit'] = random.randint(50, 200)
            ingredient = Ingredient.objects.create(**additive_data)

    green_vegetables = [
        {
            'name': 'Сельдерей',
            'protein': 0.7,
            'fat': 0.2,
            'carbohydrates': 2.2,
            'energy': 9,
            'is_available': True,
        },
        {
            'name': 'Шпинат',
            'protein': 2.9,
            'fat': 0.4,
            'carbohydrates': 3.6,
            'energy': 23,
            'is_available': True,
        },
        {
            'name': 'Брокколи',
            'protein': 2.8,
            'fat': 0.4,
            'carbohydrates': 6.6,
            'energy': 34,
            'is_available': True,
        },
        {
            'name': 'Лук-порей',
            'protein': 1.5,
            'fat': 0.3,
            'carbohydrates': 12.4,
            'energy': 61,
            'is_available': True,
        },
        {
            'name': 'Зеленый горошек',
            'protein': 5.4,
            'fat': 0.2,
            'carbohydrates': 14.5,
            'energy': 81,
            'is_available': True,
        },
    ]

    for vegetable_data in green_vegetables:
        if not Ingredient.objects.filter(name=vegetable_data['name']):
            vegetable_data['type'] = green_vegetables_type
            vegetable_data['price_per_unit'] = random.randint(20, 50)
            ingredient = Ingredient.objects.create(**vegetable_data)

    spicy_additives = [
        {
            'name': 'Свежий перец чили',
            'protein': 1.9,
            'fat': 0.4,
            'carbohydrates': 8.8,
            'energy': 40,
            'is_available': True,
        },
        {
            'name': 'Соус табаско',
            'protein': 0.9,
            'fat': 0.4,
            'carbohydrates': 7.1,
            'energy': 35,
            'is_available': True,
        },
        {
            'name': 'Редкий перец',
            'protein': 0.9,
            'fat': 0.2,
            'carbohydrates': 3.7,
            'energy': 19,
            'is_available': True,
        },
        {
            'name': 'Халапеньо',
            'protein': 0.9,
            'fat': 0.2,
            'carbohydrates': 4.1,
            'energy': 20,
            'is_available': True,
        },
        {
            'name': 'Перец чили в масле',
            'protein': 1,
            'fat': 34,
            'carbohydrates': 1,
            'energy': 326,
            'is_available': True,
        },
    ]

    for additive_data in spicy_additives:
        if not Ingredient.objects.filter(name=additive_data['name']):
            additive_data['type'] = spicy_additives_type
            additive_data['price_per_unit'] = random.randint(20, 50)
            ingredient = Ingredient.objects.create(**additive_data) 

    other_vegetables = [
        {
            'name': 'Артишоки',
            'protein': 2.2,
            'fat': 0.2,
            'carbohydrates': 10.5,
            'energy': 53,
            'is_available': True,
        },
        {
            'name': 'Черри-помидоры',
            'protein': 0.9,
            'fat': 0.2,
            'carbohydrates': 3.9,
            'energy': 18,
            'is_available': True,
        },
        {
            'name': 'Лук-шалот',
            'protein': 2.5,
            'fat': 0.1,
            'carbohydrates': 12.2,
            'energy': 60,
            'is_available': True,
        },
        {
            'name': 'Редька',
            'protein': 0.7,
            'fat': 0.1,
            'carbohydrates': 3.4,
            'energy': 16,
            'is_available': True,
        },
        {
            'name': 'Морковь разных цветов (фиолетовая, желтая)',
            'protein': 0.9,
            'fat': 0.2,
            'carbohydrates': 6.9,
            'energy': 32,
            'is_available': True,
        },
    ]

    for vegetable_data in other_vegetables:
        if not Ingredient.objects.filter(name=vegetable_data['name']):
            vegetable_data['type'] = other_vegetables_type
            vegetable_data['price_per_unit'] = random.randint(5, 15)
            ingredient = Ingredient.objects.create(**vegetable_data)


class Command(BaseCommand):
    def handle(self, *args, **options):
        run()
