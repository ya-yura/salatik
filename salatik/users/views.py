from django.shortcuts import render, redirect
from .forms import UserRegistrationForm
from django.contrib.auth.decorators import login_required
from .forms import UserProfileForm, UserAddressFormSet
from django.contrib.auth import get_user_model

User = get_user_model()


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ingredient_list')
    else:
        form = UserRegistrationForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def edit_profile(request):
    user = request.user

    if request.method == 'POST':
        user_form = UserProfileForm(request.POST, instance=user)
        address_formset = UserAddressFormSet(request.POST, instance=user)

        if user_form.is_valid() and address_formset.is_valid():
            user_form.save()
            address_formset.save()
            return redirect('profile')

    else:
        user_form = UserProfileForm(instance=user)
        address_formset = UserAddressFormSet(instance=user)

    context = {
        'user_form': user_form,
        'address_formset': address_formset,
    }
    return render(request, 'users/edit_profile.html', context)


@login_required
def profile(request):
    user = request.user
    orders = user.order_set.all()  # Получение списка заказов пользователя
    salads = user.salad_set.all()  # Получение списка созданных салатов пользователя
    context = {
        'user': user,
        'orders': orders,
        'salads': salads
    }
    return render(request, 'users/profile.html', context)
