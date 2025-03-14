from rest_framework import serializers
from utils.helpers.validate_phone import validate_phone_value

from ..models import Contact, Newsletter


class NewsletterPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Newsletter
        fields = ('id', 'email')


class ContactPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ('first_name', 'last_name', 'email', 'phone', 'message')

    def validate(self, attrs):
        phone = attrs.get('phone', '')
        validate_phone_value(phone)
        return super().validate(attrs)
