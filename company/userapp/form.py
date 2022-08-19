from dataclasses import fields
from django import forms
from userapp.models import Company_User,Company_Product

class userForm(forms.ModelForm):
    class Meta:
        model=Company_User
        fields="__all__"
        widgets ={
            'id': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Your id'}),
			'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Enter Name'}),
            'email': forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Your Eamil'}),
			'password': forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Password'}),
        }
        
class logForm(forms.ModelForm):
    class Meta:
        model=Company_User
        fields=['name','password'] 

class productForm(forms.ModelForm):
    class Meta:
        model=Company_Product
        fields="__all__"
