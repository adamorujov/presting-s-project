from django.urls import path
from service.api import views

urlpatterns = [
    path("branch-list/", views.BranchListAPIView.as_view(), name="branch-list"),
    path("branch-season-list/<int:id>/", views.BranchSeasonListAPIView.as_view(), name="branch-list"),
    path("season-student-list/<int:id>/", views.SeasonStudentListAPIView.as_view(), name="season-student-list"),
    path("season-teacher-list/<int:id>/", views.SeasonTeacherListAPIView.as_view(), name="season-teacher-list"),
    path("accountant-list/", views.AccountantListAPIView.as_view(), name="accountant-list"),

    path("abiturient-block-list/", views.AbiturientBlockListAPIView.as_view(), name="abiturient-block-list"),
    path("abiturient-class-list/", views.AbiturientClassListAPIView.as_view(), name="abiturient-class-list"),
    path("abiturient-subject-list/", views.AbiturientSubjectListAPIView.as_view(), name="abiturient-subject-list"),
    path("abiturient-group-list/", views.AbiturientGroupListAPIView.as_view(), name="abiturient-group-list"),
    path("abiturient-list/<int:id>/", views.AbiturientListAPIView.as_view(), name="abiturient-list"),

    path("master-foreignlanguage-list/", views.MasterForeignLanguageListAPIView.as_view(), name="master-foreignlanguage-list"),
    path("master-subject-list/", views.MasterSubjectListAPIView.as_view(), name="master-subject-list"),
    path("master-group-list/", views.MasterGroupListAPIView.as_view(), name="master-group-list"),
    path("master-list/<int:id>/", views.MasterListAPIView.as_view(), name="master-list"),

    path("miq-subject-list/", views.MIQSubjectListAPIView.as_view(), name="miq-subject-list"),
    path("miq-list/<int:id>/", views.MIQListAPIView.as_view(), name="miq-list"),

    path("civilservice-subject-list/", views.CivilServiceSubjectListAPIView.as_view(), name="civilservice-subject-list"),
    path("civilservice-list/<int:id>/", views.CivilServiceListAPIView.as_view(), name="civilservice-list"),

    path("foreignlanguage-list/<int:id>/", views.ForeignLanguageListAPIView.as_view(), name="foreignlanguage-list"),

    path("computerprogram-type-list/", views.ComputerProgramTypeListAPIView.as_view(), name="computerprogram-type-list"),
    path("computercourse-list/<int:id>/", views.ComputerCourseListAPIView.as_view(), name="computercourse-list"),

    path("accounting-list/<int:id>/", views.AccountingListAPIView.as_view(), name="accounting-list"),

    path("highschool-class-list/", views.HighSchoolClassListAPIView.as_view(), name="highschool-class-list"),
    path("highschool-subject-list/", views.HighSchoolSubjectListAPIView.as_view(), name="highschool-subject-list"),
    path("highschool-group-list/", views.HighSchoolGroupListAPIView.as_view(), name="highschool-group-list"),
    path("highschool-list/<int:id>/", views.HighSchoolListAPIView.as_view(), name="highschool-list"),

    path("preschool-subject-list/", views.PreSchoolSubjectListAPIView.as_view(), name="preschool-subject-list"),
    path("preschool-list/<int:id>/", views.PreSchoolListAPIView.as_view(), name="preschool-list"),

    path("primaryschool-class-list/", views.PrimarySchoolClassListAPIView.as_view(), name="primaryschool-class-list"),
    path("primaryschool-subject-list/", views.PrimarySchoolSubjectListAPIView.as_view(), name="primaryschool-subject-list"),
    path("primaryschool-group-list/", views.PrimarySchoolGroupListAPIView.as_view(), name="primaryschool-group-list"),
    path("primaryschool-list/<int:id>/", views.PrimarySchoolListAPIView.as_view(), name="primaryschool-list"),
]