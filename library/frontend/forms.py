from django import forms


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()


class ItemDownloadForm(forms.Form):
    item_id = forms.CharField()