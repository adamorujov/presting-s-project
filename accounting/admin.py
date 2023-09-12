from typing import Any
from django.contrib import admin
from django.db.models.query import QuerySet
from django.http.request import HttpRequest
from accounting.models import (
    MonthModel, TeacherPaymentInformationModel, AbiturientPaymentInformationModel, MasterPaymentInformationModel,
    MIQPaymentInformationModel, CivilServicePaymentInformationModel, ForeignLanguagePaymentInformationModel,
    ComputerCoursePaymentInformationModel, AccountingPaymentInformationModel,
    HighSchoolPaymentInformationModel, PreSchoolPaymentInformationModel,
    PrimarySchoolPaymentInformationModel
)
from django.contrib import messages

@admin.register(MonthModel)
class MonthAdmin(admin.ModelAdmin):
    list_display = ("__str__", "season")

@admin.register(TeacherPaymentInformationModel)
class TeacherPaymentInformationAdmin(admin.ModelAdmin):
    list_display = ("teacher", "month", "payment_date", "payment_amount", "status")
    list_filter = ("status", "payment_date")
    search_fields = ("teacher__first_name", "teacher__last_name")

    actions = ("mark_as_true", "mark_as_false")

    @admin.action(description="Seçilmiş Müəllimlər ödəniş aldı.")
    def mark_as_true(self, request, queryset):
        updated = queryset.update(status=True)
        self.message_user(request, "Seçilmiş Müəllimlər ödəniş aldı.", messages.SUCCESS)

    @admin.action(description="Seçilmiş Müəllimlər ödəniş almayıb.")
    def mark_as_false(self, request, queryset):
        updated = queryset.update(status=False)
        self.message_user(request, "Seçilmiş Müəllimlər ödəniş almayıb.", messages.SUCCESS)


@admin.register(AbiturientPaymentInformationModel)
class AbiturientPaymentInformationAdmin(admin.ModelAdmin):
    list_display = ("abiturient", "month", "payment_date", "payment_amount", "status")
    list_filter = ("status", "payment_date")
    search_fields = ("abiturient__student__first_name", "abiturient__student__last_name")

    actions = ("mark_as_true", "mark_as_false")

    @admin.action(description="Seçilmiş Abituriyentlər ödəniş etdi.")
    def mark_as_true(self, request, queryset):
        updated = queryset.update(status=True)
        self.message_user(request, "Seçilmiş Abituriyentlər ödəniş etdi.", messages.SUCCESS)

    @admin.action(description="Seçilmiş Abituriyentlər ödəniş etməyib.")
    def mark_as_false(self, request, queryset):
        updated = queryset.update(status=False)
        self.message_user(request, "Seçilmiş Abituriyentlər ödəniş etməyib.", messages.SUCCESS)

@admin.register(MasterPaymentInformationModel)
class MasterPaymentInformationAdmin(admin.ModelAdmin):
    list_display = ("master", "month", "payment_date", "payment_amount", "status")
    list_filter = ("status", "payment_date")
    search_fields = ("master__student__first_name", "master__student__last_name")

    actions = ("mark_as_true", "mark_as_false")

    @admin.action(description="Seçilmiş Magistrantlar ödəniş etdi.")
    def mark_as_true(self, request, queryset):
        updated = queryset.update(status=True)
        self.message_user(request, "Seçilmiş Magistrantlar ödəniş etdi.", messages.SUCCESS)

    @admin.action(description="Seçilmiş Magistrantlar ödəniş etməyib.")
    def mark_as_false(self, request, queryset):
        updated = queryset.update(status=False)
        self.message_user(request, "Seçilmiş Magistrantlar ödəniş etməyib.", messages.SUCCESS)

