from typing import Any
from django.db import models
from account.models import Account
from django.apps import apps
import accounting
from datetime import date
from notification.models import NotificationModel

class BranchModel(models.Model):
    name = models.CharField("Filial", max_length=300)

    class Meta:
        verbose_name = "Filial"
        verbose_name_plural = "Filiallar"

    def __str__(self):
        return self.name
    
class SeasonModel(models.Model):
    name = models.CharField("Ad", max_length=150)
    start_date = models.DateField("Başlama tarixi", blank=True, null=True)
    end_date = models.DateField("Bitmə tarixi", blank=True, null=True)
    branch = models.ForeignKey(BranchModel, verbose_name="Filial", on_delete=models.CASCADE, related_name="seasons")

    class Meta:
        verbose_name = "Sezon"
        verbose_name_plural = "Sezonlar"

    def save(self, *args, **kwargs):
        if self.id:
            months = [
                "Sentyabr", "Oktyabr", "Noyabr", "Dekabr", "Yanvar",
                "Fevral", "Mart", "Aprel", "May", "Iyun",
                "Iyul", "Avqust"
                ]
            for month in months:
                accounting.models.MonthModel.objects.create(
                    name = month,
                    season = self
                )
            NotificationModel.objects.create(
                content = self.branch.name + " filialında bir sezona düzəliş edildi: " + self.name,
                type = "U"
            )
        else:
            NotificationModel.objects.create(
                content = self.branch.name + " filialına yeni sezon əlavə olundu: " + self.name,
                type = "A"
            )
        return super(SeasonModel, self).save(*args, **kwargs)
    
    def delete(self, *args, **kwargs):
        NotificationModel.objects.create(
            content = self.branch.name + " filialından bir sezon silindi: " + self.name,
            type = "D"
        )
        return super().delete(*args, **kwargs)

    def __str__(self):
        return self.name
    
class StudentModel(models.Model):
    STATUS = (
        ("DE", "Davam edir"),
        ("D", "Dondurulub"),
        ("B", "Bitirilib")
    )
    first_name = models.CharField("Ad", max_length=100)
    last_name = models.CharField("Soyad", max_length=100)
    phone_number1 = models.CharField("Telefon nömrəsi 1", max_length=50, blank=True, null=True)
    phone_number2 = models.CharField("Telefon nömrəsi 2", max_length=50, blank=True, null=True)
    wp_number = models.CharField("Whatsapp nömrəsi", max_length=50, blank=True, null=True)
    status = models.CharField("Status", max_length=2, choices=STATUS, default="DE")
    season = models.ForeignKey(SeasonModel, verbose_name="Sezon", on_delete=models.CASCADE, related_name="students")

    payment_date = models.DateField("Ödənişin tarixi", blank=True, null=True)
    payment_amount = models.FloatField("Ödəniş məbləği", default=0)

    class Meta:
        verbose_name = "Tələbə"
        verbose_name_plural = "Tələbələr"

    @property
    def get_full_name(self):
        return self.first_name + " " + self.last_name
    
    def save(self, *args, **kwargs):
        if self.id:
            NotificationModel.objects.create(
                content = self.season.branch.name + " filialında bir tələbənin məlumatları yeniləndi: " + self.get_full_name,
                type = "U"
            )
        else:
            NotificationModel.objects.create(
                content = self.season.branch.name + " filialına bir tələbə əlavə olundu: " + self.get_full_name,
                type = "A"
            )
        return super(StudentModel, self).save(*args, **kwargs)
    
    def delete(self, *args, **kwargs):
        NotificationModel.objects.create(
            content = self.season.branch.name + " filialından bir tələbə silindi: " + self.get_full_name,
            type = "D"
        )
        return super(StudentModel, self).delete(*args, **kwargs)

    def __str__(self):
        return self.first_name + " " + self.last_name
       
class TeacherModel(models.Model):
    STATUS = (
        ("QE", "Qeyd edilməyib"),
        ("TS", "Tələbə sayı"),
        ("FM", "Fiks maaş")
    )
    first_name = models.CharField("Ad", max_length=100)
    last_name = models.CharField("Soyad", max_length=100)
    specialty = models.CharField("İxtisas", max_length=300, blank=True, null=True)
    section = models.CharField("Bölmə", max_length=300, blank=True, null=True)
    salary = models.FloatField("Aylıq əmək haqqı", blank=True, null=True)
    phone_number1 = models.CharField("Telefon nömrəsi", max_length=50, blank=True, null=True)
    wp_number = models.CharField("Whatsapp nömrəsi", max_length=50, blank=True, null=True)
    status = models.CharField("Status", max_length=2, choices=STATUS, default="QE")
    season = models.ForeignKey(SeasonModel, verbose_name="Sezon", on_delete=models.CASCADE, related_name="teachers")

    payment_date = models.DateField("Ödənişin tarixi", blank=True, null=True)
    payment_amount = models.FloatField("Ödəniş məbləği", default=0)

    class Meta:
        verbose_name = "Müəllim"
        verbose_name_plural = "Müəllimlər"

    @property
    def get_full_name(self):
        return self.first_name + " " + self.last_name

    def save(self, *args, **kwargs):
        if self.id and self.payment_date:
            mon = 8
            year = self.payment_date.year 
            months = accounting.models.MonthModel.objects.filter(season=self.season)
            for month in months:
                day = self.payment_date.day
                mon = mon + 1
                if mon == 13:
                    mon = 1
                    year = year + 1
                elif mon in (4, 6, 9, 11) and day == 31:
                    day = 30
                elif mon == 2 and day > 28:
                    day = 28
                if not accounting.models.TeacherPaymentInformationModel.objects.filter(
                    teacher=self,
                    month=month
                ).exists():
                    accounting.models.TeacherPaymentInformationModel.objects.create(
                        teacher = self,
                        month = month,
                        payment_date = date(year, mon, day),
                        payment_amount = self.payment_amount
                    )
                else:
                    paymentinfo = accounting.models.TeacherPaymentInformationModel.objects.get(teacher=self, month=month)
                    paymentinfo.payment_date = date(year, mon, day)
                    paymentinfo.payment_amount = self.payment_amount
                    paymentinfo.save()

            # NotificationModel.objects.create(
            #     content = self.season.branch.name + " filialında bir müəllimin məlumatları yeniləndi: " + self.get_full_name,
            #     type = "U"
            # )
        # elif self.id:
        #     NotificationModel.objects.create(
        #         content = self.season.branch.name + " filialında bir müəllimin məlumatları yeniləndi: " + self.get_full_name,
        #         type = "U"
        #     )
        # else:
        #     NotificationModel.objects.create(
        #         content = self.season.branch.name + " filialına bir müəllim əlavə olundu: " + self.get_full_name,
        #         type = "A"
        #     )

        return super(TeacherModel, self).save(*args, **kwargs)
    
    def delete(self, *args, **kwargs):
        NotificationModel.objects.create(
            content = self.season.branch.name + " filialından bir müəllim silindi: " + self.get_full_name,
            type = "D"
        )
        return super(TeacherModel, self).delete(*args, **kwargs)

    def __str__(self):
        return self.first_name + " " + self.last_name
    
