from django.db import models
from service.models import (
    SeasonModel, AbiturientModel, MasterModel, MIQModel,
    CivilServiceModel, ForeignLanguageModel, ComputerCourseModel,
    AccountingModel, HighSchoolModel, PreSchoolModel, PrimarySchoolModel
)

class MonthModel(models.Model):
    name = models.CharField("Ad", max_length=100)
    season = models.ForeignKey(SeasonModel, verbose_name="Sezon", on_delete=models.CASCADE, related_name="months")

    class Meta:
        verbose_name = "Ay"
        verbose_name_plural = "Aylar"

    def __str__(self):
        return self.name
    
class AbiturientPaymentInformationModel(models.Model):
    abiturient = models.ForeignKey(AbiturientModel, verbose_name="Abituriyent", on_delete=models.CASCADE, related_name="abiturient_payments")
    month = models.ForeignKey(MonthModel, verbose_name="Ay", on_delete=models.CASCADE, related_name="a_month_payments")
    payment_date = models.DateField("Ödənişin tarixi", blank=True, null=True)
    payment_amount = models.FloatField("Ödəniş məbləği", default=0)
    status = models.BooleanField("Status", default=False)

    class Meta:
        verbose_name = "Abituriyent ödəniş məlumatı"
        verbose_name_plural = "Abituriyent ödəniş məlumatları"

    def save(self, *args, **kwargs):
        if AbiturientPaymentInformationModel.objects.filter(
            abiturient = self.abiturient,
            month = self.month
        ).exists():
            pass
        else:
            return super(AbiturientPaymentInformationModel, self).save(*args, **kwargs)

    def __str__(self):
        return self.abiturient.student.first_name + " " + self.abiturient.student.last_name + " | " + self.month.name
    
class MasterPaymentInformationModel(models.Model):
    master = models.ForeignKey(MasterModel, verbose_name="Magistrant", on_delete=models.CASCADE, related_name="master_payments")
    month = models.ForeignKey(MonthModel, verbose_name="Ay", on_delete=models.CASCADE, related_name="m_month_payments")
    payment_date = models.DateField("Ödənişin tarixi", blank=True, null=True)
    payment_amount = models.FloatField("Ödəniş məbləği", default=0)
    status = models.BooleanField("Status", default=False)

    class Meta:
        verbose_name = "Magistrant ödəniş məlumatı"
        verbose_name_plural = "Magistrant ödəniş məlumatları"

    def save(self, *args, **kwargs):
        if MasterPaymentInformationModel.objects.filter(
            master = self.master,
            month = self.month
        ).exists():
            pass
        else:
            return super(MasterPaymentInformationModel, self).save(*args, **kwargs)

    def __str__(self):
        return self.master.student.first_name + " " + self.master.last_name + " | " + self.month.name
    
class MIQPaymentInformationModel(models.Model):
    miq = models.ForeignKey(MIQModel, verbose_name="MİQ", on_delete=models.CASCADE, related_name="miq_payments")
    month = models.ForeignKey(MonthModel, verbose_name="Ay", on_delete=models.CASCADE, related_name="mi_month_payments")
    payment_date = models.DateField("Ödənişin tarixi", blank=True, null=True)
    payment_amount = models.FloatField("Ödəniş məbləği", default=0)
    status = models.BooleanField("Status", default=False)

    class Meta:
        verbose_name = "MİQ ödəniş məlumatı"
        verbose_name_plural = "MİQ ödəniş məlumatları"

    def save(self, *args, **kwargs):
        if MIQPaymentInformationModel.objects.filter(
            miq = self.miq,
            month = self.month
        ).exists():
            pass
        else:
            return super(MIQPaymentInformationModel, self).save(*args, **kwargs)

    def __str__(self):
        return self.miq.student.first_name + " " + self.miq.last_name + " | " + self.month.name
    
