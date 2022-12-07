from django.contrib.auth import authenticate
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import password_validation

from rest_framework import serializers

from users.models import User


class LoginSerializer(serializers.Serializer):
    nickname = serializers.CharField(
        label=_("Nickname"),
        write_only=True
    )
    password = serializers.CharField(
        label=_("Password"),
        style={'input_type': 'password'},
        trim_whitespace=False,
        write_only=True
    )
    token = serializers.CharField(
        label=_("Token"),
        read_only=True
    )

    def validate(self, attrs):
        nickname = attrs.get('nickname')
        password = attrs.get('password')

        if nickname and password:
            user = authenticate(request=self.context.get('request'),
                                nickname=nickname, password=password)

            if not user:
                msg = _('Unable to log in with provided credentials.')
                raise serializers.ValidationError(msg, code='authorization')
        else:
            msg = _('Must include "nickname" and "password".')
            raise serializers.ValidationError(msg, code='authorization')

        attrs['user'] = user
        return attrs


class UserSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={"input_type": "password"}, write_only=True)

    class Meta:
        model = User
        fields = ('id', 'name', 'last_name', 'nickname', 'password', 'password2')
        extra_kwargs = {'password': {'write_only': True}}

    def validate(self, data):
        password = data.get('password')
        password2 = data.pop('password2')
        if password != password2:
            raise serializers.ValidationError({'password': 'Passwords must match.'})
        password_validation.validate_password(password, self.instance)
        return data

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user