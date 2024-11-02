from django import forms

from .models import (
    Contact,
    SiteSettings
)


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = (
            'full_name',
            'email',
            'phone',
            'subject',
            'message'
        )

    def clean_phone(self) -> str:
        phone = self.cleaned_data.get('phone', '')
        if phone.startswith('+'):
            phone_without_plus = phone[1:]
        else:
            phone_without_plus = phone

        if phone_without_plus and not phone_without_plus.isdigit():
            raise forms.ValidationError('Only numeric values are allowed.')

        if phone_without_plus and len(phone_without_plus) < 10:
            raise forms.ValidationError('Phone number must be at least 10 characters.')
        
        return phone_without_plus
    

class SiteSettingsForm(forms.ModelForm):
    class Meta:
        model = SiteSettings
        fields = '__all__'

    def clean_number(self) -> str:
        number = self.cleaned_data.get('number', '')
        if number.startswith('+'):
            number_without_plus = number[1:]
        else:
            number_without_plus = number

        if number_without_plus and not number_without_plus.isdigit():
            raise forms.ValidationError('Only numeric values are allowed.')

        if number_without_plus and len(number_without_plus) < 10:
            raise forms.ValidationError('Mobile number must be at least 10 characters.')
        
        return number