class CivilServicePaymentInformationModel(models.Model):
    civilservice = models.ForeignKey(CivilServiceModel, verbose_name="Dövləq qulluğu", on_delete=models.CASCADE, related_name="civilservice_payments")
    month = models.ForeignKey(MonthModel, verbose_name="Ay", on_delete=models.CASCADE, related_name="cs_month_payments")
    payment_date = models.DateField("Ödənişin tarixi", blank=True, null=True)
    payment_amount = models.FloatField("Ödəniş məbləği", default=0)
    status = models.BooleanField("Status", default=False)

    class Meta:
        verbose_name = "Dövlət qulluğu ödəniş məlumatı"
        verbose_name_plural = "Dövlət qulluğu ödəniş məlumatları"

    def save(self, *args, **kwargs):
        if CivilServicePaymentInformationModel.objects.filter(
            civilservice = self.civilservice,
            month = self.month
        ).exists():
            pass
        else:
            return super(CivilServicePaymentInformationModel, self).save(*args, **kwargs)

    def __str__(self):
        return self.civilservice.student.first_name + " " + self.civilservice.last_name + " | " + self.month.name
    
class ForeignLanguagePaymentInformationModel(models.Model):
    foreignlanguage = models.ForeignKey(ForeignLanguageModel, verbose_name="Xarici dil", on_delete=models.CASCADE, related_name="foreignlanguage_payments")
    month = models.ForeignKey(MonthModel, verbose_name="Ay", on_delete=models.CASCADE, related_name="fl_month_payments")
    payment_date = models.DateField("Ödənişin tarixi", blank=True, null=True)
    payment_amount = models.FloatField("Ödəniş məbləği", default=0)
    status = models.BooleanField("Status", default=False)

    class Meta:
        verbose_name = "Xarici dil ödəniş məlumatı"
        verbose_name_plural = "Xarici dil ödəniş məlumatları"

    def save(self, *args, **kwargs):
        if ForeignLanguagePaymentInformationModel.objects.filter(
            foreignlanguage = self.foreignlanguage,
            month = self.month
        ).exists():
            pass
        else:
            return super(ForeignLanguagePaymentInformationModel, self).save(*args, **kwargs)

    def __str__(self):
        return self.foreignlanguage.student.first_name + " " + self.foreignlanguage.student.last_name + " | " + self.month.name
    
class ComputerCoursePaymentInformationModel(models.Model):
    computercourse = models.ForeignKey(ComputerCourseModel, verbose_name="Komputer kursu", on_delete=models.CASCADE, related_name="computercourse_payments")
    month = models.ForeignKey(MonthModel, verbose_name="Ay", on_delete=models.CASCADE, related_name="cc_month_payments")
    payment_date = models.DateField("Ödənişin tarixi", blank=True, null=True)
    payment_amount = models.FloatField("Ödəniş məbləği", default=0)
    status = models.BooleanField("Status", default=False)

    class Meta:
        verbose_name = "Komputer kursu ödəniş məlumatı"
        verbose_name_plural = "Komputer kursu ödəniş məlumatları"

    def save(self, *args, **kwargs):
        if ComputerCoursePaymentInformationModel.objects.filter(
            computercourse = self.computercourse,
            month = self.month
        ).exists():
            pass
        else:
            return super(ComputerCoursePaymentInformationModel, self).save(*args, **kwargs)

    def __str__(self):
        return self.computercourse.student.first_name + " " + self.computercourse.student.last_name + " | " + self.month.name
    
class AccountingPaymentInformationModel(models.Model):
    accounting = models.ForeignKey(AccountingModel, verbose_name="Mühasibatlıq", on_delete=models.CASCADE, related_name="accounting_payments")
    month = models.ForeignKey(MonthModel, verbose_name="Ay", on_delete=models.CASCADE, related_name="ac_month_payments")
    payment_date = models.DateField("Ödənişin tarixi", blank=True, null=True)
    payment_amount = models.FloatField("Ödəniş məbləği", default=0)
    status = models.BooleanField("Status", default=False)

    class Meta:
        verbose_name = "Mühasibatlıq ödəniş məlumatı"
        verbose_name_plural = "Mühasibatlıq ödəniş məlumatları"

    def save(self, *args, **kwargs):
        if AccountingPaymentInformationModel.objects.filter(
            accounting = self.accounting,
            month = self.month
        ).exists():
            pass
        else:
            return super(AccountingPaymentInformationModel, self).save(*args, **kwargs)

    def __str__(self):
        return self.accounting.student.first_name + " " + self.accounting.student.last_name + " | " + self.month.name
 
