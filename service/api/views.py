from rest_framework.generics import ListAPIView, CreateAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from service.models import (
    BranchModel, SeasonModel, BlockModel, ClassModel, SubjectModel,
    GroupModel, LanguageModel, StudentModel, TeacherModel,
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
    BranchSerializer, SeasonSerializer, BlockSerializer, ClassSerializer, SubjectSerializer,
    GroupSerializer, LanguageSerializer, StudentSerializer, TeacherSerializer,
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
from account.models import Account
from django.shortcuts import get_object_or_404

class BranchListAPIView(ListAPIView):
    def get_queryset(self):
        email = self.kwargs.get("email")
        account = get_object_or_404(Account, email=email)
        if account.is_superuser:
            return BranchModel.objects.all()
        else:
            return BranchModel.objects.filter(
                branch_accountant__account__email=email
            )
    serializer_class = BranchSerializer
    permission_classes = (IsAdminUser,)

class BranchSeasonListAPIView(ListAPIView):
    def get_queryset(self):
        id = self.kwargs.get("id")
        return SeasonModel.objects.filter(branch_id=id)
    serializer_class = SeasonSerializer
    permission_classes = (IsAdminUser,)

class BranchCreateAPIView(CreateAPIView):
    queryset = BranchModel.objects.all()
    serializer_class = BranchSerializer
    permission_classes = (IsAdminUser,)

class BranchRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = BranchModel.objects.all()
    serializer_class = BranchSerializer
    permission_classes = (IsAdminUser,)
    lookup_field = "id"

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

class SeasonCreateAPIView(CreateAPIView):
    queryset = SeasonModel.objects.all()
    serializer_class = SeasonSerializer
    permission_classes = (IsAdminUser,)

class SeasonRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = SeasonModel.objects.all()
    serializer_class = SeasonSerializer
    permission_classes = (IsAdminUser,)
    lookup_field = "id"

class BlockListCreateAPIView(ListCreateAPIView):
    queryset = BlockModel.objects.all()
    serializer_class = BlockSerializer
    permission_classes = (IsAdminUser,)

class BlockRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = BlockModel.objects.all()
    serializer_class = BlockSerializer
    permission_classes = (IsAdminUser,)
    lookup_field = "id"

class ClassListAPIView(ListAPIView):
    queryset = ClassModel.objects.all()
    serializer_class = ClassSerializer
    permission_classes = (IsAdminUser,)

class ClassListCreateAPIView(ListCreateAPIView):
    queryset = ClassModel.objects.all()
    serializer_class = ClassSerializer
    permission_classes = (IsAdminUser,)

class ClassRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = ClassModel.objects.all()
    serializer_class = ClassSerializer
    permission_classes = (IsAdminUser,)
    lookup_field = "id"

class SubjectListAPIView(ListAPIView):
    queryset = SubjectModel.objects.all()
    serializer_class = SubjectSerializer
    permission_classes = (IsAdminUser,)

class SubjectListCreateAPIView(ListCreateAPIView):
    queryset = SubjectModel.objects.all()
    serializer_class = SubjectSerializer
    permission_classes = (IsAdminUser,)

class SubjectRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = SubjectModel.objects.all()
    serializer_class = SubjectSerializer
    permission_classes = (IsAdminUser,)
    lookup_field = "id"

class GroupListAPIView(ListAPIView):
    queryset = GroupModel.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (IsAdminUser,)

class GroupListCreateAPIView(ListCreateAPIView):
    queryset = GroupModel.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (IsAdminUser,)

class GroupRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = GroupModel.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (IsAdminUser,)
    lookup_field = "id"

class LanguageListAPIView(ListAPIView):
    queryset = LanguageModel.objects.all()
    serializer_class = LanguageSerializer
    permission_classes = (IsAdminUser,)

class LanguageListCreateAPIView(ListCreateAPIView):
    queryset = LanguageModel.objects.all()
    serializer_class = LanguageSerializer
    permission_classes = (IsAdminUser,)

class LanguageRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = LanguageModel.objects.all()
    serializer_class = LanguageSerializer
    permission_classes = (IsAdminUser,)
    lookup_field = "id"

class AccountantListAPIView(ListAPIView):
    queryset = AccountantModel.objects.all()
    serializer_class = AccountantSerializer
    permission_classes = (IsAdminUser,)

class AbiturientBlockListAPIView(ListAPIView):
    queryset = AbiturientBlockModel.objects.all()
    serializer_class = AbiturientBlockSerializer
    permission_classes = (IsAdminUser,)

class AbiturientClassListAPIView(ListAPIView):
    queryset = AbiturientClassModel.objects.all()
    serializer_class = AbiturientClassSerializer
    permission_classes = (IsAdminUser,)

class AbiturientSubjectListAPIView(ListAPIView):
    queryset = AbiturientSubjectModel.objects.all()
    serializer_class = AbiturientSubjectSerializer
    permission_classes = (IsAdminUser,)

class AbiturientGroupListAPIView(ListAPIView):
    queryset = AbiturientGroupModel.objects.all()
    serializer_class = AbiturientGroupSerializer
    permission_classes = (IsAdminUser,)

class AbiturientListAPIView(ListAPIView):
    def get_queryset(self):
        id = self.kwargs.get("id")
        return AbiturientModel.objects.filter(student__season_id=id)
    serializer_class = AbiturientSerializer
    permission_classes = (IsAdminUser,)

class BlockAbiturientListAPIView(ListAPIView):
    def get_queryset(self):
        id = self.kwargs.get("id")
        block = AbiturientBlockModel.objects.get(id=id)
        return AbiturientModel.objects.filter(blocks=block)
    serializer_class = AbiturientSerializer
    permission_classes = (IsAdminUser,)

class ClassAbiturientListAPIView(ListAPIView):
    def get_queryset(self):
        id = self.kwargs.get("id")
        abiturient_class = AbiturientClassModel.objects.get(id=id)
        return AbiturientModel.objects.filter(abiturient_class=abiturient_class)
    serializer_class = AbiturientSerializer
    permission_classes = (IsAdminUser,)

class SubjectAbiturientListAPIView(ListAPIView):
    def get_queryset(self):
        id = self.kwargs.get("id")
        subject = AbiturientSubjectModel.objects.get(id=id)
        return AbiturientModel.objects.filter(subjects=subject)
    serializer_class = AbiturientSerializer
    permission_classes = (IsAdminUser,)

class GroupAbiturientListAPIView(ListAPIView):
    def get_queryset(self):
        id = self.kwargs.get("id")
        group = AbiturientGroupModel.objects.get(id=id)
        return AbiturientModel.objects.filter(group=group)
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

class ForeignLanguageMasterListAPIView(ListAPIView):
    def get_queryset(self):
        id = self.kwargs.get("id")
        language = MasterForeignLanguageModel.objects.get(id=id)
        return MasterModel.objects.filter(language=language)
    serializer_class = MasterSerializer
    permission_classes = (IsAdminUser,)

class SubjectMasterListAPIView(ListAPIView):
    def get_queryset(self):
        id = self.kwargs.get("id")
        subject = MasterSubjectModel.objects.get(id=id)
        return MasterModel.objects.filter(subjects=subject)
    serializer_class = MasterSerializer
    permission_classes = (IsAdminUser,)

class GroupMasterListAPIView(ListAPIView):
    def get_queryset(self):
        id = self.kwargs.get("id")
        group = MasterGroupModel.objects.get(id=id)
        return MasterModel.objects.filter(group=group)
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

class SubjectMIQListAPIView(ListAPIView):
    def get_queryset(self):
        id = self.kwargs.get("id")
        subject = MIQSubjectModel.objects.get(id=id)
        return MIQModel.objects.filter(subjects=subject)
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

class SubjectCivilServiceListAPIView(ListAPIView):
    def get_queryset(self):
        id = self.kwargs.get("id")
        subject = CivilServiceSubjectModel.objects.get(id=id)
        return CivilServiceModel.objects.filter(subjects=subject)
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

class ProgramTypeComputerCourseListAPIView(ListAPIView):
    def get_queryset(self):
        id = self.kwargs.get("id")
        program_type = ComputerProgramTypeModel.objects.get(id=id)
        return ComputerCourseModel.objects.filter(program_types=program_type)
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

class ClassHighSchoolListAPIView(ListAPIView):
    def get_queryset(self):
        id = self.kwargs.get("id")
        highschool_class = HighSchoolClassModel.objects.get(id=id)
        return HighSchoolModel.objects.filter(highschool_class=highschool_class)
    serializer_class = HighSchoolSerializer
    permission_classes = (IsAdminUser,)

class SubjectHighSchoolListAPIView(ListAPIView):
    def get_queryset(self):
        id = self.kwargs.get("id")
        subject = HighSchoolSubjectModel.objects.get(id=id)
        return HighSchoolModel.objects.filter(subjects=subject)
    serializer_class = HighSchoolSerializer
    permission_classes = (IsAdminUser,)

class GroupHighSchoolListAPIView(ListAPIView):
    def get_queryset(self):
        id = self.kwargs.get("id")
        group = HighSchoolGroupModel.objects.get(id=id)
        return HighSchoolModel.objects.filter(group=group)
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

class SubjectPreSchoolListAPIView(ListAPIView):
    def get_queryset(self):
        id = self.kwargs.get("id")
        subject = PreSchoolSubjectModel.objects.get(id=id)
        return PreSchoolModel.objects.filter(subjects=subject)
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

class ClassPrimarySchoolListAPIView(ListAPIView):
    def get_queryset(self):
        id = self.kwargs.get("id")
        primaryschool_class = PrimarySchoolClassModel.objects.get(id=id)
        return PrimarySchoolModel.objects.filter(primaryschool_class=primaryschool_class)
    serializer_class = PrimarySchoolSerializer
    permission_classes = (IsAdminUser,)

class SubjectPrimarySchoolListAPIView(ListAPIView):
    def get_queryset(self):
        id = self.kwargs.get("id")
        subject = PrimarySchoolSubjectModel.objects.get(id=id)
        return PrimarySchoolModel.objects.filter(subjects=subject)
    serializer_class = PrimarySchoolSerializer
    permission_classes = (IsAdminUser,)

class GroupPrimarySchoolListAPIView(ListAPIView):
    def get_queryset(self):
        id = self.kwargs.get("id")
        group = PrimarySchoolGroupModel.objects.get(id=id)
        return PrimarySchoolModel.objects.filter(group=group)
    serializer_class = PrimarySchoolSerializer
    permission_classes = (IsAdminUser,)