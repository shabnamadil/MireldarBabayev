from django.core.exceptions import ValidationError

from rest_framework import serializers

from ..models import (
    Newsletter,
    Contact
)


class NewsletterPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Newsletter
        fields = (
            'id',
            'email'
        )


class ContactPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = (
            'first_name',
            'last_name',
            'email',
            'phone',
            'message'
        )

    def validate(self, attrs):
        phone = attrs.get('phone', '')

        if phone.startswith('+'):
            phone_without_plus = phone[1:]
        else:
            phone_without_plus = phone

        if phone_without_plus and not phone_without_plus.isdigit():
            raise ValidationError({'phone': 'Only numeric values are allowed.'})
        if phone_without_plus and len(phone_without_plus) < 10:
            raise ValidationError({'phone': 'Phone number must be at least 10 characters.'})
        
        return super().validate(attrs)