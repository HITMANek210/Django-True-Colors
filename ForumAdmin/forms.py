from django import forms

class BackupServerForm(forms.Form):
    backup_name = forms.CharField(max_length=40)