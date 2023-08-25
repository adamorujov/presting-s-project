from django.urls import path
from accounting.api import views

urlpatterns = [
    path('season-month-list/<int:id>/', views.SeasonMonthListAPIView.as_view(), name="month-list"),
    path('abiturient-month-payment-list/<int:id>/', views.AbiturientMonthPaymentInformationListAPIView.as_view(), name="abiturient-month-payment-list"),
    path('month-abiturient-payment-list/<int:id>/', views.MonthAbiturientPaymentInformationListAPIView.as_view(), name="month-abiturient-payment-list"),
    path('master-month-payment-list/<int:id>/', views.MasterMonthPaymentInformationListAPIView.as_view(), name="master-month-payment-list"),
    path('month-master-payment-list/<int:id>/', views.MonthMasterPaymentInformationListAPIView.as_view(), name="month-master-payment-list"),
    path('miq-month-payment-list/<int:id>/', views.MIQMonthPaymentInformationListAPIView.as_view(), name="miq-month-payment-list"),
    path('month-miq-payment-list/<int:id>/', views.MonthMIQPaymentInformationListAPIView.as_view(), name="month-miq-payment-list"),
    path('civilservice-month-payment-list/<int:id>/', views.CivilServiceMonthPaymentInformationListAPIView.as_view(), name="civilservice-month-payment-list"),
    path('month-civilservice-payment-list/<int:id>/', views.MonthCivilServicePaymentInformationListAPIView.as_view(), name="month-civilservice-payment-list"),
    path('foreignlanguage-month-payment-list/<int:id>/', views.ForeignLanguageMonthPaymentInformationListAPIView.as_view(), name="foreignlanguage-month-payment-list"),
    path('month-foreignlanguage-payment-list/<int:id>/', views.MonthForeignLanguagePaymentInformationListAPIView.as_view(), name="month-foreignlanguage-payment-list"),
    path('computercourse-month-payment-list/<int:id>/', views.ComputerCourseMonthPaymentInformationListAPIView.as_view(), name="computercourse-month-payment-list"),
    path('month-computercourse-payment-list/<int:id>/', views.MonthComputerCoursePaymentInformationListAPIView.as_view(), name="month-computercourse-payment-list"),
    path('accounting-month-payment-list/<int:id>/', views.AccountingMonthPaymentInformationListAPIView.as_view(), name="accounting-month-payment-list"),
    path('month-accounting-payment-list/<int:id>/', views.MonthAccountingPaymentInformationListAPIView.as_view(), name="month-accounting-payment-list"),
    path('highschool-month-payment-list/<int:id>/', views.HighSchoolMonthPaymentInformationListAPIView.as_view(), name="highschool-month-payment-list"),
    path('month-highschool-payment-list/<int:id>/', views.MonthHighSchoolPaymentInformationListAPIView.as_view(), name="month-highschool-payment-list"),
    path('preschool-month-payment-list/<int:id>/', views.PreSchoolMonthPaymentInformationListAPIView.as_view(), name="preschool-month-payment-list"),
    path('month-preschool-payment-list/<int:id>/', views.MonthPreSchoolPaymentInformationListAPIView.as_view(), name="month-preschool-payment-list"),
    path('primaryschool-month-payment-list/<int:id>/', views.PrimarySchoolMonthPaymentInformationListAPIView.as_view(), name="primaryschool-month-payment-list"),
    path('month-primaryschool-payment-list/<int:id>/', views.MonthPrimarySchoolPaymentInformationListAPIView.as_view(), name="month-primaryschool-payment-list"),
]