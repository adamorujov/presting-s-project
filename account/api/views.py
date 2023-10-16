from rest_framework.generics import CreateAPIView, RetrieveAPIView
from account.models import Account
from account.api.serializers import AccountCreateSerializer, AccountSerializer
from rest_framework.permissions import IsAuthenticated

class AccountRetrieveAPIView(RetrieveAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    permission_classes = (IsAuthenticated,)
    lookup_field = 'email'

class AccountCreateAPIView(CreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountCreateSerializer

    