class AccountantModel(models.Model):
    account = models.OneToOneField(Account, on_delete=models.CASCADE, related_name="accountant")
    branch = models.ForeignKey(BranchModel, on_delete=models.CASCADE, related_name="branch_accountant")

    class Meta:
        verbose_name = "Mühasib"
        verbose_name_plural = "Mühasiblər"

    def save(self, *args, **kwargs):
        account = self.account
        account.is_accountant = True
        account.save()
        return super(AccountantModel, self).save(*args, **kwargs)

    def __str__(self):
        return self.account.first_name + " " + self.account.last_name

class AbiturientBlockModel(models.Model):
    name = models.CharField("Ad", max_length=100)

    class Meta:
        verbose_name = "Blok"
        verbose_name_plural = "Abituriyent blokları"

    def save(self, *args, **kwargs):
        if self.id:
            NotificationModel.objects.create(
                content = "Abituriyent bloku yeniləndi: " + self.name,
                type = "U"
            )
        else:
            NotificationModel.objects.create(
                content = "Abituriyent bloku əlavə olundu: " + self.name,
                type = "A"
            )
        return super(AbiturientBlockModel, self).save(*args, **kwargs)
    
    def delete(self, *args, **kwargs):
        NotificationModel.objects.create(
            content = "Bir Abituriyent bloku silindi: " + self.name,
            type = "D"
        )
        return super(AbiturientBlockModel, self).delete(*args, **kwargs)

    def __str__(self):
        return self.name
    
class AbiturientClassModel(models.Model):
    name = models.CharField("Ad", max_length=100)

    class Meta:
        verbose_name = "Sinif"
        verbose_name_plural = "Abituriyent sinifləri"

    def save(self, *args, **kwargs):
        if self.id:
            NotificationModel.objects.create(
                content = "Abituriyent sinifi yeniləndi: " + self.name,
                type = "U"
            )
        else:
            NotificationModel.objects.create(
                content = "Abituriyent sinifi əlavə olundu: " + self.name,
                type = "A"
            )
        return super(AbiturientClassModel, self).save(*args, **kwargs)
    
    def delete(self, *args, **kwargs):
        NotificationModel.objects.create(
            content = "Bir Abituriyent sinifi silindi: " + self.name,
            type = "D"
        )
        return super(AbiturientClassModel, self).delete(*args, **kwargs)


    def __str__(self):
        return self.name
    
class AbiturientSubjectModel(models.Model):
    name = models.CharField("Ad", max_length=300)

    class Meta:
        verbose_name = "Fənn"
        verbose_name_plural = "Abituriyent fənnləri"

    def save(self, *args, **kwargs):
        if self.id:
            NotificationModel.objects.create(
                content = "Abituriyent fənni yeniləndi: " + self.name,
                type = "U"
            )
        else:
            NotificationModel.objects.create(
                content = "Abituriyent fənni əlavə olundu: " + self.name,
                type = "A"
            )
        return super(AbiturientSubjectModel, self).save(*args, **kwargs)
    
    def delete(self, *args, **kwargs):
        NotificationModel.objects.create(
            content = "Bir Abituriyent fənni silindi: " + self.name,
            type = "D"
        )
        return super(AbiturientSubjectModel, self).delete(*args, **kwargs)


    def __str__(self):
        return self.name
    
class AbiturientGroupModel(models.Model):
    name = models.CharField("Ad", max_length=200)

    class Meta:
        verbose_name = "Qrup"
        verbose_name_plural = "Abituriyent qrupları"

    def save(self, *args, **kwargs):
        if self.id:
            NotificationModel.objects.create(
                content = "Abituriyent qrupu yeniləndi: " + self.name,
                type = "U"
            )
        else:
            NotificationModel.objects.create(
                content = "Abituriyent qrupu əlavə olundu: " + self.name,
                type = "A"
            )
        return super(AbiturientGroupModel, self).save(*args, **kwargs)
    
    def delete(self, *args, **kwargs):
        NotificationModel.objects.create(
            content = "Bir Abituriyent qrupu silindi: " + self.name,
            type = "D"
        )
        return super(AbiturientGroupModel, self).delete(*args, **kwargs)


    def __str__(self):
        return self.name

