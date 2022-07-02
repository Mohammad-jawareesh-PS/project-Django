from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
 
 
 
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(label="البريد الاكتروني")
    first_name = forms.CharField(max_length = 20 ,label="الاسم الاول")
    last_name = forms.CharField(max_length = 20, label="الاسم الاخير")
    username = forms.CharField(max_length = 20, label="اسم المستخدم")
    password1 = forms.CharField(max_length=250 ,label="كلمه المرور",widget=forms.PasswordInput)
    password2 = forms.CharField(max_length=250,label="تاكيد كلمه المرور",widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        