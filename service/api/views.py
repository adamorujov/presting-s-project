from rest_framework.generics import ListAPIView
from service.models import (
    BranchModel, SeasonModel, StudentModel, TeacherModel,
    AccountantModel, AbiturientBlockModel, AbiturientClassModel,
    AbiturientSubjectModel, AbiturientGroupModel, AbiturientModel,
    MasterForeignLanguageModel, MasterSubjectModel, MasterGroupModel,
    MasterModel, MIQSubjectModel, MIQModel, CivilServiceSubjectModel, CivilServiceModel,
    ForeignLanguageModel, ComputerProgramTypeModel, ComputerCourseModel,
    AccountingModel, HighSchoolClassModel, HighSchoolSubjectModel,
    HighSchoolGroupModel, HighSchoolModel, PreSchoolSubjectModel,
    PreSchoolModel, PrimarySchoolClassModel, PrimarySchoolSubjectModel,
    PrimarySchoolGroupModel, PrimarySchoolModel, 
)
from account.models import Account
from service.api.serializers import (
    BranchSerializer, SeasonSerializer, StudentSerializer, TeacherSerializer,
    AccountantSerializer, AbiturientBlockSerializer, AbiturientClassSerializer,
    AbiturientSubjectSerializer, AbiturientGroupSerializer, AbiturientSerializer,
    MasterForeignLanguageSerializer, MasterSubjectSerializer, MasterGroupSerializer,
    MasterSerializer, MIQSubjectSerializer, MIQSerializer,
    CivilServiceSubjectSerializer, CivilServiceSerializer, ForeignLanguageSerializer,
    ComputerProgramTypeSerializer, ComputerCourseSerializer, AccountingSerializer,
    HighSchoolClassSerializer, HighSchoolSubjectSerializer, HighSchoolGroupSerializer,
    HighSchoolSerializer, PreSchoolSubjectSerializer, PreSchoolSerializer,
    PrimarySchoolClassSerializer, PrimarySchoolSubjectSerializer, PrimarySchoolGroupSerializer,
    PrimarySchoolSerializer
)
from rest_framework.permissions import IsAdminUser

class BranchListAPIView(ListAPIView):
    queryset = BranchModel.objects.all()
    serializer_class = BranchSerializer
    permission_classes = (IsAdminUser,)

class BranchSeasonListAPIView(ListAPIView):
    def get_queryset(self):
        id = self.kwargs.get("id")
        return SeasonModel.objects.filter(branch_id=id)
    serializer_class = SeasonSerializer
    permission_classes = (IsAdminUser,)

class SeasonStudentListAPIView(ListAPIView):
    def get_queryset(self):
        id = self.kwargs.get("id")
        return StudentModel.objects.filter(season_id=id)
    serializer_class = StudentSerializer
    permission_classes = (IsAdminUser,)

class SeasonTeacherListAPIView(ListAPIView):
    def get_queryset(self):
        id = self.kwargs.get("id")
        return TeacherModel.objects.filter(season_id=id)
    serializer_class = TeacherSerializer
    permission_classes = (IsAdminUser,)

class AccountantListAPIView(ListAPIView):
    queryset = AccountantModel.objects.all()
    serializer_class = AccountantSerializer
    permission_classes = (IsAdminUser,)

class AbiturientBlockListAPIView(ListAPIView):
    queryset = AbiturientBlockModel
    serializer_class = AbiturientBlockSerializer
    permission_classes = (IsAdminUser,)

class AbiturientClassListAPIView(ListAPIView):
    queryset = AbiturientClassModel
    serializer_class = AbiturientClassSerializer
    permission_classes = (IsAdminUser,)

class AbiturientSubjectListAPIView(ListAPIView):
    queryset = AbiturientSubjectModel
    serializer_class = AbiturientSubjectSerializer
    permission_classes = (IsAdminUser,)

class AbiturientGroupListAPIView(ListAPIView):
    queryset = AbiturientGroupModel
    serializer_class = AbiturientGroupSerializer
    permission_classes = (IsAdminUser,)

class AbiturientListAPIView(ListAPIView):
    def get_queryset(self):
        id = self.kwargs.get("id")
        return AbiturientModel.objects.filter(student__season_id=id)
    serializer_class = AbiturientSerializer
    permission_classes = (IsAdminUser,)

class MasterForeignLanguageListAPIView(ListAPIView):
    queryset = MasterForeignLanguageModel.objects.all()
    serializer_class = MasterForeignLanguageSerializer
    permission_classes = (IsAdminUser,)

class MasterSubjectListAPIView(ListAPIView):
    queryset = MasterSubjectModel.objects.all()
    serializer_class = MasterSubjectSerializer
    permission_classes = (IsAdminUser,)

