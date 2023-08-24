from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.hashers import UnsaltedMD5PasswordHasher
from django.forms.models import model_to_dict
from django.db.models import Q

from .models import ForumUser
from .forms import LoginForm, RegisterForm, EditProfileModelForm

# Create your views here.

def logged_in(request) -> bool:
    if request.session.get('is_logged_in') and request.session.get('user_id'):
        return True
    return False

def register(request):
    if logged_in(request):
        return redirect('profile_page', request.session.get('user_id'))

    if request.method == "POST":
        error = False

        form = RegisterForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['user_name']
            email = form.cleaned_data['user_email']
            password1 = form.cleaned_data['user_password1']
            password2 = form.cleaned_data['user_password2']

            if password1 != password2:
                form.add_error(None, "Passwords don't match.")
                error = True

            if ForumUser.objects.filter(user_name__iexact=username).exists():
                form.add_error(None, "User already exists.")
                error = True

            if not error:
                ForumUser.objects.create(user_name=username, user_email=email, user_password=password2)
                return redirect('login_page_str', login_message="Registration Successful.")

    else:
        form = RegisterForm()

    return render(request, "ForumApp/register.html", {
        "form": form,
        "errors": form.non_field_errors()
    })

def login(request, login_message=False):
    if logged_in(request):
        return redirect('profile_page', request.session.get('user_id'))

    if request.method == "POST":
        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['user_name']
            password = UnsaltedMD5PasswordHasher.encode(None, form.cleaned_data['user_password'], "")

            user =  ForumUser.objects.filter(user_name=username, user_password=password).first()

            if user:
                request.session['is_logged_in'] = True
                request.session['user_id'] = user.id
                return redirect('profile_page', request.session.get('user_id'))
            else:
                form.add_error(None, "Incorrect credentials.")
    else:
        form = LoginForm()

    return render(request, "ForumApp/login.html", {
        "form": form,
        "errors": form.non_field_errors(),
        "login_message": login_message
    })

def logout(request):
    try:
        del request.session['is_logged_in']
    except:
        pass

    return redirect('login_page')

def profile(request, id):
    if not request.session.get('is_logged_in'):
        return redirect('login_page')

    user_info = ForumUser.objects.get(pk=id)

    return render(request, "ForumApp/profile.html", {
        "user_id": str(request.session.get('user_id')),
        "page_id": str(id),
        "user_info": user_info
    })

def edit_profile(request):
    if not logged_in(request):
        return redirect('login_page')

    if request.method == "POST":
        error = False

        user = ForumUser.objects.get(pk=request.POST['user_id'])
        form = EditProfileModelForm(request.POST or None, request.FILES or None, instance=user)

        if form.is_valid():
            dict = {key:value for key,value in form.cleaned_data.items() if value != '' and value != None} # get all

            if ForumUser.objects.filter(~Q(pk=request.session.get('user_id')), user_name__iexact=form.cleaned_data['user_name']).exists():
                form.add_error(None, "Username already in use.")
                error = True

            if not error:
                print(dict.keys())
                user.save(update_fields=dict.keys())
                return redirect('profile_page', id=request.session.get('user_id'))

    else:
        form_values = ForumUser.objects.get(pk=request.session.get('user_id'))
        values = model_to_dict(form_values)
        values['user_password'] = ''
        form = EditProfileModelForm(values)

    return render(request, "ForumApp/edit-profile.html", {
        "user_image": ForumUser.objects.get(pk=request.session.get('user_id')).user_image.url,
        "user_id": request.session.get('user_id'),
        "form": form,
        "errors": form.non_field_errors()
    })