from django import forms
from .models import ForumUser
from django.core.validators import MinLengthValidator


class LoginForm(forms.Form):
    user_name = forms.CharField(max_length=50, widget=forms.TextInput(
        attrs={'placeholder': 'Username'}))
    user_password = forms.CharField(
        max_length=20, widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))


class RegisterForm(forms.Form):
    user_name = forms.CharField(max_length=50, widget=forms.TextInput(
        attrs={'placeholder': 'Username'}), validators=[MinLengthValidator(5)])
    user_email = forms.EmailField(widget=forms.TextInput(
        attrs={'placeholder': 'Email'}))
    user_password1 = forms.CharField(max_length=20, widget=forms.PasswordInput(
        attrs={'placeholder': 'Password'}), validators=[MinLengthValidator(5)])
    user_password2 = forms.CharField(max_length=20, widget=forms.PasswordInput(
        attrs={'placeholder': 'Repeat Password'}), validators=[MinLengthValidator(5)])


class EditProfileModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['user_password'].required = False
    
    user_image = forms.ImageField(widget=forms.FileInput, required=False)

    class Meta:
        model = ForumUser
        exclude = ['']
        widgets = {
            "user_name": forms.TextInput(attrs={'placeholder': 'Change Username'}),
            "user_email": forms.TextInput(attrs={'placeholder': 'Change Email'}),
            "user_password": forms.PasswordInput(attrs={'placeholder': 'Change Password'})
        }