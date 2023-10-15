from django.urls import path
from service.api import views

urlpatterns = [
    path("branch-list/<email>/", views.BranchListAPIView.as_view(), name="branch-list"),
    path("branch-create/", views.BranchCreateAPIView.as_view(), name="branch-create"),
    path("branch-retrieve-update-delete/<int:id>/", views.BranchRetrieveUpdateDestroyAPIView.as_view(), name="branch-retrieve-update-delete"),

    path("branch-season-list/<int:id>/", views.BranchSeasonListAPIView.as_view(), name="branch-list"),
    path("season-create/", views.SeasonCreateAPIView.as_view(), name="season-create"),
    path("season-retrieve-update-delete/<int:id>/", views.SeasonRetrieveUpdateDestroyAPIView.as_view(), name="season-retrieve-update-delete"),

    path("season-student-list/<int:id>/", views.SeasonStudentListAPIView.as_view(), name="season-student-list"),
    path("category-season-student-list/<int:season_id>/<int:category_id>/", views.CategorySeasonStudentListAPIView.as_view(), name="category-season-student-list"),
    path("student-create/", views.StudentCreateAPIView.as_view(), name="student-list-create"),
    path("student-retrieve-update-delete/<int:id>/", views.StudentRetrieveUpdateDestroyAPIView.as_view(), name="student-retrieve-update-delete"),

    path("season-teacher-list/<int:id>/", views.SeasonTeacherListAPIView.as_view(), name="season-teacher-list"),

    path("teacher-create/", views.TeacherCreateAPIView.as_view(), name="teacher-create"),
    path("teacher-retrieve-update-delete/<int:id>/", views.TeacherRetrieveUpdateDestroyAPIView.as_view(), name="teacher-retrieve-update-delete"),

    path("accountant-list/", views.AccountantListAPIView.as_view(), name="accountant-list"),
    path("accountant-create/", views.AccountantCreateAPIView.as_view(), name="accountant-create"),
    path("accountant-retrieve-update-delete/<int:id>/", views.AccountantRetrieveUpdateDestroyAPIView.as_view(), name="accountant-retrieve-update-delete"),

    path("block-list-create/", views.BlockListCreateAPIView.as_view(), name="block-list-create"),
    path("block-retrieve-update-delete/<int:id>/", views.BlockRetrieveUpdateDestroyAPIView.as_view(), name="block-retrieve-update-delete"),

    path("class-list-create/", views.ClassListCreateAPIView.as_view(), name="class-list-create"),
    path("class-retrieve-update-delete/<int:id>/", views.ClassRetrieveUpdateDestroyAPIView.as_view(), name="class-retrieve-update-delete"),

    path("subject-list-create/", views.SubjectListCreateAPIView.as_view(), name="subject-list-create"),
    path("subject-retrieve-update-delete/<int:id>/", views.SubjectRetrieveUpdateDestroyAPIView.as_view(), name="subject-retrieve-update-delete"),

    path("group-list-create/", views.GroupListCreateAPIView.as_view(), name="group-list-create"),
    path("group-retrieve-update-delete/<int:id>/", views.GroupRetrieveUpdateDestroyAPIView.as_view(), name="group-retrieve-update-delete"),

    path("category-list-create/", views.StudentCategoryListCreateAPIView.as_view(), name="category-list-create"),
    path("category-retrieve-update-delete/<int:id>/", views.StudentCategoryRetrieveUpdateDestroyAPIView.as_view(), name="category-retrieve-update-delete"),

    path("language-list-create/", views.LanguageListCreateAPIView.as_view(), name="language-list-create"),
    path("language-retrieve-update-delete/<int:id>/", views.LanguageRetrieveUpdateDestroyAPIView.as_view(), name="language-retrieve-update-delete"),

    # path("abiturient-block-list/", views.AbiturientBlockListAPIView.as_view(), name="abiturient-block-list"),
    # path("block-abiturient-list/<int:id>/", views.BlockAbiturientListAPIView.as_view(), name="block-abiturient-list"),
    # path("abiturient-class-list/", views.AbiturientClassListAPIView.as_view(), name="abiturient-class-list"),
    # path("class-abiturient-list/<int:id>/", views.ClassAbiturientListAPIView.as_view(), name="class-abiturient-list"),
    # path("abiturient-subject-list/", views.AbiturientSubjectListAPIView.as_view(), name="abiturient-subject-list"),
    # path("subject-abiturient-list/<int:id>/", views.SubjectAbiturientListAPIView.as_view(), name="subject-abiturient-list"),
    # path("abiturient-group-list/", views.AbiturientGroupListAPIView.as_view(), name="abiturient-group-list"),
    # path("group-abiturient-list/<int:id>/", views.GroupAbiturientListAPIView.as_view(), name="group-abiturient-list"),
    # path("abiturient-list/<int:id>/", views.AbiturientListAPIView.as_view(), name="abiturient-list"),

    # path("master-foreignlanguage-list/", views.MasterForeignLanguageListAPIView.as_view(), name="master-foreignlanguage-list"),
    # path("foreignlanguage-master-list/<int:id>/", views.ForeignLanguageMasterListAPIView.as_view(), name="foreignlanguage-master-list"),
    # path("master-subject-list/", views.MasterSubjectListAPIView.as_view(), name="master-subject-list"),
    # path("subject-master-list/<int:id>/", views.SubjectMasterListAPIView.as_view(), name="subject-master-list"),
    # path("master-group-list/", views.MasterGroupListAPIView.as_view(), name="master-group-list"),
    # path("group-master-list/<int:id>/", views.GroupMasterListAPIView.as_view(), name="group-master-list"),
    # path("master-list/<int:id>/", views.MasterListAPIView.as_view(), name="master-list"),

    # path("miq-subject-list/", views.MIQSubjectListAPIView.as_view(), name="miq-subject-list"),
    # path("subject-miq-list/<int:id>/", views.SubjectMIQListAPIView.as_view(), name="subject-miq-list"),
    # path("miq-list/<int:id>/", views.MIQListAPIView.as_view(), name="miq-list"),

    # path("civilservice-subject-list/", views.CivilServiceSubjectListAPIView.as_view(), name="civilservice-subject-list"),
    # path("subject-civilservice-list/<int:id>/", views.SubjectCivilServiceListAPIView.as_view(), name="subject-civilservice-list"),
    # path("civilservice-list/<int:id>/", views.CivilServiceListAPIView.as_view(), name="civilservice-list"),

    # path("foreignlanguage-list/<int:id>/", views.ForeignLanguageListAPIView.as_view(), name="foreignlanguage-list"),

    # path("computerprogram-type-list/", views.ComputerProgramTypeListAPIView.as_view(), name="computerprogram-type-list"),
    # path("programtype-computercourse-list/<int:id>/", views.ProgramTypeComputerCourseListAPIView.as_view(), name="programtype-computercourse-list"),
    # path("computercourse-list/<int:id>/", views.ComputerCourseListAPIView.as_view(), name="computercourse-list"),

    # path("accounting-list/<int:id>/", views.AccountingListAPIView.as_view(), name="accounting-list"),

    # path("highschool-class-list/", views.HighSchoolClassListAPIView.as_view(), name="highschool-class-list"),
    # path("class-highschool-list/<int:id>/", views.ClassHighSchoolListAPIView.as_view(), name="class-highschool-list"),
    # path("highschool-subject-list/", views.HighSchoolSubjectListAPIView.as_view(), name="highschool-subject-list"),
    # path("subject-highschool-list/<int:id>/", views.SubjectHighSchoolListAPIView.as_view(), name="subject-highschool-list"),
    # path("highschool-group-list/", views.HighSchoolGroupListAPIView.as_view(), name="highschool-group-list"),
    # path("group-highschool-list/<int:id>/", views.GroupHighSchoolListAPIView.as_view(), name="group-highschool-list"),
    # path("highschool-list/<int:id>/", views.HighSchoolListAPIView.as_view(), name="highschool-list"),

    # path("preschool-subject-list/", views.PreSchoolSubjectListAPIView.as_view(), name="preschool-subject-list"),
    # path("subject-preschool-list/<int:id>/", views.SubjectPreSchoolListAPIView.as_view(), name="subject-preschool-list"),
    # path("preschool-list/<int:id>/", views.PreSchoolListAPIView.as_view(), name="preschool-list"),

    # path("primaryschool-class-list/", views.PrimarySchoolClassListAPIView.as_view(), name="primaryschool-class-list"),
    # path("class-primaryschool-list/<int:id>/", views.ClassPrimarySchoolListAPIView.as_view(), name="class-primaryschool-list"),
    # path("primaryschool-subject-list/", views.PrimarySchoolSubjectListAPIView.as_view(), name="primaryschool-subject-list"),
    # path("subject-primaryschool-list/<int:id>/", views.SubjectPrimarySchoolListAPIView.as_view(), name="subject-primaryschool-list"),
    # path("primaryschool-group-list/", views.PrimarySchoolGroupListAPIView.as_view(), name="primaryschool-group-list"),
    # path("group-primaryschool-list/<int:id>/", views.GroupPrimarySchoolListAPIView.as_view(), name="group-primaryschool-list"),
    # path("primaryschool-list/<int:id>/", views.PrimarySchoolListAPIView.as_view(), name="primaryschool-list"),
]