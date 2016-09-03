from rest_framework import serializers
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import authenticate

from rest_framework.authtoken.models import Token

from .models import Profile, USER_ROLE_CHOICES


class AuthMixin(object):
    """
    authenticate user credentials
    """
    messages_text = {
        "invalid": _("The email address and/or password are not correct."),
        "disabled": _("This account is not activated."),
    }

    def user_credentials(self, attrs):
        """
        Provides the credentials required to authenticate the user for login.
        """
        credentials = {}
        credentials["email"] = attrs["email"].lower()
        credentials["password"] = attrs["password"]
        return credentials

    def validate_user_credentials(self, data):
        user = authenticate(**self.user_credentials(data))
        if user:
            if user.is_active:
                self.instance = user
            else:
                raise serializers.ValidationError(
                    self.messages_text["disabled"])
        else:
            raise serializers.ValidationError(self.messages_text["invalid"])
        return user


class RegisterSerializer(serializers.ModelSerializer, AuthMixin):

    """ Profile Serializer for User Signup """
    # password_confirmation = serializers.CharField(
    #     max_length=40)

    # def validate(self, data, format=None):
    #     """
    #     password_confirmation check
    #     """
    #     password_confirmation = data.get('password_confirmation')
    #     password = data.get('password')
    #     if password_confirmation != password:
    #         raise serializers.ValidationError(
    #             _('Password confirmation mismatch'))
    #     return data

    def validate_email(self, value):
        try:
            Profile.objects.get(email=value.lower())
        except Profile.DoesNotExist:
            return value.lower()
        raise serializers.ValidationError(
            _('User already registered with this Email ID.'))

    def create(self, validated_data):
        """
        Create a new User instance.
        """
        # del validated_data['password_confirmation']
        validated_data['username'] = validated_data.get('email')
        self.instance = Profile.objects.create_user(**validated_data)
        return self.validate_user_credentials(validated_data)

    class Meta:
        model = Profile
        fields = (
            'name', 'email', 'password',
        )


class TokenSerializer(serializers.ModelSerializer):
    auth_token = serializers.CharField(source='key', read_only=True)

    class Meta:
        model = Token
        fields = (
            'auth_token',
        )


class LoginSerializer(serializers.Serializer, AuthMixin):

    """
    User serializer with custom fields for authentication
    """
    email = serializers.CharField(
        max_length=Profile._meta.get_field('email').max_length)
    password = serializers.CharField(max_length=Profile._meta.get_field('email').max_length)

    def validate(self, data):
        """ validate login credentials """
        user = self.validate_user_credentials(data)
        if user.account_activated is not True and not user.is_superuser:
            raise serializers.ValidationError(_("Account is not activated yet."))
        return data


class LogOutSerializer(serializers.Serializer):
    pass


class ProfileMiniSerializer(serializers.ModelSerializer):
    """
    profile of user mini serializer
    """
    role = serializers.SerializerMethodField('get_user_role')

    def get_user_role(self, obj):
        return [item[1] for item in USER_ROLE_CHOICES if item[0] == obj.role][0]

    class Meta:
        model = Profile
        fields = ('id', 'first_name', 'last_name', 'email', 'role')
