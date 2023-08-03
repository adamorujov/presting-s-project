from rest_framework.generics import CreateAPIView
from account.models import Account
from account.api.serializers import AccountCreateSerializer

class AccountCreateAPIView(CreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountCreateSerializer
    