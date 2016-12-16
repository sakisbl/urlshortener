from django import forms


class URLSubmitForm(forms.Form):
    url = forms.URLField()
    
