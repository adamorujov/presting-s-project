from django.contrib import admin
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

admin.site.register(BranchModel)
admin.site.register(SeasonModel)
admin.site.register(StudentModel)
admin.site.register(TeacherModel)
admin.site.register(AccountantModel)
admin.site.register(AbiturientBlockModel)
admin.site.register(AbiturientClassModel)
admin.site.register(AbiturientSubjectModel)
admin.site.register(AbiturientGroupModel)
admin.site.register(AbiturientModel)
admin.site.register(MasterForeignLanguageModel)
admin.site.register(MasterSubjectModel)
admin.site.register(MasterGroupModel)
admin.site.register(MasterModel)
admin.site.register(MIQSubjectModel)
admin.site.register(MIQModel)
admin.site.register(CivilServiceSubjectModel)
admin.site.register(CivilServiceModel)
admin.site.register(ForeignLanguageModel)
admin.site.register(ComputerProgramTypeModel)
admin.site.register(ComputerCourseModel)
admin.site.register(AccountingModel)
admin.site.register(HighSchoolClassModel)
admin.site.register(HighSchoolSubjectModel)
admin.site.register(HighSchoolGroupModel)
admin.site.register(HighSchoolModel)
admin.site.register(PreSchoolSubjectModel)
admin.site.register(PreSchoolModel)
admin.site.register(PrimarySchoolClassModel)
admin.site.register(PrimarySchoolSubjectModel)
admin.site.register(PrimarySchoolGroupModel)
admin.site.register(PrimarySchoolModel)
