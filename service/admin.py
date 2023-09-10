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
from accounting.models import (
    TeacherPaymentInformationModel, AbiturientPaymentInformationModel, MasterPaymentInformationModel,
    MIQPaymentInformationModel, CivilServicePaymentInformationModel, ForeignLanguagePaymentInformationModel,
    ComputerCoursePaymentInformationModel, AccountingPaymentInformationModel, HighSchoolPaymentInformationModel,
    PreSchoolPaymentInformationModel, PrimarySchoolPaymentInformationModel
)
from django.contrib import messages

admin.site.register(BranchModel)

@admin.register(SeasonModel)
class SeasonAdmin(admin.ModelAdmin):
    list_display = ("__str__", "branch", "start_date", "end_date")

@admin.register(StudentModel)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("__str__", "season", "status")
    list_filter = ("status",)
    search_fields = ("first_name", "last_name")

    actions = ("mark_as_de", "mark_as_d", "mark_as_b")

    @admin.action(description="Seçilmiş Tələbələri davam edir kimi göstər")
    def mark_as_de(self, request, queryset):
        updated = queryset.update(status="DE")
        self.message_user(request, "Seçilmiş Tələbələr davam edir.", messages.SUCCESS)

    @admin.action(description="Seçilmiş Tələbələri dondurulub kimi göstər")
    def mark_as_d(self, request, queryset):
        updated = queryset.update(status="D")
        self.message_user(request, "Seçilmiş Tələbələr dondurulub.", messages.SUCCESS)

    @admin.action(description="Seçilmiş Tələbələri bitirilib kimi göstər")
    def mark_as_b(self, request, queryset):
        updated = queryset.update(status="B")
        self.message_user(request, "Seçilmiş Tələbələr bitirilib.", messages.SUCCESS)

class TeacherPaymentInformationAdmin(admin.TabularInline):
    model = TeacherPaymentInformationModel
    extra = 3

@admin.register(TeacherModel)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ("__str__", "specialty", "section", "salary", "status")
    list_filter = ("status",)
    search_fields = ("first_name", "last_name")

    inlines = [TeacherPaymentInformationAdmin]
    actions = ("mark_as_qe", "mark_as_ts", "mark_as_fm")

    @admin.action(description="Seçilmiş Müəllimləri qeyd edilməyib kimi göstər")
    def mark_as_qe(self, request, queryset):
        updated = queryset.update(status="QE")
        self.message_user(request, "Seçilmiş Müəllimlər qeyd edilməyib.", messages.SUCCESS)

    @admin.action(description="Seçilmiş Müəllimləri tələbə sayı kimi göstər")
    def mark_as_ts(self, request, queryset):
        updated = queryset.update(status="TS")
        self.message_user(request, "Seçilmiş Müəllimlər tələbə sayına görə maaş alır.", messages.SUCCESS)

    @admin.action(description="Seçilmiş Müəllimləri fiks maaş kimi göstər")
    def mark_as_fm(self, request, queryset):
        updated = queryset.update(status="FM")
        self.message_user(request, "Seçilmiş Müəllimlər fiks maaş alır.", messages.SUCCESS)


@admin.register(AccountantModel)
class AccountantAdmin(admin.ModelAdmin):
    list_display = ("__str__", "branch")

admin.site.register(AbiturientBlockModel)
admin.site.register(AbiturientClassModel)
admin.site.register(AbiturientSubjectModel)
admin.site.register(AbiturientGroupModel)

class AbiturientPaymentInformationAdmin(admin.TabularInline):
    model = AbiturientPaymentInformationModel
    extra = 3

