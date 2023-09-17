from django.urls import path
from notification.api import views

urlpatterns = [
    path("notification-list/", views.NotificationListAPIView.as_view(), name="notification-list"),
]