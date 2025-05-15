from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from django.templatetags.static import static
from django.utils.translation import gettext as _

from rest_framework import serializers
from utils.serializers.password_field import PasswordField

User = get_user_model()


class RegisterSerializer(serializers.ModelSerializer):
    password = PasswordField(write_only=True, validators=[validate_password])
    password_confirm = PasswordField(write_only=True)

    class Meta:
        model = User
        fields = (
            'id',
            'first_name',
            'last_name',
            'image',
            'email',
            'password',
            'password_confirm',
        )

    def validate(self, attrs):
        password = attrs.get('password', '')
        password_confirm = self.initial_data.get('password_confirm', '')

        if not password_confirm:
            raise serializers.ValidationError(
                {
                    'password_confirm': _('This field is required.'),
                }
            )

        if password != password_confirm:
            raise serializers.ValidationError(
                {
                    'password_confirm': _("Passwords do not match."),
                }
            )

        return attrs

    def create(self, validated_data):
        validated_data.pop('password_confirm')
        user = User.objects.create_user(**validated_data)
        return user


class UserInfoSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ('id', 'full_name', 'email', 'image')

    def get_image(self, obj):
        request = self.context.get('request', None)
        if obj.image:
            if request:
                return request.build_absolute_uri(obj.image.url)
            return obj.image.url
        static_url = static('images/user.png')
        return request.build_absolute_uri(static_url) if request else static_url
