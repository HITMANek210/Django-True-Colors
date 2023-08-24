from django import forms

class BackupServerForm(forms.Form):
    backup_name = forms.CharField()