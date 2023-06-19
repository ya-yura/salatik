from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.generic.edit import FormView
from core.models import Ingredient
from .forms import IngredientForm


@login_required
def ingredient_list(request):
    role = request.user.role.values_list('slug', flat=True)  # Получаем объект роли пользователя

    if 'store' in role:
        ingredients = Ingredient.objects.all().order_by('type')
        ingredient_types = set(ingredient.type for ingredient in ingredients)
        form = None

        if request.method == 'POST':
            form = IngredientForm(request.POST)
            if form.is_valid():
                try:
                    ingredient = form.save(commit=False)
                    # Дополнительная обработка данных, если необходимо
                    ingredient.save()
                    form = IngredientForm()
                except Exception as e:
                    print(f"Ошибка сохранения данных: {e}")
        else:
            form = IngredientForm()

        return render(
            request,
            'kitchen/ingredient_list.html',
            {'ingredients': ingredients, 'ingredient_types': ingredient_types, 'form': form}
        )
    else:
        return render(
            request,
            'kitchen/access_denied.html',
            {'user': request.user, 'role': role}
        )
