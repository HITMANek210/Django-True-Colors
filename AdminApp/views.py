from django.shortcuts import render
from django.http import HttpResponseForbidden
import os

from .forms import BackupServerForm

# Create your views here.

def logged_in_as_admin(request) -> bool:
    if request.session.get('is_logged_in') and request.session.get('user_id') and str(request.session.get('user_id')) == "1":
        return True
    return False

def admin_panel(request):
    if not logged_in_as_admin(request):
        return HttpResponseForbidden("<h2>Access Denied</h2><br> Log in as admin to view this page.")
    
    message = False
    
    if request.method == "POST":
        form = BackupServerForm(request.POST)

        if form.is_valid():
            # os.system(f"echo Backup > /home/django/backups/{form.cleaned_data['backup_name']}.db")
            os.system(f"cp db.sqlite3 /home/django/backups/{form.cleaned_data['backup_name']}.db")
            message = "Backup created successfully!"
    else:
        form = BackupServerForm()

    return render(request, "AdminApp/admin.html", {
        "message": message,
        "form": form
    })