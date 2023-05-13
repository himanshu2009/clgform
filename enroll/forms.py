from django import forms




from django .contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField, PasswordChangeForm
from django import forms
from django.contrib.auth import password_validation
from django.contrib.auth.forms import PasswordResetForm












  










# user registration(all are djangos builtin user authentication forms )

class CustomerRegistrationForm(UserCreationForm):
   password1 = forms.CharField(label='Password', widget=forms.PasswordInput())
   password2 = forms.CharField(
       label='Confirm Password (again)', widget=forms.PasswordInput())
   email = forms.CharField(required=True, widget=forms.EmailInput())

   class Meta:
     model = User
     fields = ['username', 'email', 'password1', 'password2']
     labels = {'email': 'Email'}
     widgets = {'username': forms.TextInput()}

#  user login
class LoginForm(AuthenticationForm):
 username = UsernameField(widget=forms.TextInput(
     attrs={'autofocus': True, 'class': 'form-control'}))
 password = forms.CharField(label=("Password"), strip=False, widget=forms.PasswordInput(
     attrs={'autocomplete': 'current-password', 'class': 'form-control'}))

# password change
class MyPasswordChangeForm(PasswordChangeForm):

  old_password = forms.CharField(label=("Old Password"), strip=False, widget=forms.PasswordInput(
      attrs={'autocomplete': 'current-password', 'autofocus': True,  'class': 'form-control'}))
  new_password1 = forms.CharField(label=("New Password"), strip=False, widget=forms.PasswordInput(attrs={'autocomplete': 'new-password', 'class':'form-control'}), help_text=password_validation.password_validators_help_text_html())
  new_password2 = forms.CharField(label=("Confirm New Password"), strip=False, widget=forms.PasswordInput(attrs={'autocomplete': 'new-password','class':'form-control'}))

# password reset

class CustomPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(label=("Email"), max_length=254, widget=forms.EmailInput(attrs={'autocomplete': 'email', 'class': 'form-control', 'placeholder': 'Email Address'}))  


 
  

