from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Userdata

class registration_form(UserCreationForm):
    
    class Meta:
        model = Userdata
        
        fields =['username','first_name','last_name','email','phone_no','password1','password2']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last name'}),
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'phone_no': forms.TextInput(attrs={'class': 'form-control'}),
        }

class loginform(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(max_length=50)
    
    widgets ={
        'username':forms.TextInput(attrs={'class': 'form-control','placeholder': 'Username'}),
        'password' :forms.TextInput(attrs ={'class': 'form-control','placeholder': 'Password'})
    }