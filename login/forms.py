import re
from django import forms
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
 
class RegistrationForm(forms.Form):
 
    username = forms.RegexField(regex=r'^\w+$', widget=forms.TextInput(attrs=dict(required=True, max_length=30)),
                                label=_("Username"), error_messages={ 'invalid': _("This value must contain only letters, numbers and underscores.") })
    email = forms.EmailField(widget=forms.TextInput(attrs=dict(required=True, max_length=30)), label=_("Email address"))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs=dict(required=True, max_length=30, render_value=False)),
                                label=_("Password"))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs=dict(required=True, max_length=30, render_value=False)),
                                label=_("Password (again)"))
    phone_number = forms.CharField(max_length=20, label="Phone Number")

    MANUFACTURER = 'ma'
    RECYCLER = 're'
    AUDITOR = 'au'
    GOVERNMENT_AGENCY = 'ga'
    types = ((MANUFACTURER, 'Manufacturer'),
             (RECYCLER, 'Recycler'),
             (GOVERNMENT_AGENCY, 'Overseer'),
             (AUDITOR, 'Auditor')
             )
    type = forms.ChoiceField(choices=types,)
 
    def clean_username(self):
        try:
            user = User.objects.get(username__iexact=self.cleaned_data['username'])
        except User.DoesNotExist:
            return self.cleaned_data['username']
        raise forms.ValidationError(_("The username already exists. Please try another one."))

    def clean_email(self):
        if User.objects.filter(email__iexact=self.cleaned_data['email']).exists():
            raise forms.ValidationError(_("This email is already used. Please try another one."))
        else:
            return self.cleaned_data['email']

    def clean(self):
        if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:
            if self.cleaned_data['password1'] != self.cleaned_data['password2']:
                raise forms.ValidationError(_("The two password fields did not match."))
        return self.cleaned_data