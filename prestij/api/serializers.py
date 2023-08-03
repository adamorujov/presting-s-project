from rest_framework import serializers
from prestij.models import (
    SettingsModel, BannerModel, ContactInformationModel,
    SocialMediaModel, NewsModel, VideoGalleryModel,
    PhotoGalleryModel, PhotoGalleryItem, TeacherModel, ServiceModel,
    BranchModel, BranchContactNumberModel, SuccessModel,
    SuccessItemModel, ResumeModel, ContactModel, OnlineRegister, 
    EditionModel
)

class SettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SettingsModel
        fields = "__all__"

class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = BannerModel
        fields = "__all__"

class ContactInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactInformationModel
        fields = "__all__"

class SocialMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialMediaModel
        fields = "__all__"

class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsModel
        fields = "__all__"

class VideoGallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoGalleryModel
        fields = "__all__"

class PhotoGallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = PhotoGalleryModel
        fields = "__all__"

class PhotoGalleryItemSerializer(serializers.ModelSerializer):
    photo_gallery = PhotoGallerySerializer()
    class Meta:
        model = PhotoGalleryItem
        fields = "__all__"

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeacherModel
        fields = "__all__"

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceModel
        fields = "__all__"

class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = BranchModel
        fields = "__all__"

class BranchContactNumberSerializer(serializers.ModelSerializer):
    branch = BranchSerializer()
    class Meta:
        model = BranchContactNumberModel
        fields = "__all__"

class SuccessSerializer(serializers.ModelSerializer):
    class Meta:
        model = SuccessModel
        fields = "__all__"

class SuccessItemSerializer(serializers.ModelSerializer):
    success = SuccessSerializer()
    class Meta:
        model = SuccessItemModel
        fields = "__all__"

class ResumeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResumeModel
        fields = "__all__"

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactModel
        fields = "__all__"

class OnlineRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = OnlineRegister
        fields = "__all__"

class EditionSerializer(serializers.ModelSerializer):
    class Meta:
        model = EditionModel
        fields = "__all__"