class MasterGroupListAPIView(ListAPIView):
    queryset = MasterGroupModel.objects.all()
    serializer_class = MasterGroupSerializer
    permission_classes = (IsAdminUser,)

class MasterListAPIView(ListAPIView):
    def get_queryset(self):
        id = self.kwargs.get("id")
        return MasterModel.objects.filter(student__season_id=id)
    serializer_class = MasterSerializer
    permission_classes = (IsAdminUser,)

class MIQSubjectListAPIView(ListAPIView):
    queryset = MIQSubjectModel.objects.all()
    serializer_class = MIQSubjectSerializer
    permission_classes = (IsAdminUser,)

class MIQListAPIView(ListAPIView):
    def get_queryset(self):
        id = self.kwargs.get("id")
        return MIQModel.objects.filter(student__season_id=id)
    serializer_class = MIQSerializer
    permission_classes = (IsAdminUser,)

class CivilServiceSubjectListAPIView(ListAPIView):
    queryset = CivilServiceSubjectModel.objects.all()
    serializer_class = CivilServiceSubjectSerializer
    permission_classes = (IsAdminUser,)

class CivilServiceListAPIView(ListAPIView):
    def get_queryset(self):
        id = self.kwargs.get("id")
        return CivilServiceModel.objects.filter(student__season_id=id)
    serializer_class = CivilServiceSerializer
    permission_classes = (IsAdminUser,)

class ForeignLanguageListAPIView(ListAPIView):
    def get_queryset(self):
        id = self.kwargs.get("id")
        return ForeignLanguageModel.objects.filter(student__season_id=id)
    serializer_class = ForeignLanguageSerializer
    permission_classes = (IsAdminUser,)

class ComputerProgramTypeListAPIView(ListAPIView):
    queryset = ComputerProgramTypeModel.objects.all()
    serializer_class = ComputerProgramTypeSerializer
    permission_classes = (IsAdminUser,)

class ComputerCourseListAPIView(ListAPIView):
    def get_queryset(self):
        id = self.kwargs.get("id")
        return ComputerCourseModel.objects.filter(student__season_id=id)
    serializer_class = ComputerCourseSerializer
    permission_classes = (IsAdminUser,)

class AccountingListAPIView(ListAPIView):
    def get_queryset(self):
        id = self.kwargs.get("id")
        return AccountingModel.objects.filter(student__season_id=id)
    serializer_class = AccountingSerializer
    permission_classes = (IsAdminUser,)

class HighSchoolClassListAPIView(ListAPIView):
    queryset = HighSchoolClassModel.objects.all()
    serializer_class = HighSchoolClassSerializer
    permission_classes = (IsAdminUser,)

class HighSchoolSubjectListAPIView(ListAPIView):
    queryset = HighSchoolSubjectModel.objects.all()
    serializer_class = HighSchoolSubjectSerializer
    permission_classes = (IsAdminUser,)

class HighSchoolGroupListAPIView(ListAPIView):
    queryset = HighSchoolGroupModel.objects.all()
    serializer_class = HighSchoolGroupSerializer
    permission_classes = (IsAdminUser,)

class HighSchoolListAPIView(ListAPIView):
    def get_queryset(self):
        id = self.kwargs.get("id")
        return HighSchoolModel.objects.filter(student__season_id=id)
    serializer_class = HighSchoolSerializer
    permission_classes = (IsAdminUser,)

class PreSchoolSubjectListAPIView(ListAPIView):
    queryset = PreSchoolSubjectModel.objects.all()
    serializer_class = PreSchoolSubjectSerializer
    permission_classes = (IsAdminUser,)

class PreSchoolListAPIView(ListAPIView):
    def get_queryset(self):
        id = self.kwargs.get("id")
        return PreSchoolModel.objects.filter(student__season_id=id)
    serializer_class = PreSchoolSerializer
    permission_classes = (IsAdminUser,)

class PrimarySchoolClassListAPIView(ListAPIView):
    queryset = PrimarySchoolClassModel.objects.all()
    serializer_class = PrimarySchoolClassSerializer
    permission_classes = (IsAdminUser,)

class PrimarySchoolSubjectListAPIView(ListAPIView):
    queryset = PrimarySchoolSubjectModel.objects.all()
    serializer_class = PrimarySchoolSubjectSerializer
    permission_classes = (IsAdminUser,)

class PrimarySchoolGroupListAPIView(ListAPIView):
    queryset = PrimarySchoolGroupModel.objects.all()
    serializer_class = PrimarySchoolGroupSerializer
    permission_classes = (IsAdminUser,)

class PrimarySchoolListAPIView(ListAPIView):
    def get_queryset(self):
        id = self.kwargs.get("id")
        return PrimarySchoolModel.objects.filter(student__season_id=id)
    serializer_class = PrimarySchoolSerializer
    permission_classes = (IsAdminUser,)