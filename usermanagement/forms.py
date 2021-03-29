from django import forms

from .models import Profile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('contact_no', 'full_name', 'email','district','city','postal_code','street_address','house_no' )
