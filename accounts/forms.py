# When you create a form.py you want to import these three things to import
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
# its a django syntax meta provides extra info about this particular class we are createing.
    class Meta:
        # model equeals CustomUser from models.py
        model = CustomUser
        # below is a tupel vvvvv, make sure to add commas
        fields = ('username', 'email',)

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email',)
