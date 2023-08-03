from django.urls import path
from prestij.api import views

urlpatterns = [
    path('settings-list/', views.SettingsListAPIView.as_view(), name="settings"),
    path('banners-list/', views.BannerListAPIView.as_view(), name="banners"),
    path('contactinformation-list/', views.ContactInformationListAPIView.as_view(), name="contactinformation-list"),
    path('socialmedia-list/', views.SocialMediaListAPIView.as_view(), name="socialmedia"),
    path('news-list/', views.NewsListAPIView.as_view(), name="news-list"),
    path('news-retrieve/<int:id>/', views.NewsRetrieveAPIView.as_view(), name="news-retrive"),
    path('videogallery-list/', views.VideoGalleryListAPIView.as_view(), name="videogallery-list"),
    path('photogallery-list/', views.PhotoGalleryListAPIView.as_view(), name="photogallery-list"),
    path('photogalleryitem-list/', views.PhotoGalleryItemListAPIView.as_view(), name="photogalleryitem-list"),
    path('teacher-list/', views.TeacherListAPIView.as_view(), name="teacher-list"),
    path('teacher-retrieve/<int:id>/', views.TeacherRetrieveAPIView.as_view(), name="teacher-retrieve"),
    path('service-list/', views.ServiceListAPIView.as_view(), name="service-list"),
    path('service-retrieve/<int:id>/', views.ServiceRetrieveAPIView.as_view(), name="service-retrieve"),
    path('branch-list/', views.BranchListAPIView.as_view(), name="branch-list"),
    path('branchcontactnumber-list/', views.BranchContactNumberListAPIView.as_view(), name="branchcontactnumber-list"),
    path('success-list/', views.SuccessListAPIView.as_view(), name="success-list"),
    path('successitem-list/', views.SuccessItemListAPIView.as_view(), name="successitem-list"),
    path('resume-create/', views.ResumeCreateAPIView.as_view(), name="resume-create"),
    path('contact-create/', views.ContactCreateAPIView.as_view(), name="contact-create"),
    path('onlineregister-create/', views.OnlineRegisterCreateAPIView.as_view(), name="onlineregister-create"),
    path("edition-list/", views.EditionListAPIView.as_view(), name="edition-list"),
    path("edition-retrieve/<int:id>/", views.EditionRetrieveAPIView.as_view(), name="edition-retrieve"),
]