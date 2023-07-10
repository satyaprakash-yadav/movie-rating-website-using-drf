from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput
from .models import Movie

class CreateUserForm(UserCreationForm):

    class Meta:

        model = User
        fields = ['username', 'password1', 'password2']


# - Login User

class LoginForm(AuthenticationForm):
    
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())


# - Create Record

class DateInput(forms.DateInput):
    input_type = 'date'


class CreateRecordForm(forms.ModelForm):

    class Meta:

        model = Movie
        fields = ['title', 'genre', 'release_date', 'director', 'image', 'language', 'status', 'views_count', 'rating','description']
        widgets = {
          'description': forms.Textarea(attrs={'rows':4, 'cols':15}),
          'release_date': DateInput()
        }



# - Update Record

class UpdateRecordForm(forms.ModelForm):

    class Meta:

        model = Movie
        fields = ['title', 'genre', 'release_date', 'director', 'image', 'language', 'status', 'views_count', 'rating','description']
        widgets = {
          'description': forms.Textarea(attrs={'rows':4, 'cols':15}),
          'release_date': DateInput()
        }
        
