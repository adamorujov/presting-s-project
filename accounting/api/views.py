from rest_framework.generics import ListAPIView, RetrieveUpdateAPIView
from accounting.models import (
    MonthModel, TeacherPaymentInformationModel, StudentPaymentInformationModel
)
from service.models import StudentCategoryModel

from accounting.api.serializers import (
    MonthSerializer, TeacherPaymentInformationSerializer, TeacherPaymentInformationUpdateSerializer, 
    StudentPaymentInformationSerializer, StudentPaymentInformationUpdateSerializer
)
from rest_framework.permissions import IsAdminUser
from django.shortcuts import get_object_or_404

class SeasonMonthListAPIView(ListAPIView):
    def get_queryset(self):
        season_id = self.kwargs["id"]
        return MonthModel.objects.filter(
            season_id=season_id
        )
    serializer_class = MonthSerializer
    permission_classes = (IsAdminUser,)

class TeacherMonthPaymentInformationListAPIView(ListAPIView):
    def get_queryset(self):
        month_id = self.kwargs["id"]
        return TeacherPaymentInformationModel.objects.filter(
            month_id=month_id
        )
    serializer_class = TeacherPaymentInformationSerializer
    permission_classes = (IsAdminUser,)

class MonthTeacherPaymentInformationListAPIView(ListAPIView):
    def get_queryset(self):
        teacher_id = self.kwargs["id"]
        return TeacherPaymentInformationModel.objects.filter(
            teacher_id=teacher_id
        )
    serializer_class = TeacherPaymentInformationSerializer
    permission_classes = (IsAdminUser,) 

class TeacherPaymentInformationRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    queryset = TeacherPaymentInformationModel.objects.all()
    serializer_class = TeacherPaymentInformationUpdateSerializer
    permission_classes = (IsAdminUser,) 
    lookup_field = "id"

class StudentMonthPaymentInformationListAPIView(ListAPIView):
    def get_queryset(self):
        month_id = self.kwargs.get("month_id")
        return StudentPaymentInformationModel.objects.filter(
            month_id=month_id
        )
    serializer_class = StudentPaymentInformationSerializer
    permission_classes = (IsAdminUser,) 

class StudentCategoryMonthPaymentInformationListAPIView(ListAPIView):
    def get_queryset(self):
        month_id = self.kwargs.get("month_id")
        category_id = self.kwargs.get("category_id")
        category = get_object_or_404(StudentCategoryModel, id=category_id)
        return StudentPaymentInformationModel.objects.filter(
            student__categories=category,
            month_id=month_id
        )
    serializer_class = StudentPaymentInformationSerializer
    permission_classes = (IsAdminUser,) 

class MonthStudentPaymentInformationListAPIView(ListAPIView):
    def get_queryset(self):
        student_id = self.kwargs["id"]
        return StudentPaymentInformationModel.objects.filter(
            student_id=student_id
        )
    serializer_class = StudentPaymentInformationSerializer
    permission_classes = (IsAdminUser,)

class StudentPaymentInformationRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    queryset = StudentPaymentInformationModel.objects.all()
    serializer_class = StudentPaymentInformationUpdateSerializer
    permission_classes = (IsAdminUser,) 
    lookup_field = "id"

# class AbiturientMonthPaymentInformationListAPIView(ListAPIView):
#     def get_queryset(self):
#         month_id = self.kwargs["id"]
#         return AbiturientPaymentInformationModel.objects.filter(
#             month_id=month_id
#         )
#     serializer_class = AbiturientPaymentInformationSerializer
#     permission_classes = (IsAdminUser,) 

# class MonthAbiturientPaymentInformationListAPIView(ListAPIView):
#     def get_queryset(self):
#         abiturient_id = self.kwargs["id"]
#         return AbiturientPaymentInformationModel.objects.filter(
#             abiturient_id=abiturient_id
#         )
#     serializer_class = AbiturientPaymentInformationSerializer
#     permission_classes = (IsAdminUser,) 

# class MasterMonthPaymentInformationListAPIView(ListAPIView):
#     def get_queryset(self):
#         month_id = self.kwargs["id"]
#         return MasterPaymentInformationModel.objects.filter(
#             month_id=month_id
#         )
#     serializer_class = MasterPaymentInformationSerializer
#     permission_classes = (IsAdminUser,) 

# class MonthMasterPaymentInformationListAPIView(ListAPIView):
#     def get_queryset(self):
#         master_id = self.kwargs["id"]
#         return MasterPaymentInformationModel.objects.filter(
#             master_id=master_id
#         )
#     serializer_class = MasterPaymentInformationSerializer
#     permission_classes = (IsAdminUser,) 

# class MIQMonthPaymentInformationListAPIView(ListAPIView):
#     def get_queryset(self):
#         month_id = self.kwargs["id"]
#         return MIQPaymentInformationModel.objects.filter(
#             month_id=month_id
#         )
#     serializer_class = MIQPaymentInformationSerializer
#     permission_classes = (IsAdminUser,) 

# class MonthMIQPaymentInformationListAPIView(ListAPIView):
#     def get_queryset(self):
#         miq_id = self.kwargs["id"]
#         return MIQPaymentInformationModel.objects.filter(
#             miq_id=miq_id
#         )
#     serializer_class = MIQPaymentInformationSerializer
#     permission_classes = (IsAdminUser,) 

