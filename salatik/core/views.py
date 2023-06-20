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






"""

from elasticsearch_dsl import Search
from .search_indexes import SaladDocument
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Salad
from elasticsearch import Elasticsearch


def search_salads(query):
    s = Search(index='salads').query(
        'multi_match', query=query,
        fields=['name', 'description']
        )
    response = s.execute()
    salads = []
    for hit in response:
        salad = SaladDocument.get(id=hit.meta.id)
        salads.append(salad)
    return salads


@receiver(post_save, sender=Salad)
def update_salad_index(sender, instance, created, **kwargs):
    salad_document = SaladDocument.get(id=instance.id)
    salad_document.save()


def search_results(request):
    query = request.GET.get('query')
    if query:
        # Создайте подключение к Elasticsearch
        es = Elasticsearch()

        # Настройте параметры поиска
        search_params = {
            'query': {
                'match': {
                    'field_name': query
                }
            }
        }

        # Выполните поиск в Elasticsearch на основе параметров
        results = es.search(index='your_index', body=search_params)

        # Извлеките необходимую информацию из результатов поиска
        hits = results['hits']['hits']
        search_results = [hit['_source'] for hit in hits]

        # Передайте результаты в контекст шаблона
        context = {'results': search_results}
        return render(request, 'search_results.html', context)
    else:
        return render(request, 'search_results.html')
"""
