from django.db import models
from django.contrib import admin
from django.core.validators import MinLengthValidator

from django.contrib.auth.hashers import UnsaltedMD5PasswordHasher

# Create your models here.
class ForumUser(models.Model):
    user_name = models.CharField(max_length=50, validators=[MinLengthValidator(5)])
    user_email = models.EmailField()
    user_password = models.CharField(max_length=32, blank=False, null=False, validators=[MinLengthValidator(5)])
    user_image = models.ImageField(null=True, blank=True, upload_to="images", default="images/avatar.jpg")
    user_details = models.TextField(max_length=300, blank=True)

    @admin.display(description="Password")
    def show_password(self):
        return self.user_password[:5] + "************"

    def __str__(self):
        return f"[{self.pk}] {self.user_name}"

    def save(self, *args, **kwargs):
        self.user_password = UnsaltedMD5PasswordHasher.encode(None, self.user_password, "")
        super().save(*args, **kwargs)