class HighSchoolPaymentInformationModel(models.Model):
    highschool = models.ForeignKey(HighSchoolModel, verbose_name="Liseylərə hazırlıq", on_delete=models.CASCADE, related_name="highschool_payments")
    month = models.ForeignKey(MonthModel, verbose_name="Ay", on_delete=models.CASCADE, related_name="hs_month_payments")
    payment_date = models.DateField("Ödənişin tarixi", blank=True, null=True)
    payment_amount = models.FloatField("Ödəniş məbləği", default=0)
    status = models.BooleanField("Status", default=False)

    class Meta:
        verbose_name = "Liseylərə hazırlıq ödəniş məlumatı"
        verbose_name_plural = "Liseylərə hazırlıq ödəniş məlumatları"

    def save(self, *args, **kwargs):
        if HighSchoolPaymentInformationModel.objects.filter(
            highschool = self.highschool,
            month = self.month
        ).exists():
            pass
        else:
            return super(HighSchoolPaymentInformationModel, self).save(*args, **kwargs)

    def __str__(self):
        return self.highschool.student.first_name + " " + self.highschool.student.last_name + " | " + self.month.name
    
class PreSchoolPaymentInformationModel(models.Model):
    preschool = models.ForeignKey(PreSchoolModel, verbose_name="Məktəbəqədər hazırlıq", on_delete=models.CASCADE, related_name="preschool_payments")
    month = models.ForeignKey(MonthModel, verbose_name="Ay", on_delete=models.CASCADE, related_name="ps_month_payments")
    payment_date = models.DateField("Ödənişin tarixi", blank=True, null=True)
    payment_amount = models.FloatField("Ödəniş məbləği", default=0)
    status = models.BooleanField("Status", default=False)

    class Meta:
        verbose_name = "Məktəbəqədər hazırlıq ödəniş məlumatı"
        verbose_name_plural = "Məktəbəqədər hazırlıq ödəniş məlumatları"

    def save(self, *args, **kwargs):
        if PreSchoolPaymentInformationModel.objects.filter(
            preschool = self.preschool,
            month = self.month
        ).exists():
            pass
        else:
            return super(PreSchoolPaymentInformationModel, self).save(*args, **kwargs)

    def __str__(self):
        return self.preschool.student.first_name + " " + self.preschool.student.last_name + " | " + self.month.name
    
class PrimarySchoolPaymentInformationModel(models.Model):
    primaryschool = models.ForeignKey(PrimarySchoolModel, verbose_name="İbtidai", on_delete=models.CASCADE, related_name="primary_payments")
    month = models.ForeignKey(MonthModel, verbose_name="Ay", on_delete=models.CASCADE, related_name="prs_month_payments")
    payment_date = models.DateField("Ödənişin tarixi", blank=True, null=True)
    payment_amount = models.FloatField("Ödəniş məbləği", default=0)
    status = models.BooleanField("Status", default=False)

    class Meta:
        verbose_name = "İbtidai ödəniş məlumatı"
        verbose_name_plural = "İbtidai ödəniş məlumatları"

    def save(self, *args, **kwargs):
        if PrimarySchoolPaymentInformationModel.objects.filter(
            primaryschool = self.primaryschool,
            month = self.month
        ).exists():
            pass
        else:
            return super(PrimarySchoolPaymentInformationModel, self).save(*args, **kwargs)

    def __str__(self):
        return self.primaryschool.student.first_name + " " + self.primaryschool.student.last_name + " | " + self.month.name
  
  
  
  