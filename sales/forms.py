from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django import forms
from django.contrib.auth import get_user_model

from fmsapp.models import Sales


class LoginForm (AuthenticationForm):
    username = forms.CharField(max_length=10,widget=forms.TextInput(attrs={'class':'form-control p-4 mb-3', 'placeholder':'Username '}))
    password = forms.CharField(max_length=20, widget=forms.PasswordInput(attrs={'class':'form-control p-4 mb-3', 'placeholder':'Password '}))

    class Meta:
        model = get_user_model()
        fields = '__all__'


class SalesForm(forms.ModelForm):
    class Meta:
        model = Sales
        fields =['name','category','weight','price','description','image']
        widgets = {
            'category':forms.TextInput(attrs={'class':'form-control','placeholder':'fish from tana'}),
            'category':forms.TextInput(attrs={'class':'form-control','placeholder':'e.g Tilapia'}),
            'quantity':forms.NumberInput(attrs={'class':'form-control','placeholder':'Total Number of Fish','id':'qty'}),
            'price':forms.NumberInput(attrs={'class':'form-control','placeholder':'Total Amount to be paid'}),
            'descriptin':forms.Textarea(attrs={'class': 'form-control' , 'placeholder':'Detail about the fish product'}),
            'image': forms.FileInput(attrs={'class':'form-control'})
        }