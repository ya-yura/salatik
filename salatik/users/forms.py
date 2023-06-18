from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import User, Role
from django.forms.models import inlineformset_factory
from .models import CustomerAddress


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()

    role = forms.ModelChoiceField(queryset=Role.objects.all())

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'role']


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'phone']


class UserAddressForm(forms.ModelForm):
    class Meta:
        model = CustomerAddress
        fields = ['city', 'street', 'house', 'flat']


UserAddressFormSet = inlineformset_factory(
    User, 
    CustomerAddress,
    form=UserAddressForm,
    extra=1,
    can_delete=True)