class AbiturientModel(models.Model):
    SECTORS = (
        ("AZ", "Azərbaycan dili"),
        ("RU", "Rus dili"),
    )
    student = models.OneToOneField(StudentModel, verbose_name="Tələbə", on_delete=models.CASCADE, related_name="abiturient")
    blocks = models.ManyToManyField(AbiturientBlockModel, verbose_name="Bloklar", related_name="block_abiturients", blank=True, null=True)
    abiturient_class = models.ForeignKey(AbiturientClassModel, verbose_name="Sinif", on_delete=models.CASCADE, related_name="class_abiturients", blank=True, null=True)
    subjects = models.ManyToManyField(AbiturientSubjectModel, verbose_name="Fənnlər", related_name="subject_abiturients", blank=True, null=True)
    group = models.ForeignKey(AbiturientGroupModel, verbose_name="Qrup", on_delete=models.CASCADE, related_name="group_abiturients", blank=True, null=True)
    dim_point = models.FloatField("DİM balı", blank=True, null=True)
    sector = models.CharField("Bölmə", max_length=2, choices=SECTORS, default="AZ")

    class Meta:
        verbose_name = "Abituriyent"
        verbose_name_plural = "Abituriyentlər"

    def save(self, *args, **kwargs):
        if self.id and self.student.payment_date:
            mon = 8
            year = self.student.payment_date.year
            months = accounting.models.MonthModel.objects.filter(
                season = self.student.season
            )
            for month in months: 
                day = self.student.payment_date.day
                mon = mon + 1
                if mon == 13:
                    mon = 1
                    year = year + 1
                elif mon in (4, 6, 9, 11) and day == 31:
                    day = 30
                elif mon == 2 and day > 28:
                    day = 28
                if not accounting.models.AbiturientPaymentInformationModel.objects.filter(
                    abiturient = self,
                    month = month
                ).exists():
                    accounting.models.AbiturientPaymentInformationModel.objects.create(
                        abiturient = self,
                        month = month,
                        payment_date = date(year, mon, day),
                        payment_amount = self.student.payment_amount
                    )
                else:
                    paymentinfo = accounting.models.AbiturientPaymentInformationModel.objects.get(abiturient=self, month=month)
                    paymentinfo.payment_date = date(year, mon, day)
                    paymentinfo.payment_amount = self.student.payment_amount
                    paymentinfo.save()
        elif self.id:
            NotificationModel.objects.create(
                content = self.student.season.branch.name + " filialında bir abituriyentin məlumatları yeniləndi: " + self.student.get_full_name,
                type = "U"
            )
        else:
            NotificationModel.objects.create(
                content = self.student.season.branch.name + " filialına bir abituriyent əlavə olundu: " + self.student.get_full_name,
                type = "A"
            )

        return super(AbiturientModel, self).save(*args, **kwargs)
    
    def delete(self, *args, **kwargs):
        NotificationModel.objects.create(
            content = self.student.season.branch.name + " filialından bir abituriyent silindi: " + self.student.get_full_name,
            type = "D"
        )
        return super(AbiturientModel, self).delete(*args, **kwargs)

    def __str__(self):
        return self.student.first_name + " " + self.student.last_name
            
class MasterForeignLanguageModel(models.Model):
    name = models.CharField("Ad", max_length=200)

    class Meta:
        verbose_name = "Xarici dil"
        verbose_name_plural = "Magistratura xarici dilləri"

    def save(self, *args, **kwargs):
        if self.id:
            NotificationModel.objects.create(
                content = "Magistraturaya hazırlıq xarici dili yeniləndi: " + self.name,
                type = "U"
            )
        else:
            NotificationModel.objects.create(
                content = "Magistraturaya hazırlıq xarici dili əlavə olundu: " + self.name,
                type = "A"
            )
        return super(MasterForeignLanguageModel, self).save(*args, **kwargs)
    
    def delete(self, *args, **kwargs):
        NotificationModel.objects.create(
            content = "Magistraturaya hazırlıq xarici dili silindi: " + self.name,
            type = "D"
        )
        return super(MasterForeignLanguageModel, self).delete(*args, **kwargs)


    def __str__(self):
        return self.name

class MasterSubjectModel(models.Model):
    name = models.CharField("Ad", max_length=200)

    class Meta:
        verbose_name = "Fənn"
        verbose_name_plural = "Magistraturaya hazırlıq fənnləri"

    def save(self, *args, **kwargs):
        if self.id:
            NotificationModel.objects.create(
                content = "Magistraturaya hazırlıq fənni yeniləndi: " + self.name,
                type = "U"
            )
        else:
            NotificationModel.objects.create(
                content = "Magistraturaya hazırlıq fənni əlavə olundu: " + self.name,
                type = "A"
            )
        return super(MasterSubjectModel, self).save(*args, **kwargs)
    
    def delete(self, *args, **kwargs):
        NotificationModel.objects.create(
            content = "Magistraturaya hazırlıq fənni silindi: " + self.name,
            type = "D"
        )
        return super(MasterSubjectModel, self).delete(*args, **kwargs)


    def __str__(self):
        return self.name
    
class MasterGroupModel(models.Model):
    name = models.CharField("Ad", max_length=200)

    class Meta:
        verbose_name = "Qrup"
        verbose_name_plural = "Magistraturaya hazırlıq qrupları"

    def save(self, *args, **kwargs):
        if self.id:
            NotificationModel.objects.create(
                content = "Magistraturaya hazırlıq qrupu yeniləndi: " + self.name,
                type = "U"
            )
        else:
            NotificationModel.objects.create(
                content = "Magistraturaya hazırlıq qrupu əlavə olundu: " + self.name,
                type = "A"
            )
        return super(MasterGroupModel, self).save(*args, **kwargs)
    
    def delete(self, *args, **kwargs):
        NotificationModel.objects.create(
            content = "Magistraturaya hazırlıq qrupu silindi: " + self.name,
            type = "D"
        )
        return super(MasterGroupModel, self).delete(*args, **kwargs)


    def __str__(self):
        return self.name

