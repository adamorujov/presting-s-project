from rest_framework import serializers
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

class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = BranchModel
        fields = "__all__"

class SeasonSerializer(serializers.ModelSerializer):
    branch = serializers.SlugRelatedField(queryset=BranchModel.objects.all(), slug_field="name")

    class Meta:
        model = SeasonModel
        fields = "__all__"

class BlockSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlockModel
        fields = "__all__"

class ClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassModel
        fields = "__all__"

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubjectModel
        fields = "__all__"

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupModel
        fields = "__all__"

class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = LanguageModel
        fields = "__all__"

class StudentSerializer(serializers.ModelSerializer):
    season = serializers.SlugRelatedField(queryset=SeasonModel.objects.all(), slug_field="name")

    class Meta:
        model = StudentModel
        fields = "__all__"

class TeacherSerializer(serializers.ModelSerializer):
    season = serializers.SlugRelatedField(queryset=SeasonModel.objects.all(), slug_field="name")

    class Meta:
        model = TeacherModel
        fields = "__all__"

class AccountantSerializer(serializers.ModelSerializer):
    account = serializers.SlugRelatedField(queryset=Account.objects.all(), slug_field="email")
    branch = serializers.SlugRelatedField(queryset=BranchModel.objects.all(), slug_field="name")

    class Meta:
        model = AccountantModel
        fields = "__all__"

class AbiturientBlockSerializer(serializers.ModelSerializer):
    class Meta:
        model = AbiturientBlockModel
        fields = "__all__"

class AbiturientClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = AbiturientClassModel
        fields = "__all__"

class AbiturientSubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = AbiturientSubjectModel
        fields = "__all__"

class AbiturientGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = AbiturientGroupModel
        fields = "__all__"

class AbiturientSerializer(serializers.ModelSerializer):
    student = StudentSerializer()
    blocks = AbiturientBlockSerializer(many=True)
    abiturient_class = serializers.SlugRelatedField(queryset=AbiturientClassModel.objects.all(), slug_field="name")
    subjects = AbiturientSubjectSerializer(many=True)
    group = serializers.SlugRelatedField(queryset=AbiturientGroupModel.objects.all(), slug_field="name")

    class Meta:
        model = AbiturientModel
        fields = "__all__"

class MasterForeignLanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = MasterForeignLanguageModel
        fields = "__all__"

class MasterSubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = MasterSubjectModel
        fields = "__all__"

class MasterGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = MasterGroupModel
        fields = "__all__"

class MasterSerializer(serializers.ModelSerializer):
    student = StudentSerializer()
    language = serializers.SlugRelatedField(queryset=MasterForeignLanguageModel.objects.all(), slug_field="name")
    subjects = MasterSubjectSerializer(many=True)
    group = serializers.SlugRelatedField(queryset=MasterGroupModel.objects.all(), slug_field="name")

    class Meta:
        model = MasterModel
        fields = "__all__"

class MIQSubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = MIQSubjectModel
        fields = "__all__"

class MIQSerializer(serializers.ModelSerializer):
    student = StudentSerializer()
    subjects = MIQSubjectSerializer(many=True)

    class Meta:
        model = MIQModel
        fields = "__all__"

class CivilServiceSubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = CivilServiceSubjectModel
        fields = "__all__"

class CivilServiceSerializer(serializers.ModelSerializer):
    student = StudentSerializer()
    subjects = CivilServiceSubjectSerializer(many=True)

    class Meta:
        model = CivilServiceModel
        fields = "__all__"

class ForeignLanguageSerializer(serializers.ModelSerializer):
    student = StudentSerializer()
    
    class Meta:
        model = ForeignLanguageModel
        fields = "__all__"

class ComputerProgramTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ComputerProgramTypeModel
        fields = "__all__"

class ComputerCourseSerializer(serializers.ModelSerializer):
    student = StudentSerializer()
    program_types = ComputerProgramTypeSerializer(many=True)

    class Meta:
        model = ComputerCourseModel
        fields = "__all__"

class AccountingSerializer(serializers.ModelSerializer):
    student = StudentSerializer()

    class Meta:
        model = AccountingModel
        fields = "__all__"

class HighSchoolClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = HighSchoolClassModel
        fields = "__all__"

class HighSchoolSubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = HighSchoolSubjectModel
        fields = "__all__"

class HighSchoolGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = HighSchoolGroupModel
        fields = "__all__"

class HighSchoolSerializer(serializers.ModelSerializer):
    student = StudentSerializer()
    highschool_class = serializers.SlugRelatedField(queryset=HighSchoolClassModel.objects.all(), slug_field="name")
    subjects = HighSchoolSubjectSerializer(many=True)
    group = serializers.SlugRelatedField(queryset=HighSchoolGroupModel.objects.all(), slug_field="name")

    class Meta:
        model = HighSchoolModel
        fields = "__all__"

class PreSchoolSubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = PreSchoolSubjectModel
        fields = "__all__"

class PreSchoolSerializer(serializers.ModelSerializer):
    student = StudentSerializer()
    subjects = PreSchoolSubjectSerializer(many=True)

    class Meta:
        model = PreSchoolModel
        fields = "__all__"

class PrimarySchoolClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrimarySchoolClassModel
        fields = "__all__"

class PrimarySchoolSubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrimarySchoolSubjectModel
        fields = "__all__"

class PrimarySchoolGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrimarySchoolGroupModel
        fields = "__all__"

class PrimarySchoolSerializer(serializers.ModelSerializer):
    student = StudentSerializer()
    primaryschool_class = serializers.SlugRelatedField(queryset=PrimarySchoolClassModel.objects.all(), slug_field="name")
    subjects = PrimarySchoolSubjectSerializer(many=True)
    group = serializers.SlugRelatedField(queryset=PrimarySchoolGroupModel.objects.all(), slug_field="name")

    class Meta:
        model = PrimarySchoolModel
        fields = "__all__"

