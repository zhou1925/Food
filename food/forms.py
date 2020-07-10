from django import forms
from .models import Restaurant, Meal
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    email = forms.CharField(max_length=100, required=True)
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username', 'password', 'first_name', 'last_name', 'email')

class UserEditForm(forms.ModelForm):
    email = forms.CharField(max_length=100, required=True)
    
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')


class RestaurantForm(forms.ModelForm):
    class Meta:
        model = Restaurant
        fields = ('name', 'phone', 'address', 'logo')


class AddMealForm(forms.ModelForm):
    class Meta:
        model = Meal
        exclude = ('restaurant',)

class EditMealForm(forms.ModelForm):
    class Meta:
        model = Meal
        exclude = ('restaurant',)