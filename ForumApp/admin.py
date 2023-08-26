from django.contrib import admin
from django import forms
from .models import ForumUser

# Register your models here.

class ForumUserChangePassword(forms.ModelForm):
    class Meta:
        widgets = {
            "user_password": forms.PasswordInput(attrs={'placeholder': '*************'})
        }
        help_texts = {
            "user_password": "If you leave this field empty, it will delete the password completely! <br> I will fix that later."
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.initial['user_password'] = ''
        self.fields['user_password'].required = True

class ForumUserAdmin(admin.ModelAdmin):

    list_display = ["user_name", "user_email", "show_password"]

    form = ForumUserChangePassword

    #fields = ["user_name", "user_email", "user_password"]

admin.site.register(ForumUser, ForumUserAdmin)