@admin.register(AbiturientModel)
class AbiturientAdmin(admin.ModelAdmin):
    list_display = ("__str__", "sector", "dim_point")
    list_filter = ("sector", )

    inlines = [AbiturientPaymentInformationAdmin]
    actions = ("mark_as_az", "mark_as_ru")

    @admin.action(description="Seçilmiş Abituriyentlər azərbaycan dili bölməsi et")
    def mark_as_az(self, request, queryset):
        updated = queryset.update(sector="AZ")
        self.message_user(request, "Seçilmiş Abituriyentlər azərbaycan dili bölməsi edildi.", messages.SUCCESS)

    @admin.action(description="Seçilmiş Abituriyentlər rus dili bölməsi et")
    def mark_as_ru(self, request, queryset):
        updated = queryset.update(sector="RU")
        self.message_user(request, "Seçilmiş Abituriyentlər rus dili bölməsi edildi.", messages.SUCCESS)



admin.site.register(MasterForeignLanguageModel)
admin.site.register(MasterSubjectModel)
admin.site.register(MasterGroupModel)

class MasterPaymentInformationAdmin(admin.TabularInline):
    model = MasterPaymentInformationModel
    extra = 3

@admin.register(MasterModel)
class MasterAdmin(admin.ModelAdmin):
    list_display = ("__str__", "dim_point")
    inlines = [MasterPaymentInformationAdmin]

admin.site.register(MIQSubjectModel)

class MIQPaymentInformationAdmin(admin.TabularInline):
    model = MIQPaymentInformationModel
    extra = 3

@admin.register(MIQModel)
class MIQAdmin(admin.ModelAdmin):
    list_display = ("__str__", "specialty")
    inlines = [MIQPaymentInformationAdmin]

admin.site.register(CivilServiceSubjectModel)

class CivilServicePaymentInformationAdmin(admin.TabularInline):
    model = CivilServicePaymentInformationModel
    extra = 3


@admin.register(CivilServiceModel)
class CivilServiceAdmin(admin.ModelAdmin):
    inlines = [CivilServicePaymentInformationAdmin]

class ForeignLanguagePaymentInformationAdmin(admin.TabularInline):
    model = ForeignLanguagePaymentInformationModel
    extra = 3

@admin.register(ForeignLanguageModel)
class ForeignLanguageAdmin(admin.ModelAdmin):
    inlines = [ForeignLanguagePaymentInformationAdmin]


admin.site.register(ComputerProgramTypeModel)

class ComputerCoursePaymentInformationAdmin(admin.TabularInline):
    model = ComputerCoursePaymentInformationModel
    extra = 3

@admin.register(ComputerCourseModel)
class ComputerCourseAdmin(admin.ModelAdmin):
    inlines = [ComputerCoursePaymentInformationAdmin]

class AccountingPaymentInformationAdmin(admin.TabularInline):
    model = AccountingPaymentInformationModel
    extra = 3

@admin.register(AccountingModel)
class AccountingAdmin(admin.ModelAdmin):
    inlines = [AccountingPaymentInformationAdmin]


admin.site.register(HighSchoolClassModel)
admin.site.register(HighSchoolSubjectModel)
admin.site.register(HighSchoolGroupModel)

class HighSchoolPaymentInformationAdmin(admin.TabularInline):
    model = HighSchoolPaymentInformationModel
    extra = 3

@admin.register(HighSchoolModel)
class HighSchoolAdmin(admin.ModelAdmin):
    inlines = [HighSchoolPaymentInformationAdmin]

admin.site.register(PreSchoolSubjectModel)

class PreSchoolPaymentInformationAdmin(admin.TabularInline):
    model = PreSchoolPaymentInformationModel
    extra = 3

@admin.register(PreSchoolModel)
class PreSchoolAdmin(admin.ModelAdmin):
    inlines = [PreSchoolPaymentInformationAdmin]

admin.site.register(PrimarySchoolClassModel)
admin.site.register(PrimarySchoolSubjectModel)
admin.site.register(PrimarySchoolGroupModel)

class PrimarySchoolPaymentInformationAdmin(admin.TabularInline):
    model = PrimarySchoolPaymentInformationModel
    extra = 3

@admin.register(PrimarySchoolModel)
class PrimarySchoolAdmin(admin.ModelAdmin):
    inlines = [PrimarySchoolPaymentInformationAdmin]
