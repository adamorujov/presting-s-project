from rest_framework import serializers
from account.models import Account
from django.contrib.auth.password_validation import validate_password

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ("id", "first_name", "last_name", "email", "is_staff", "is_accountant", "date_joined", "last_login")

class AccountCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = Account
        fields = ('first_name', 'last_name', 'email', 'password', 'is_staff', 'is_accountant')

    def validate(self, data):
        validate_password(data["password"])
        return data

    def create(self, validated_data):
        account = Account.objects.create(
            first_name = validated_data["first_name"]
            last_name = validated_data["last_name"]
            email = validated_data["email"],
            is_staff = validated_data["is_staff"]
            is_accountant = validated_data["is_accountant"]
        )
        account.set_password(validated_data["password"])
        account.save()
        return account
