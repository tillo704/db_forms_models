from django import forms
from .models import User


class SignUp(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())
    



class Register(forms.Form):
    
    first_name = forms.CharField()
    last_name = forms.CharField(required=False)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())
    Confirm_Password = forms.CharField(widget=forms.PasswordInput())
    birthday = forms.DateField(widget=forms.DateInput(attrs={"type":"date"}))



class UserForm(forms.ModelForm):
    class Meta :
        model = User
        fields = ('user_id','first_name','last_name','username','email','about','is_married','birthday')
  
