from django.urls import path
from account.api import views

urlpatterns = [
    path('account-create/', views.AccountCreateAPIView.as_view(), name="account-create"),
]