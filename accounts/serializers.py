from rest_framework import serializers
from rest_framework.response import Response
from rest_framework import status
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from django.utils.translation import gettext_lazy as _

from django.contrib.auth import get_user_model

User = get_user_model()

#Serializer to get and update User Details 
class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=False,
        validators=[
            UniqueValidator(
                queryset=User.objects.all(), 
                message = _('A user with that email already exists.')
            )
        ]
    )
    current_password = serializers.CharField(
        write_only=True, 
        required=True
    )
    class Meta:
        model = User
        fields = ["id", "first_name", "last_name", "username", "email", "current_password"]
        extra_kwargs = {
            'id': {'read_only':True},
            'username':{'required':False},
            'first_name':{'required':False},
            'last_name':{'required':False},
        }

    def validate_current_password(self, value):
        if not self.instance.check_password(value):
            raise serializers.ValidationError('Wrong password')
        return value


#Serializer to Register User
class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[
            UniqueValidator(
                queryset=User.objects.all(), 
                message = _('A user with that email already exists.')
            )
        ]
    )
    password = serializers.CharField(
        write_only=True, 
        required=True, 
        validators=[validate_password]
    )
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user



class ChangePasswordSerializer(serializers.Serializer):
    model = User

    """
    Serializer for password change endpoint.
    """
    current_password = serializers.CharField(
        write_only=True, 
        required=True
    )
    new_password = serializers.CharField(
        write_only=True, 
        required=True, 
        validators=[validate_password]
    )

    def validate_current_password(self, value):
        if not self.instance.check_password(value):
            raise serializers.ValidationError('Wrong password')
        return value

    def update(self, instance, validated_data):
        instance.set_password(validated_data['new_password'])
        instance.save()
        return instance


class DeleteUserSerializer(serializers.Serializer):
    model = User

    """
    Serializer for user deletion
    """
    current_password = serializers.CharField(
        write_only=True,
        required=True
    )

    def validate_current_password(self, value):
        if not self.instance.check_password(value):
            raise serializers.ValidationError('Wrong password')
        return value

    def update(self, instance, validated_data):
        instance.is_active = False
        instance.save()
        return instance