@admin.register(MIQPaymentInformationModel)
class MIQPaymentInformationAdmin(admin.ModelAdmin):
    list_display = ("miq", "month", "payment_date", "payment_amount", "status")
    list_filter = ("status", "payment_date")
    search_fields = ("miq__student__first_name", "miq__student__last_name")

    actions = ("mark_as_true", "mark_as_false")

    @admin.action(description="Seçilmiş MİQlər ödəniş etdi.")
    def mark_as_true(self, request, queryset):
        updated = queryset.update(status=True)
        self.message_user(request, "Seçilmiş MİQlər ödəniş etdi.", messages.SUCCESS)

    @admin.action(description="Seçilmiş MİQlər ödəniş etməyib.")
    def mark_as_false(self, request, queryset):
        updated = queryset.update(status=False)
        self.message_user(request, "Seçilmiş MİQlər ödəniş etməyib.", messages.SUCCESS)

@admin.register(CivilServicePaymentInformationModel)
class CivilServicePaymentInformationAdmin(admin.ModelAdmin):
    list_display = ("civilservice", "month", "payment_date", "payment_amount", "status")
    list_filter = ("status", "payment_date")
    search_fields = ("civilservice__student__first_name", "civilservice__student__last_name")

    actions = ("mark_as_true", "mark_as_false")

    @admin.action(description="Seçilmiş Dövlət qulluqları ödəniş etdi.")
    def mark_as_true(self, request, queryset):
        updated = queryset.update(status=True)
        self.message_user(request, "Seçilmiş Dövlət qulluqları ödəniş etdi.", messages.SUCCESS)

    @admin.action(description="Seçilmiş Dövlət qulluqları ödəniş etməyib.")
    def mark_as_false(self, request, queryset):
        updated = queryset.update(status=False)
        self.message_user(request, "Seçilmiş Dövlət qulluqları ödəniş etməyib.", messages.SUCCESS)
    
@admin.register(ForeignLanguagePaymentInformationModel)
class ForeignLanguagePaymentInformationAdmin(admin.ModelAdmin):
    list_display = ("foreignlanguage", "month", "payment_date", "payment_amount", "status")
    list_filter = ("status", "payment_date")
    search_fields = ("foreignlanguage__student__first_name", "foreignlanguage__student__last_name")

    actions = ("mark_as_true", "mark_as_false")

    @admin.action(description="Seçilmiş Xarici dillər ödəniş etdi.")
    def mark_as_true(self, request, queryset):
        updated = queryset.update(status=True)
        self.message_user(request, "Seçilmiş Xarici dillər ödəniş etdi.", messages.SUCCESS)

    @admin.action(description="Seçilmiş Xarici dillər ödəniş etməyib.")
    def mark_as_false(self, request, queryset):
        updated = queryset.update(status=False)
        self.message_user(request, "Seçilmiş Xarici dillər ödəniş etməyib.", messages.SUCCESS)

@admin.register(ComputerCoursePaymentInformationModel)
class ComputerCoursePaymentInformationAdmin(admin.ModelAdmin):
    list_display = ("computercourse", "month", "payment_date", "payment_amount", "status")
    list_filter = ("status", "payment_date")
    search_fields = ("computercourse__student__first_name", "computercourse__student__last_name")

    actions = ("mark_as_true", "mark_as_false")

    @admin.action(description="Seçilmiş Kompüter kursları ödəniş etdi.")
    def mark_as_true(self, request, queryset):
        updated = queryset.update(status=True)
        self.message_user(request, "Seçilmiş Kompüter kursları ödəniş etdi.", messages.SUCCESS)

    @admin.action(description="Seçilmiş Kompüter kursları ödəniş etməyib.")
    def mark_as_false(self, request, queryset):
        updated = queryset.update(status=False)
        self.message_user(request, "Seçilmiş Kompüter kursları ödəniş etməyib.", messages.SUCCESS)

