from rest_framework.generics import (
    ListAPIView, RetrieveAPIView, CreateAPIView, ListCreateAPIView
)
from prestij.models import (
    SettingsModel, BannerModel, ContactInformationModel,
    SocialMediaModel, NewsModel, VideoGalleryModel,
    PhotoGalleryModel, PhotoGalleryItem, TeacherModel, ServiceModel,
    BranchModel, BranchContactNumberModel, SuccessModel,
    SuccessItemModel, ResumeModel, ContactModel, OnlineRegister,
    EditionModel
)
from prestij.api.serializers import (
    SettingsSerializer, BannerSerializer, ContactInformationSerializer,
    SocialMediaSerializer, NewsSerializer, VideoGallerySerializer,
    PhotoGallerySerializer, PhotoGalleryItemSerializer, TeacherSerializer, ServiceSerializer,
    BranchSerializer, BranchContactNumberSerializer, SuccessSerializer,
    SuccessItemSerializer, ResumeSerializer, ContactSerializer, OnlineRegisterSerializer,
    EditionSerializer
)

class SettingsListAPIView(ListAPIView):
    queryset = SettingsModel.objects.all()
    serializer_class = SettingsSerializer

class BannerListAPIView(ListAPIView):
    queryset = BannerModel.objects.all()
    serializer_class = BannerSerializer

class ContactInformationListAPIView(ListAPIView):
    queryset = ContactInformationModel.objects.all()
    serializer_class = ContactInformationSerializer

class SocialMediaListAPIView(ListAPIView):
    queryset = SocialMediaModel.objects.all()
    serializer_class = SocialMediaSerializer

class NewsListAPIView(ListAPIView):
    queryset = NewsModel.objects.all()
    serializer_class = NewsSerializer

class NewsRetrieveAPIView(RetrieveAPIView):
    queryset = NewsModel.objects.all()
    serializer_class = NewsSerializer
    lookup_field = "id"

class VideoGalleryListAPIView(ListAPIView):
    queryset = VideoGalleryModel.objects.all()
    serializer_class = VideoGallerySerializer

class PhotoGalleryListAPIView(ListAPIView):
    queryset = PhotoGalleryModel.objects.all()
    serializer_class = PhotoGallerySerializer

class PhotoGalleryItemListAPIView(ListAPIView):
    queryset = PhotoGalleryItem.objects.all()
    serializer_class = PhotoGalleryItemSerializer

class TeacherListAPIView(ListAPIView):
    queryset = TeacherModel.objects.all()
    serializer_class = TeacherSerializer

class TeacherRetrieveAPIView(RetrieveAPIView):
    queryset = TeacherModel.objects.all()
    serializer_class = TeacherSerializer
    lookup_field = "id"

class ServiceListAPIView(ListAPIView):
    queryset = ServiceModel.objects.all()
    serializer_class = ServiceSerializer

class ServiceRetrieveAPIView(RetrieveAPIView):
    queryset = ServiceModel.objects.all()
    serializer_class = ServiceSerializer
    lookup_field = "id"

class BranchListAPIView(ListAPIView):
    queryset = BranchModel.objects.all()
    serializer_class = BranchSerializer

class BranchContactNumberListAPIView(ListAPIView):
    queryset = BranchContactNumberModel.objects.all()
    serializer_class = BranchContactNumberSerializer

class SuccessListAPIView(ListAPIView):
    queryset = SuccessModel.objects.all()
    serializer_class = SuccessSerializer

class SuccessItemListAPIView(ListAPIView):
    queryset = SuccessItemModel.objects.all()
    serializer_class = SuccessItemSerializer

class ResumeCreateAPIView(CreateAPIView):
    queryset = ResumeModel.objects.all()
    serializer_class = ResumeSerializer

class ContactCreateAPIView(CreateAPIView):
    queryset = ContactModel.objects.all()
    serializer_class = ContactSerializer

class OnlineRegisterCreateAPIView(CreateAPIView):
    queryset = OnlineRegister.objects.all()
    serializer_class = OnlineRegisterSerializer

class EditionListAPIView(ListAPIView):
    queryset = EditionModel.objects.all()
    serializer_class = EditionSerializer

class EditionRetrieveAPIView(RetrieveAPIView):
    queryset = EditionModel.objects.all()
    serializer_class = EditionSerializer
    lookup_field = "id"




