from rest_framework.generics import ListAPIView
from notification.api.serializers import NotificationSerializer
from notification.models import NotificationModel
from notification.api.permissions import IsSuperUser

class NotificationListAPIView(ListAPIView):
    queryset = NotificationModel.objects.all()
    serializer_class = NotificationSerializer
    permission_classes = (IsSuperUser,)

