from django.shortcuts import render
from .models import Ingredient, IngredientType


def ingredient_list(request):
    # Получаем все типы ингредиентов
    ingredient_types = IngredientType.objects.all()

    # Создаем пустой словарь, где ключами будут типы ингредиентов,
    # а значениями - списки ингредиентов
    ingredient_dict = {}

    # Для каждого типа ингредиентов
    for ingredient_type in ingredient_types:
        # Получаем все ингредиенты этого типа
        ingredients = Ingredient.objects.filter(type=ingredient_type)

        # Добавляем ингредиенты в словарь, используя тип ингредиента
        # в качестве ключа
        ingredient_dict[ingredient_type] = ingredients

    # Передаем словарь с ингредиентами в шаблон для отображения
    return render(request, 'index.html', {'ingredient_dict': ingredient_dict})
