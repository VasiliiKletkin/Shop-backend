from django.contrib.auth import authenticate, get_user_model, login
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers
from rest_framework.authtoken.serializers import AuthTokenSerializer

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    code = serializers.CharField(source='username', read_only=True)

    class Meta:
        model = User
        fields = ['code']
        read_only_fields = ['code']


class CustomAuthTokenSerializer(AuthTokenSerializer):
    username = serializers.CharField(
        label=_("Username"),
        write_only=True
    )
    password = serializers.CharField(
        label=_("Password"),
        style={'input_type': 'password'},
        trim_whitespace=False,
        required=False,
    )
    
    def validate(self, attrs):
        if username := attrs.get('username'):
            user = User.objects.filter(username=username).get()
            login(request=self.context.get('request'), user=user)
            if not user:
                msg = _('Unable to log in with provided credentials.')
                raise serializers.ValidationError(msg, code='authorization')
        else:
            msg = _('Must include "username".')
            raise serializers.ValidationError(msg, code='authorization')

        attrs['user'] = user
        return attrs
