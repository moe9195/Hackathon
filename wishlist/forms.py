from django import forms
from django.contrib.auth.models import User
from .models import Item, Wishlist

class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email' ,'password']

        widgets={
        'password': forms.PasswordInput(),
        }

class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, widget=forms.PasswordInput())

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'image', 'url']

class WishlistForm(forms.ModelForm):
    class Meta:
        model = Wishlist
        fields = ['title']

class BoughtForm(forms.Form):
    bought = forms.BooleanField(label="Check this")