class MasterModel(models.Model):
    student = models.OneToOneField(StudentModel, verbose_name="Tələbə", on_delete=models.CASCADE, related_name="master")
    language = models.ForeignKey(MasterForeignLanguageModel, verbose_name="Xarici dil", on_delete=models.CASCADE, related_name="language_masters")
    subjects = models.ManyToManyField(MasterSubjectModel, verbose_name="Fənnlər", related_name="subject_masters")
    group = models.ForeignKey(MasterGroupModel, verbose_name="Qrup", on_delete=models.CASCADE, related_name="group_masters")
    dim_point = models.FloatField("Ali məktəbə qəbul balı", blank=True, null=True)

    class Meta:
        verbose_name = "Magistraturaya hazırlıq"
        verbose_name_plural = "Magistraturaya hazırlıqlar"

    def save(self, *args, **kwargs):
        if self.id and self.student.payment_date:
            mon = 8
            year = self.student.payment_date.year
            months = accounting.models.MonthModel.objects.filter(
                season = self.student.season
            )
            for month in months: 
                day = self.student.payment_date.day
                mon = mon + 1
                if mon == 13:
                    mon = 1
                    year = year + 1
                elif mon in (4, 6, 9, 11) and day == 31:
                    day = 30
                elif mon == 2 and day > 28:
                    day = 28
                if not accounting.models.MasterPaymentInformationModel.objects.filter(
                    master = self,
                    month = month
                ).exists():
                    accounting.models.MasterPaymentInformationModel.objects.create(
                        master = self,
                        month = month,
                        payment_date = date(year, mon, day),
                        payment_amount = self.student.payment_amount
                    )
                else:
                    paymentinfo = accounting.models.MasterPaymentInformationModel.objects.get(master=self, month=month)
                    paymentinfo.payment_date = date(year, mon, day)
                    paymentinfo.payment_amount = self.student.payment_amount
                    paymentinfo.save()
        elif self.id:
            NotificationModel.objects.create(
                content = self.student.season.branch.name + " filialında bir magistraturaya hazırlıq tələbəsinin məlumatları yeniləndi: " + self.student.get_full_name,
                type = "U"
            )
        else:
            NotificationModel.objects.create(
                content = self.student.season.branch.name + " filialına bir magistraturaya hazırlıq tələbəsi əlavə olundu: " + self.student.get_full_name,
                type = "A"
            )
        return super(MasterModel, self).save(*args, **kwargs)
    
    def delete(self, *args, **kwargs):
        NotificationModel.objects.create(
            content = self.student.season.branch.name + " filialından bir magistraturaya hazırlıq tələbəsi silindi: " + self.student.get_full_name,
            type = "D"
        )
        return super(MasterModel, self).delete(*args, **kwargs)

    def __str__(self):
        return self.student.first_name + " " + self.student.last_name

class MIQSubjectModel(models.Model):
    name = models.CharField("Ad", max_length=200)

    class Meta:
        verbose_name = "Fənn"
        verbose_name_plural = "MİQ fənnləri"

    def save(self, *args, **kwargs):
        if self.id:
            NotificationModel.objects.create(
                content = "MIQ fənni yeniləndi: " + self.name,
                type = "U"
            )
        else:
            NotificationModel.objects.create(
                content = "MIQ fənni əlavə olundu: " + self.name,
                type = "A"
            )
        return super(MIQSubjectModel, self).save(*args, **kwargs)
    
    def delete(self, *args, **kwargs):
        NotificationModel.objects.create(
            content = "MIQ fənni silindi: " + self.name,
            type = "D"
        )
        return super(MIQSubjectModel, self).delete(*args, **kwargs)


    def __str__(self):
        return self.name  

class MIQModel(models.Model):
    student = models.OneToOneField(StudentModel, verbose_name="Tələbə", on_delete=models.CASCADE, related_name="miq")
    specialty = models.CharField("İxtisas", max_length=300)
    subjects = models.ManyToManyField(MIQSubjectModel, verbose_name="Fənnlər", related_name="subject_miqs")

    class Meta:
        verbose_name = "MİQ"
        verbose_name_plural = "MİQlər"

    def save(self, *args, **kwargs):
        if self.id and self.student.payment_date:
            mon = 8
            year = self.student.payment_date.year
            months = accounting.models.MonthModel.objects.filter(
                season = self.student.season
            )
            for month in months: 
                day = self.student.payment_date.day
                mon = mon + 1
                if mon == 13:
                    mon = 1
                    year = year + 1
                elif mon in (4, 6, 9, 11) and day == 31:
                    day = 30
                elif mon == 2 and day > 28:
                    day = 28
                if not accounting.models.MIQPaymentInformationModel.objects.filter(
                    miq = self,
                    month = month
                ).exists():
                    accounting.models.MIQPaymentInformationModel.objects.create(
                        miq = self,
                        month = month,
                        payment_date = date(year, mon, day),
                        payment_amount = self.student.payment_amount
                    )
                else:
                    paymentinfo = accounting.models.MIQPaymentInformationModel.objects.get(miq=self, month=month)
                    paymentinfo.payment_date = date(year, mon, day)
                    paymentinfo.payment_amount = self.student.payment_amount
                    paymentinfo.save()
        elif self.id:
            NotificationModel.objects.create(
                content = self.student.season.branch.name + " filialında bir miq tələbəsinin məlumatları yeniləndi: " + self.student.get_full_name,
                type = "U"
            )
        else:
            NotificationModel.objects.create(
                content = self.student.season.branch.name + " filialına bir miq tələbəsi əlavə olundu: " + self.student.get_full_name,
                type = "A"
            )

        return super(MIQModel, self).save(*args, **kwargs)
    
    def delete(self, *args, **kwargs):
        NotificationModel.objects.create(
            content = self.student.season.branch.name + " filialından bir miq tələbəsi silindi: " + self.student.get_full_name,
            type = "D"
        )
        return super(MIQModel, self).delete(*args, **kwargs)

    def __str__(self):
        return self.student.first_name + " " + self.student.last_name

class CivilServiceSubjectModel(models.Model):
    name = models.CharField("Ad", max_length=200)

    class Meta:
        verbose_name = "Fənn"
        verbose_name_plural = "Dövlət qulluğu fənnləri"

    def save(self, *args, **kwargs):
        if self.id:
            NotificationModel.objects.create(
                content = "Dövlət qulluğu fənni yeniləndi: " + self.name,
                type = "U"
            )
        else:
            NotificationModel.objects.create(
                content = "Dövlət qulluğu fənni əlavə olundu: " + self.name,
                type = "A"
            )
        return super(CivilServiceSubjectModel, self).save(*args, **kwargs)
    
    def delete(self, *args, **kwargs):
        NotificationModel.objects.create(
            content = "Dövlət qulluğu fənni silindi: " + self.name,
            type = "D"
        )
        return super(CivilServiceSubjectModel, self).delete(*args, **kwargs)


    def __str__(self):
        return self.name
       
