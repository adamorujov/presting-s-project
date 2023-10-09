from rest_framework import serializers
from accounting.models import (
    MonthModel, TeacherPaymentInformationModel, StudentPaymentInformationModel, AbiturientPaymentInformationModel, MasterPaymentInformationModel,
    MIQPaymentInformationModel, CivilServicePaymentInformationModel, ForeignLanguagePaymentInformationModel,
    ComputerCoursePaymentInformationModel, AccountingPaymentInformationModel,
    HighSchoolPaymentInformationModel, PreSchoolPaymentInformationModel,
    PrimarySchoolPaymentInformationModel
)
from service.api.serializers import (
    SeasonSerializer, TeacherSerializer, StudentSerializer, AbiturientSerializer, MasterSerializer, MIQSerializer,
    ForeignLanguageSerializer, CivilServiceSerializer, ComputerCourseSerializer,
    AccountingSerializer, HighSchoolSerializer, PreSchoolSerializer,
    PrimarySchoolSerializer
)

class MonthSerializer(serializers.ModelSerializer):
    season = SeasonSerializer()

    class Meta:
        model = MonthModel
        fields = "__all__"

class TeacherPaymentInformationSerializer(serializers.ModelSerializer):
    teacher = TeacherSerializer()
    month = MonthSerializer()

    class Meta:
        model = TeacherPaymentInformationModel
        fields = "__all__"

class StudentPaymentInformationSerializer(serializers.ModelSerializer):
    student = StudentSerializer()
    month = MonthSerializer()

    class Meta:
        model = StudentPaymentInformationModel
        fields = "__all__"

class AbiturientPaymentInformationSerializer(serializers.ModelSerializer):
    abiturient = AbiturientSerializer()
    month = MonthSerializer()

    class Meta:
        model = AbiturientPaymentInformationModel
        fields = "__all__"

class MasterPaymentInformationSerializer(serializers.ModelSerializer):
    master = MasterSerializer()
    month = MonthSerializer()
    
    class Meta:
        model = MasterPaymentInformationModel
        fields = "__all__"

class MIQPaymentInformationSerializer(serializers.ModelSerializer):
    miq = MIQSerializer()
    month = MonthSerializer()
    
    class Meta:
        model = MIQPaymentInformationModel
        fields = "__all__"

class ForeignLanguagePaymentInformationSerializer(serializers.ModelSerializer):
    foreignlanguage = ForeignLanguageSerializer()
    month = MonthSerializer()
    
    class Meta:
        model = ForeignLanguagePaymentInformationModel
        fields = "__all__"

class CivilServicePaymentInformationSerializer(serializers.ModelSerializer):
    civilservice = CivilServiceSerializer()
    month = MonthSerializer()
    
    class Meta:
        model = CivilServicePaymentInformationModel
        fields = "__all__"

class ComputerCoursePaymentInformationSerializer(serializers.ModelSerializer):
    computercourse = ComputerCourseSerializer()
    month = MonthSerializer()
    
    class Meta:
        model = ComputerCoursePaymentInformationModel
        fields = "__all__"

class AccountingPaymentInformationSerializer(serializers.ModelSerializer):
    accounting = AccountingSerializer()
    month = MonthSerializer()
    
    class Meta:
        model = AccountingPaymentInformationModel
        fields = "__all__"

class HighSchoolPaymentInformationSerializer(serializers.ModelSerializer):
    highschool = HighSchoolSerializer()
    month = MonthSerializer()
    
    class Meta:
        model = HighSchoolPaymentInformationModel
        fields = "__all__"

class PreSchoolPaymentInformationSerializer(serializers.ModelSerializer):
    preschool = PreSchoolSerializer()
    month = MonthSerializer()
    
    class Meta:
        model = PreSchoolPaymentInformationModel
        fields = "__all__"

class PrimarySchoolPaymentInformationSerializer(serializers.ModelSerializer):
    primaryschool = PrimarySchoolSerializer()
    month = MonthSerializer()
    
    class Meta:
        model = PrimarySchoolPaymentInformationModel
        fields = "__all__"