# class ForeignLanguageMonthPaymentInformationListAPIView(ListAPIView):
#     def get_queryset(self):
#         month_id = self.kwargs["id"]
#         return ForeignLanguagePaymentInformationModel.objects.filter(
#             month_id=month_id
#         )
#     serializer_class = ForeignLanguagePaymentInformationSerializer
#     permission_classes = (IsAdminUser,) 

# class MonthForeignLanguagePaymentInformationListAPIView(ListAPIView):
#     def get_queryset(self):
#         foreignlanguage_id = self.kwargs["id"]
#         return ForeignLanguagePaymentInformationModel.objects.filter(
#             foreignlanguage_id=foreignlanguage_id
#         )
#     serializer_class = ForeignLanguagePaymentInformationSerializer
#     permission_classes = (IsAdminUser,) 

# class ComputerCourseMonthPaymentInformationListAPIView(ListAPIView):
#     def get_queryset(self):
#         month_id = self.kwargs["id"]
#         return ComputerCoursePaymentInformationModel.objects.filter(
#             month_id=month_id
#         )
#     serializer_class = ComputerCoursePaymentInformationSerializer
#     permission_classes = (IsAdminUser,) 

# class MonthComputerCoursePaymentInformationListAPIView(ListAPIView):
#     def get_queryset(self):
#         computercourse_id = self.kwargs["id"]
#         return ComputerCoursePaymentInformationModel.objects.filter(
#             computercourse_id=computercourse_id
#         )
#     serializer_class = ComputerCoursePaymentInformationSerializer
#     permission_classes = (IsAdminUser,) 

# class CivilServiceMonthPaymentInformationListAPIView(ListAPIView):
#     def get_queryset(self):
#         month_id = self.kwargs["id"]
#         return CivilServicePaymentInformationModel.objects.filter(
#             month_id=month_id
#         )
#     serializer_class = CivilServicePaymentInformationSerializer
#     permission_classes = (IsAdminUser,) 

# class MonthCivilServicePaymentInformationListAPIView(ListAPIView):
#     def get_queryset(self):
#         civilservice_id = self.kwargs["id"]
#         return CivilServicePaymentInformationModel.objects.filter(
#             civilservice_id=civilservice_id
#         )
#     serializer_class = CivilServicePaymentInformationSerializer
#     permission_classes = (IsAdminUser,) 

# class AccountingMonthPaymentInformationListAPIView(ListAPIView):
#     def get_queryset(self):
#         month_id = self.kwargs["id"]
#         return AccountingPaymentInformationModel.objects.filter(
#             month_id=month_id
#         )
#     serializer_class = AccountingPaymentInformationSerializer
#     permission_classes = (IsAdminUser,) 

# class MonthAccountingPaymentInformationListAPIView(ListAPIView):
#     def get_queryset(self):
#         accounting_id = self.kwargs["id"]
#         return AccountingPaymentInformationModel.objects.filter(
#             accounting_id=accounting_id
#         )
#     serializer_class = AccountingPaymentInformationSerializer
#     permission_classes = (IsAdminUser,) 

# class HighSchoolMonthPaymentInformationListAPIView(ListAPIView):
#     def get_queryset(self):
#         month_id = self.kwargs["id"]
#         return HighSchoolPaymentInformationModel.objects.filter(
#             month_id=month_id
#         )
#     serializer_class = HighSchoolPaymentInformationSerializer
#     permission_classes = (IsAdminUser,) 

# class MonthHighSchoolPaymentInformationListAPIView(ListAPIView):
#     def get_queryset(self):
#         highschool_id = self.kwargs["id"]
#         return HighSchoolPaymentInformationModel.objects.filter(
#             highschool_id=highschool_id
#         )
#     serializer_class = HighSchoolPaymentInformationSerializer
#     permission_classes = (IsAdminUser,) 

# class PreSchoolMonthPaymentInformationListAPIView(ListAPIView):
#     def get_queryset(self):
#         month_id = self.kwargs["id"]
#         return PreSchoolPaymentInformationModel.objects.filter(
#             month_id=month_id
#         )
#     serializer_class = PreSchoolPaymentInformationSerializer
#     permission_classes = (IsAdminUser,)

# class MonthPreSchoolPaymentInformationListAPIView(ListAPIView):
#     def get_queryset(self):
#         preschool_id = self.kwargs["id"]
#         return PreSchoolPaymentInformationModel.objects.filter(
#             preschool_id=preschool_id
#         )
#     serializer_class = PreSchoolPaymentInformationSerializer
#     permission_classes = (IsAdminUser,)

# class PrimarySchoolMonthPaymentInformationListAPIView(ListAPIView):
#     def get_queryset(self):
#         month_id = self.kwargs["id"]
#         return PrimarySchoolPaymentInformationModel.objects.filter(
#             month_id=month_id
#         )
#     serializer_class = PrimarySchoolPaymentInformationSerializer
#     permission_classes = (IsAdminUser,) 

# class MonthPrimarySchoolPaymentInformationListAPIView(ListAPIView):
#     def get_queryset(self):
#         primaryschool_id = self.kwargs["id"]
#         return PrimarySchoolPaymentInformationModel.objects.filter(
#             primaryschool_id=primaryschool_id
#         )
#     serializer_class = PrimarySchoolPaymentInformationSerializer
#     permission_classes = (IsAdminUser,) 