@admin.register(AccountingPaymentInformationModel)
class AccountingPaymentInformationAdmin(admin.ModelAdmin):
    list_display = ("accounting", "month", "payment_date", "payment_amount", "status")
    list_filter = ("status", "payment_date")
    search_fields = ("accounting__student__first_name", "accounting__student__last_name")

    actions = ("mark_as_true", "mark_as_false")

    @admin.action(description="Seçilmiş Mühasibatlıqlar ödəniş etdi.")
    def mark_as_true(self, request, queryset):
        updated = queryset.update(status=True)
        self.message_user(request, "Seçilmiş Mühasibatlıqlar ödəniş etdi.", messages.SUCCESS)

    @admin.action(description="Seçilmiş Mühasibatlıqlar ödəniş etməyib.")
    def mark_as_false(self, request, queryset):
        updated = queryset.update(status=False)
        self.message_user(request, "Seçilmiş Mühasibatlıqlar ödəniş etməyib.", messages.SUCCESS)


@admin.register(HighSchoolPaymentInformationModel)
class HighSchoolPaymentInformationAdmin(admin.ModelAdmin):
    list_display = ("highschool", "month", "payment_date", "payment_amount", "status")
    list_filter = ("status", "payment_date")
    search_fields = ("highschool__student__first_name", "highschool__student__last_name")

    actions = ("mark_as_true", "mark_as_false")

    @admin.action(description="Seçilmiş Liseylərə hazırlıqlar ödəniş etdi.")
    def mark_as_true(self, request, queryset):
        updated = queryset.update(status=True)
        self.message_user(request, "Seçilmiş Liseylərə hazırlıqlar ödəniş etdi.", messages.SUCCESS)

    @admin.action(description="Seçilmiş Liseylərə hazırlıqlar ödəniş etməyib.")
    def mark_as_false(self, request, queryset):
        updated = queryset.update(status=False)
        self.message_user(request, "Seçilmiş Liseylərə hazırlıqlar ödəniş etməyib.", messages.SUCCESS)

@admin.register(PreSchoolPaymentInformationModel)
class PreSchoolPaymentInformationAdmin(admin.ModelAdmin):
    list_display = ("preschool", "month", "payment_date", "payment_amount", "status")
    list_filter = ("status", "payment_date")
    search_fields = ("preschool__student__first_name", "preschool__student__last_name")

    actions = ("mark_as_true", "mark_as_false")

    @admin.action(description="Seçilmiş Məktəbəqədər hazırlıqlar ödəniş etdi.")
    def mark_as_true(self, request, queryset):
        updated = queryset.update(status=True)
        self.message_user(request, "Seçilmiş Məktəbəqədər hazırlıqlar ödəniş etdi.", messages.SUCCESS)

    @admin.action(description="Seçilmiş Məktəbəqədər hazırlıqlar ödəniş etməyib.")
    def mark_as_false(self, request, queryset):
        updated = queryset.update(status=False)
        self.message_user(request, "Seçilmiş Məktəbəqədər hazırlıqlar ödəniş etməyib.", messages.SUCCESS)

@admin.register(PrimarySchoolPaymentInformationModel)
class PrimarySchoolPaymentInformationAdmin(admin.ModelAdmin):
    list_display = ("primaryschool", "month", "payment_date", "payment_amount", "status")
    list_filter = ("status", "payment_date")
    search_fields = ("primaryschool__student__first_name", "highschool__student__last_name")

    actions = ("mark_as_true", "mark_as_false")

    @admin.action(description="Seçilmiş İbtidailər ödəniş etdi.")
    def mark_as_true(self, request, queryset):
        updated = queryset.update(status=True)
        self.message_user(request, "Seçilmiş İbtidailər ödəniş etdi.", messages.SUCCESS)

    @admin.action(description="Seçilmiş İbtidailər ödəniş etməyib.")
    def mark_as_false(self, request, queryset):
        updated = queryset.update(status=False)
        self.message_user(request, "Seçilmiş İbtidailər ödəniş etməyib.", messages.SUCCESS)
