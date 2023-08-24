from django.urls import path
from . import views

urlpatterns = [
    path("", views.login, name="login_page"),
    path("?login_message=<str:login_message>", views.login, name="login_page_str"),
    path("register/", views.register, name="register_page"),
    path("logout/", views.logout, name="logout_page"),
    path("profile/<int:id>", views.profile, name="profile_page"),
    path("edit-profile/", views.edit_profile, name="edit_profile_page"),
]