class CivilServiceModel(models.Model):
    student = models.OneToOneField(StudentModel, verbose_name="Tələbə", on_delete=models.CASCADE, related_name="civilservice")
    subjects = models.ManyToManyField(CivilServiceSubjectModel, verbose_name="Fənnlər", related_name="subject_civilservices")

    class Meta:
        verbose_name = "Dövlət qulluğu"
        verbose_name_plural = "Dövlət qulluqları"

    def save(self, *args, **kwargs):
        if self.id and self.student.payment_date:
            mon = 8
            year = self.student.payment_date.year 
            months = accounting.models.MonthModel.objects.filter(
                season = self.student.season
            )
            for month in months:
                day = self.student.payment_date.day
                mon = mon + 1
                if mon == 13:
                    mon = 1
                    year = year + 1
                elif mon in (4, 6, 9, 11) and day == 31:
                    day = 30
                elif mon == 2 and day > 28:
                    day = 28
                if not accounting.models.CivilServicePaymentInformationModel.objects.filter(
                    civilservice = self,
                    month = month
                ).exists():
                    accounting.models.CivilServicePaymentInformationModel.objects.create(
                        civilservice = self,
                        month = month,
                        payment_date = date(year, mon, day),
                        payment_amount = self.student.payment_amount
                    )
                else:
                    paymentinfo = accounting.models.CivilServicePaymentInformationModel.objects.get(civilservice=self, month=month)
                    paymentinfo.payment_date = date(year, mon, day)
                    paymentinfo.payment_amount = self.student.payment_amount
                    paymentinfo.save()

        elif self.id:
            NotificationModel.objects.create(
                content = self.student.season.branch.name + " filialında bir dövlət qulluğu tələbəsinin məlumatları yeniləndi: " + self.student.get_full_name,
                type = "U"
            )
        else:
            NotificationModel.objects.create(
                content = self.student.season.branch.name + " filialına bir dövlət qulluğu tələbəsi əlavə olundu: " + self.student.get_full_name,
                type = "A"
            )
        return super(CivilServiceModel, self).save(*args, **kwargs)
    
    def delete(self, *args, **kwargs):
        NotificationModel.objects.create(
            content = self.student.season.branch.name + " filialından bir dövlət qulluğu tələbəsi silindi: " + self.student.get_full_name,
            type = "D"
        )
        return super(CivilServiceModel, self).delete(*args, **kwargs)

    def __str__(self):
        return self.student.first_name + " " + self.student.last_name
    
class ForeignLanguageModel(models.Model):
    student = models.OneToOneField(StudentModel, verbose_name="Tələbə", on_delete=models.CASCADE, related_name="foreignlanguage")

    class Meta:
        verbose_name = "Xarici dil"
        verbose_name_plural = "Xarici dillər"

    def save(self, *args, **kwargs):
        if self.id and self.student.payment_date:
            mon = 8
            year = self.student.payment_date.year
            months = accounting.models.MonthModel.objects.filter(
                season = self.student.season
            )
            for month in months: 
                day = self.student.payment_date.day
                mon = mon + 1
                if mon == 13:
                    mon = 1
                    year = year + 1
                elif mon in (4, 6, 9, 11) and day == 31:
                    day = 30
                elif mon == 2 and day > 28:
                    day = 28
                if not accounting.models.ForeignLanguagePaymentInformationModel.objects.filter(
                    foreignlanguage = self,
                    month = month
                ).exists():
                    accounting.models.ForeignLanguagePaymentInformationModel.objects.create(
                        foreignlanguage = self,
                        month = month,
                        payment_date = date(year, mon, day),
                        payment_amount = self.student.payment_amount
                    )
                else:
                    paymentinfo = accounting.models.ForeignLanguagePaymentInformationModel.objects.get(foreignlanguage=self, month=month)
                    paymentinfo.payment_date = date(year, mon, day)
                    paymentinfo.payment_amount = self.student.payment_amount
                    paymentinfo.save()
        elif self.id:
            NotificationModel.objects.create(
                content = self.student.season.branch.name + " filialında bir xarici dil tələbəsinin məlumatları yeniləndi: " + self.student.get_full_name,
                type = "U"
            )
        else:
            NotificationModel.objects.create(
                content = self.student.season.branch.name + " filialına bir xarici dil tələbəsi əlavə olundu: " + self.student.get_full_name,
                type = "A"
            )
        return super(ForeignLanguageModel, self).save(*args, **kwargs)
    
    def delete(self, *args, **kwargs):
        NotificationModel.objects.create(
            content = self.student.season.branch.name + " filialından bir xarici dil tələbəsi silindi: " + self.student.get_full_name,
            type = "D"
        )
        return super(ForeignLanguageModel, self).delete(*args, **kwargs)

    def __str__(self):
        return self.student.first_name + " " + self.student.last_name
    
class ComputerProgramTypeModel(models.Model):
    name = models.CharField("Ad", max_length=200)

    class Meta:
        verbose_name = "Proqram növü"
        verbose_name_plural = "Kompüter Proqram növləri"

    def save(self, *args, **kwargs):
        if self.id:
            NotificationModel.objects.create(
                content = "Kompüter proqramı yeniləndi: " + self.name,
                type = "U"
            )
        else:
            NotificationModel.objects.create(
                content = "Kompüter proqramı əlavə olundu: " + self.name,
                type = "A"
            )
        return super(ComputerProgramTypeModel, self).save(*args, **kwargs)
    
    def delete(self, *args, **kwargs):
        NotificationModel.objects.create(
            content = "Kompüter proqramı silindi: " + self.name,
            type = "D"
        )
        return super(ComputerProgramTypeModel, self).delete(*args, **kwargs)


    def __str__(self):
        return self.name
    
