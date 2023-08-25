from django.contrib import admin
from accounting.models import (
    MonthModel, AbiturientPaymentInformationModel, MasterPaymentInformationModel,
    MIQPaymentInformationModel, CivilServicePaymentInformationModel, ForeignLanguagePaymentInformationModel,
    ComputerCoursePaymentInformationModel, AccountingPaymentInformationModel,
    HighSchoolPaymentInformationModel, PreSchoolPaymentInformationModel,
    PrimarySchoolPaymentInformationModel
)

admin.site.register(MonthModel)
admin.site.register(AbiturientPaymentInformationModel)
admin.site.register(MasterPaymentInformationModel)
admin.site.register(MIQPaymentInformationModel)
admin.site.register(CivilServicePaymentInformationModel)
admin.site.register(ForeignLanguagePaymentInformationModel)
admin.site.register(ComputerCoursePaymentInformationModel)
admin.site.register(AccountingPaymentInformationModel)
admin.site.register(HighSchoolPaymentInformationModel)
admin.site.register(PreSchoolPaymentInformationModel)
admin.site.register(PrimarySchoolPaymentInformationModel)