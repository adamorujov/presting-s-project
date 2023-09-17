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
        fields = ('email', 'password', 'is_accountant')

    def validate(self, data):
        validate_password(data["password"])
        return data

    def create(self, validated_data):
        account = Account.objects.create(
            email = validated_data["email"],
            is_accountant = validated_data["is_accountant"]
        )
        account.set_password(validated_data["password"])
        account.save()
        return account