class ComputerCourseModel(models.Model):
    student = models.OneToOneField(StudentModel, verbose_name="Tələbə", on_delete=models.CASCADE, related_name="computercourse")
    program_types = models.ManyToManyField(ComputerProgramTypeModel, verbose_name="Proqram növləri", related_name="programtypes_computercourses")

    class Meta:
        verbose_name = "Komputer kursu"
        verbose_name_plural = "Komputer kursları"

    def save(self, *args, **kwargs):
        if self.id and self.student.payment_date:
            mon = 8
            year = self.student.payment_date.year
            months = accounting.models.MonthModel.objects.filter(
                season = self.student.season
            )
            for month in months: 
                day = self.student.payment_date.day
                mon = mon + 1
                if mon == 13:
                    mon = 1
                    year = year + 1
                elif mon in (4, 6, 9, 11) and day == 31:
                    day = 30
                elif mon == 2 and day > 28:
                    day = 28
                if not accounting.models.ComputerCoursePaymentInformationModel.objects.filter(
                    computercourse = self,
                    month = month
                ).exists():
                    accounting.models.ComputerCoursePaymentInformationModel.objects.create(
                        computercourse = self,
                        month = month,
                        payment_date = date(year, mon, day),
                        payment_amount = self.student.payment_amount
                    )
                else:
                    paymentinfo = accounting.models.ComputerCoursePaymentInformationModel.objects.get(computercourse=self, month=month)
                    paymentinfo.payment_date = date(year, mon, day)
                    paymentinfo.payment_amount = self.student.payment_amount
                    paymentinfo.save()

        elif self.id:
            NotificationModel.objects.create(
                content = self.student.season.branch.name + " filialında bir kompüter kursu tələbəsinin məlumatları yeniləndi: " + self.student.get_full_name,
                type = "U"
            )
        else:
            NotificationModel.objects.create(
                content = self.student.season.branch.name + " filialına bir kompüter kursu tələbəsi əlavə olundu: " + self.student.get_full_name,
                type = "A"
            )
        return super(ComputerCourseModel, self).save(*args, **kwargs)
    
    def delete(self, *args, **kwargs):
        NotificationModel.objects.create(
            content = self.student.season.branch.name + " filialından bir kompüter kursu tələbəsi silindi: " + self.student.get_full_name,
            type = "D"
        )
        return super(ComputerCourseModel, self).delete(*args, **kwargs)

    def __str__(self):
        return self.student.first_name + " " + self.student.last_name
    
class AccountingModel(models.Model):
    student = models.OneToOneField(StudentModel, verbose_name="Tələbə", on_delete=models.CASCADE, related_name="accounting")

    class Meta:
        verbose_name = "Mühasibatlıq"
        verbose_name_plural = "Mühasibatlıqlar"

    def save(self, *args, **kwargs):
        if self.id and self.student.payment_date:
            mon = 8
            year = self.student.payment_date.year
            months = accounting.models.MonthModel.objects.filter(
                season = self.student.season
            )
            for month in months: 
                day = self.student.payment_date.day
                mon = mon + 1
                if mon == 13:
                    mon = 1
                    year = year + 1
                elif mon in (4, 6, 9, 11) and day == 31:
                    day = 30
                elif mon == 2 and day > 28:
                    day = 28
                if not accounting.models.AccountingPaymentInformationModel.objects.filter(
                    accounting = self,
                    month = month
                ).exists():
                    accounting.models.AccountingPaymentInformationModel.objects.create(
                        accounting = self,
                        month = month,
                        payment_date = date(year, mon, day),
                        payment_amount = self.student.payment_amount
                    )
                else:
                    paymentinfo = accounting.models.AccountingPaymentInformationModel.objects.get(accounting=self, month=month)
                    paymentinfo.payment_date = date(year, mon, day)
                    paymentinfo.payment_amount = self.student.payment_amount
                    paymentinfo.save()
        elif self.id:
            NotificationModel.objects.create(
                content = self.student.season.branch.name + " filialında bir mühasibatlıq tələbəsinin məlumatları yeniləndi: " + self.student.get_full_name,
                type = "U"
            )
        else:
            NotificationModel.objects.create(
                content = self.student.season.branch.name + " filialına bir mühasibatlıq tələbəsi əlavə olundu: " + self.student.get_full_name,
                type = "A"
            )
        return super(AccountingModel, self).save(*args, **kwargs)
    
    def delete(self, *args, **kwargs):
        NotificationModel.objects.create(
            content = self.student.season.branch.name + " filialından bir mühasibatlıq tələbəsi silindi: " + self.student.get_full_name,
            type = "D"
        )
        return super(AccountingModel, self).delete(*args, **kwargs)

    def __str__(self):
        return self.student.first_name + " " + self.student.last_name
    
class HighSchoolClassModel(models.Model):
    name = models.CharField("Ad", max_length=100)

    class Meta:
        verbose_name = "Sinif"
        verbose_name_plural = "Liseylərə hazırlıq sinifləri"

    def save(self, *args, **kwargs):
        if self.id:
            NotificationModel.objects.create(
                content = "Liseylərə hazırlıq sinifi yeniləndi: " + self.name,
                type = "U"
            )
        else:
            NotificationModel.objects.create(
                content = "Liseylərə hazırlıq sinifi əlavə olundu: " + self.name,
                type = "A"
            )
        return super(HighSchoolClassModel, self).save(*args, **kwargs)
    
    def delete(self, *args, **kwargs):
        NotificationModel.objects.create(
            content = "Bir liseylərə hazırlıq sinifi silindi: " + self.name,
            type = "D"
        )
        return super(HighSchoolClassModel, self).delete(*args, **kwargs)


    def __str__(self):
        return self.name
    
class HighSchoolSubjectModel(models.Model):
    name = models.CharField("Ad", max_length=300)

    class Meta:
        verbose_name = "Fənn"
        verbose_name_plural = "Liseylərə hazırlıq fənnləri"

    def save(self, *args, **kwargs):
        if self.id:
            NotificationModel.objects.create(
                content = "Liseylərə hazırlıq fənni yeniləndi: " + self.name,
                type = "U"
            )
        else:
            NotificationModel.objects.create(
                content = "Liseylərə hazırlıq fənni əlavə olundu: " + self.name,
                type = "A"
            )
        return super(HighSchoolSubjectModel, self).save(*args, **kwargs)
    
    def delete(self, *args, **kwargs):
        NotificationModel.objects.create(
            content = "Bir liseylərə hazırlıq fənni silindi: " + self.name,
            type = "D"
        )
        return super(HighSchoolSubjectModel, self).delete(*args, **kwargs)


    def __str__(self):
        return self.name
    
