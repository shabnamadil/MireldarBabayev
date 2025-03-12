from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import (
    validate_password,
)
from django.utils.translation import gettext as _

from rest_framework import serializers
from rest_framework_simplejwt.serializers import (
    TokenObtainPairSerializer,
)
from utils.serializers.password_field import (
    PasswordField,
)

User = get_user_model()


class RegisterSerializer(serializers.ModelSerializer):
    password = PasswordField(
        write_only=True,
        validators=[validate_password],
    )
    password_confirm = PasswordField(write_only=True)

    class Meta:
        model = User
        extra_kwargs = {"password": {"write_only": True}}
        fields = (
            "id",
            "first_name",
            "last_name",
            "image",
            "email",
            "password",
            "password_confirm",
        )

    def validate(self, attrs):
        password = attrs.get("password", "")
        password_confirm = self.initial_data.get("password_confirm", "")

        if not password_confirm:
            raise serializers.ValidationError(
                {
                    "password_confirm": _("This field is required."),
                }
            )

        if password != password_confirm:
            raise serializers.ValidationError(
                {
                    "password_confirm": _("Passwords do not match."),
                }
            )

        return attrs

    def create(self, validated_data):
        validated_data.pop("password_confirm")
        user = User(
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
            email=validated_data["email"],
            image=validated_data["image"],
        )
        user.set_password(validated_data["password"])
        user.save()
        return user


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        try:
            refresh = self.get_token(self.user)
            access_token = refresh.access_token
            access_token["refresh_jti"] = str(refresh["jti"])
            data["access"] = str(access_token)
            data["refresh"] = str(refresh)
            data.update(
                {
                    "user": {
                        "id": self.user.id,
                        "full_name": self.user.full_name,
                        "email": self.user.email,
                        "image": (
                            self.user.image.url if self.user.image else None
                        ),
                    }
                }
            )
        except Exception as e:
            print(f"Token creation failed: {e}")
            raise e
        return data