class HighSchoolGroupModel(models.Model):
    name = models.CharField("Ad", max_length=200)

    class Meta:
        verbose_name = "Qrup"
        verbose_name_plural = "Liseylərə hazırlıq qrupları"

    def save(self, *args, **kwargs):
        if self.id:
            NotificationModel.objects.create(
                content = "Liseylərə hazırlıq qrupu yeniləndi: " + self.name,
                type = "U"
            )
        else:
            NotificationModel.objects.create(
                content = "Liseylərə hazırlıq qrupu əlavə olundu: " + self.name,
                type = "A"
            )
        return super(HighSchoolGroupModel, self).save(*args, **kwargs)
    
    def delete(self, *args, **kwargs):
        NotificationModel.objects.create(
            content = "Bir liseylərə hazırlıq qrupu silindi: " + self.name,
            type = "D"
        )
        return super(HighSchoolGroupModel, self).delete(*args, **kwargs)


    def __str__(self):
        return self.name

class HighSchoolModel(models.Model):
    student = models.OneToOneField(StudentModel, verbose_name="Tələbə", on_delete=models.CASCADE, related_name="highschool")
    highschool_class = models.ForeignKey(HighSchoolClassModel, verbose_name="Sinif", on_delete=models.CASCADE, related_name="class_highschools")
    subjects = models.ManyToManyField(HighSchoolSubjectModel, verbose_name="Fənnlər", related_name="subject_highschools")
    group = models.ForeignKey(HighSchoolGroupModel, verbose_name="Qrup", on_delete=models.CASCADE, related_name="group_highschools")

    class Meta:
        verbose_name = "Liseylərə hazırlıq"
        verbose_name_plural = "Liseylərə hazırlıqlar"

    def save(self, *args, **kwargs):
        if self.id and self.student.payment_date:
            mon = 8
            year = self.student.payment_date.year
            months = accounting.models.MonthModel.objects.filter(
                season = self.student.season
            )
            for month in months: 
                day = self.student.payment_date.day
                mon = mon + 1
                if mon == 13:
                    mon = 1
                    year = year + 1
                elif mon in (4, 6, 9, 11) and day == 31:
                    day = 30
                elif mon == 2 and day > 28:
                    day = 28
                if not accounting.models.HighSchoolPaymentInformationModel.objects.filter(
                    highschool = self,
                    month = month
                ).exists():
                    accounting.models.HighSchoolPaymentInformationModel.objects.create(
                        highschool = self,
                        month = month,
                        payment_date = date(year, mon, day),
                        payment_amount = self.student.payment_amount
                    )
                else:
                    paymentinfo = accounting.models.HighSchoolPaymentInformationModel.objects.get(highschool=self, month=month)
                    paymentinfo.payment_date = date(year, mon, day)
                    paymentinfo.payment_amount = self.student.payment_amount
                    paymentinfo.save()
        elif self.id:
            NotificationModel.objects.create(
                content = self.student.season.branch.name + " filialında bir liseylərə hazırlıq tələbəsinin məlumatları yeniləndi: " + self.student.get_full_name,
                type = "U"
            )
        else:
            NotificationModel.objects.create(
                content = self.student.season.branch.name + " filialına bir liseylərə hazırlıq tələbəsi əlavə olundu: " + self.student.get_full_name,
                type = "A"
            )
        return super(HighSchoolModel, self).save(*args, **kwargs)
    
    def delete(self, *args, **kwargs):
        NotificationModel.objects.create(
            content = self.student.season.branch.name + " filialından bir liseylərə hazırlıq tələbəsi silindi: " + self.student.get_full_name,
            type = "D"
        )
        return super(HighSchoolModel, self).delete(*args, **kwargs)

    def __str__(self):
        return self.student.first_name + " " + self.student.last_name
    
class PreSchoolSubjectModel(models.Model):
    name = models.CharField("Ad", max_length=300)

    class Meta:
        verbose_name = "Fənn"
        verbose_name_plural = "Məktəbəqədər hazırlıq fənnləri"

    
    def save(self, *args, **kwargs):
        if self.id:
            NotificationModel.objects.create(
                content = "Məktəbəqədər hazırlıq fənni yeniləndi: " + self.name,
                type = "U"
            )
        else:
            NotificationModel.objects.create(
                content = "Məktəbəqədər hazırlıq fənni əlavə olundu: " + self.name,
                type = "A"
            )
        return super(PreSchoolSubjectModel, self).save(*args, **kwargs)
    
    def delete(self, *args, **kwargs):
        NotificationModel.objects.create(
            content = "Bir məktəbəqədər hazırlıq fənni silindi: " + self.name,
            type = "D"
        )
        return super(PreSchoolSubjectModel, self).delete(*args, **kwargs)


    def __str__(self):
        return self.name

class PreSchoolModel(models.Model):
    student = models.OneToOneField(StudentModel, verbose_name="Tələbə", on_delete=models.CASCADE, related_name="preschool")
    subjects = models.ManyToManyField(PreSchoolSubjectModel, verbose_name="Fənnlər", related_name="subject_preschools")

    class Meta:
        verbose_name = "Məktəbəqədər hazırlıq"
        verbose_name_plural = "Məktəbəqədər hazırlıqlar"

    def save(self, *args, **kwargs):
        if self.id and self.student.payment_date:
            mon = 8
            year = self.student.payment_date.year
            months = accounting.models.MonthModel.objects.filter(
                season = self.student.season
            )
            for month in months: 
                day = self.student.payment_date.day
                mon = mon + 1
                if mon == 13:
                    mon = 1
                    year = year + 1
                elif mon in (4, 6, 9, 11) and day == 31:
                    day = 30
                elif mon == 2 and day > 28:
                    day = 28
                if not accounting.models.PreSchoolPaymentInformationModel.objects.filter(
                    preschool = self,
                    month = month
                ).exists():
                    accounting.models.PreSchoolPaymentInformationModel.objects.create(
                        preschool = self,
                        month = month,
                        payment_date = date(year, mon, day),
                        payment_amount = self.student.payment_amount
                    )
                else:
                    paymentinfo = accounting.models.PreSchoolPaymentInformationModel.objects.get(preschool=self, month=month)
                    paymentinfo.payment_date = date(year, mon, day)
                    paymentinfo.payment_amount = self.student.payment_amount
                    paymentinfo.save()
        elif self.id:
            NotificationModel.objects.create(
                content = self.student.season.branch.name + " filialında bir məktəbəqədər hazırlıq tələbəsinin məlumatları yeniləndi: " + self.student.get_full_name,
                type = "U"
            )
        else:
            NotificationModel.objects.create(
                content = self.student.season.branch.name + " filialına bir məktəbəqədər hazırlıq tələbəsi əlavə olundu: " + self.student.get_full_name,
                type = "A"
            )
        return super(PreSchoolModel, self).save(*args, **kwargs)
    
    def delete(self, *args, **kwargs):
        NotificationModel.objects.create(
            content = self.student.season.branch.name + " filialından bir məktəbəqədər hazırlıq tələbəsi silindi: " + self.student.get_full_name,
            type = "D"
        )
        return super(PreSchoolModel, self).delete(*args, **kwargs)

    def __str__(self):
        return self.student.first_name + " " + self.student.last_name
    
class PrimarySchoolClassModel(models.Model):
    name = models.CharField("Ad", max_length=100)

    class Meta:
        verbose_name = "Sinif"
        verbose_name_plural = "İbtidai sinifləri"

    def save(self, *args, **kwargs):
        if self.id:
            NotificationModel.objects.create(
                content = "İbtidai sinifi yeniləndi: " + self.name,
                type = "U"
            )
        else:
            NotificationModel.objects.create(
                content = "İbtidai sinifi əlavə olundu: " + self.name,
                type = "A"
            )
        return super(PrimarySchoolClassModel, self).save(*args, **kwargs)
    
    def delete(self, *args, **kwargs):
        NotificationModel.objects.create(
            content = "Bir ibtidai sinifi silindi: " + self.name,
            type = "D"
        )
        return super(HighSchoolClassModel, self).delete(*args, **kwargs)

    def __str__(self):
        return self.name
    
class PrimarySchoolSubjectModel(models.Model):
    name = models.CharField("Ad", max_length=300)

    class Meta:
        verbose_name = "Fənn"
        verbose_name_plural = "İbtidai fənnləri"

    def save(self, *args, **kwargs):
        if self.id:
            NotificationModel.objects.create(
                content = "İbtidai fənni yeniləndi: " + self.name,
                type = "U"
            )
        else:
            NotificationModel.objects.create(
                content = "İbtidai fənni əlavə olundu: " + self.name,
                type = "A"
            )
        return super(PrimarySchoolSubjectModel, self).save(*args, **kwargs)
    
    def delete(self, *args, **kwargs):
        NotificationModel.objects.create(
            content = "Bir ibtidai fənni silindi: " + self.name,
            type = "D"
        )
        return super(PrimarySchoolSubjectModel, self).delete(*args, **kwargs)


    def __str__(self):
        return self.name
    
class PrimarySchoolGroupModel(models.Model):
    name = models.CharField("Ad", max_length=200)

    class Meta:
        verbose_name = "Qrup"
        verbose_name_plural = "İbtidai qrupları"

    def save(self, *args, **kwargs):
        if self.id:
            NotificationModel.objects.create(
                content = "İbtidai qrupu yeniləndi: " + self.name,
                type = "U"
            )
        else:
            NotificationModel.objects.create(
                content = "İbtidai qrupu əlavə olundu: " + self.name,
                type = "A"
            )
        return super(PrimarySchoolGroupModel, self).save(*args, **kwargs)
    
    def delete(self, *args, **kwargs):
        NotificationModel.objects.create(
            content = "Bir ibtidai qrupu silindi: " + self.name,
            type = "D"
        )
        return super(PrimarySchoolGroupModel, self).delete(*args, **kwargs)

    def __str__(self):
        return self.name

class PrimarySchoolModel(models.Model):
    student = models.OneToOneField(StudentModel, verbose_name="Tələbə", on_delete=models.CASCADE, related_name="primaryschool")
    primaryschool_class = models.ForeignKey(PrimarySchoolClassModel, verbose_name="Sinif", on_delete=models.CASCADE, related_name="class_primaryschools")
    subjects = models.ManyToManyField(PrimarySchoolSubjectModel, verbose_name="Fənnlər", related_name="subject_primaryschools")
    group = models.ForeignKey(PrimarySchoolGroupModel, verbose_name="Qrup", on_delete=models.CASCADE, related_name="group_primaryschools")

    class Meta:
        verbose_name = "İbtidai"
        verbose_name_plural = "İbtidailər"

    def save(self, *args, **kwargs):
        if self.id and self.student.payment_date:
            mon = 8
            year = self.student.payment_date.year
            months = accounting.models.MonthModel.objects.filter(
                season = self.student.season
            )
            for month in months: 
                day = self.student.payment_date.day
                mon = mon + 1
                if mon == 13:
                    mon = 1
                    year = year + 1
                elif mon in (4, 6, 9, 11) and day == 31:
                    day = 30
                elif mon == 2 and day > 28:
                    day = 28
                if not accounting.models.PrimarySchoolPaymentInformationModel.objects.filter(
                    primaryschool = self,
                    month = month
                ).exists():
                    accounting.models.PrimarySchoolPaymentInformationModel.objects.create(
                        primaryschool = self,
                        month = month,
                        payment_date = date(year, mon, day),
                        payment_amount = self.student.payment_amount
                    )
                else:
                    paymentinfo = accounting.models.PrimarySchoolPaymentInformationModel.objects.get(primaryschool=self, month=month)
                    paymentinfo.payment_date = date(year, mon, day)
                    paymentinfo.payment_amount = self.student.payment_amount
                    paymentinfo.save()
        elif self.id:
            NotificationModel.objects.create(
                content = self.student.season.branch.name + " filialında bir ibtidai tələbəsinin məlumatları yeniləndi: " + self.student.get_full_name,
                type = "U"
            )
        else:
            NotificationModel.objects.create(
                content = self.student.season.branch.name + " filialına bir ibtidai tələbəsi əlavə olundu: " + self.student.get_full_name,
                type = "A"
            )
        return super(PrimarySchoolModel, self).save(*args, **kwargs)
    
    def delete(self, *args, **kwargs):
        NotificationModel.objects.create(
            content = self.student.season.branch.name + " filialından bir ibtidai tələbəsi silindi: " + self.student.get_full_name,
            type = "D"
        )
        return super(PrimarySchoolModel, self).delete(*args, **kwargs)

    def __str__(self):
        return self.student.first_name + " " + self.student.last_name