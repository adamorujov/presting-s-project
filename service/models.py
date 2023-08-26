from django.db import models
from account.models import Account

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

    class Meta:
        verbose_name = "Tələbə"
        verbose_name_plural = "Tələbələr"

    @property
    def get_full_name(self):
        return self.first_name + " " + self.last_name

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

    class Meta:
        verbose_name = "Müəllim"
        verbose_name_plural = "Müəllimlər"

    def __str__(self):
        return self.first_name + " " + self.last_name
    
class AccountantModel(models.Model):
    account = models.OneToOneField(Account, on_delete=models.CASCADE, related_name="accountant")
    branch = models.ForeignKey(BranchModel, on_delete=models.CASCADE, related_name="branch_accountant")

    class Meta:
        verbose_name = "Mühasib"
        verbose_name_plural = "Mühasiblər"

    def __str__(self):
        return self.account.first_name + " " + self.account.last_name

class AbiturientBlockModel(models.Model):
    name = models.CharField("Ad", max_length=100)

    class Meta:
        verbose_name = "Blok"
        verbose_name_plural = "Abituriyent blokları"

    def __str__(self):
        return self.name
    
class AbiturientClassModel(models.Model):
    name = models.CharField("Ad", max_length=100)

    class Meta:
        verbose_name = "Sinif"
        verbose_name_plural = "Abituriyent sinifləri"

    def __str__(self):
        return self.name
    
class AbiturientSubjectModel(models.Model):
    name = models.CharField("Ad", max_length=300)

    class Meta:
        verbose_name = "Fənn"
        verbose_name_plural = "Abituriyent fənnləri"

    def __str__(self):
        return self.name
    
class AbiturientGroupModel(models.Model):
    name = models.CharField("Ad", max_length=200)

    class Meta:
        verbose_name = "Qrup"
        verbose_name_plural = "Abituriyent qrupları"

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

    def __str__(self):
        return self.student.first_name + " " + self.student.last_name
    
class MasterForeignLanguageModel(models.Model):
    name = models.CharField("Ad", max_length=200)

    class Meta:
        verbose_name = "Xarici dil"
        verbose_name_plural = "Magistr xarici dilləri"

    def __str__(self):
        return self.name

class MasterSubjectModel(models.Model):
    name = models.CharField("Ad", max_length=200)

    class Meta:
        verbose_name = "Fənn"
        verbose_name_plural = "Magistr fənnləri"

    def __str__(self):
        return self.name
    
class MasterGroupModel(models.Model):
    name = models.CharField("Ad", max_length=200)

    class Meta:
        verbose_name = "Qrup"
        verbose_name_plural = "Magistr qrupları"

    def __str__(self):
        return self.name

class MasterModel(models.Model):
    student = models.OneToOneField(StudentModel, verbose_name="Tələbə", on_delete=models.CASCADE, related_name="master")
    language = models.ForeignKey(MasterForeignLanguageModel, verbose_name="Xarici dil", on_delete=models.CASCADE, related_name="language_masters")
    subjects = models.ManyToManyField(MasterSubjectModel, verbose_name="Fənnlər", related_name="subject_masters")
    group = models.ForeignKey(MasterGroupModel, verbose_name="Qrup", on_delete=models.CASCADE, related_name="group_masters")
    dim_point = models.FloatField("Ali məktəbə qəbul balı", blank=True, null=True)

    class Meta:
        verbose_name = "Magistrant"
        verbose_name_plural = "Magistrantlar"

    def __str__(self):
        return self.student.first_name + " " + self.student.last_name

class MIQSubjectModel(models.Model):
    name = models.CharField("Ad", max_length=200)

    class Meta:
        verbose_name = "Fənn"
        verbose_name_plural = "MİQ fənnləri"

    def __str__(self):
        return self.name  

class MIQModel(models.Model):
    student = models.OneToOneField(StudentModel, verbose_name="Tələbə", on_delete=models.CASCADE, related_name="miq")
    specialty = models.CharField("İxtisas", max_length=300)
    subjects = models.ManyToManyField(MIQSubjectModel, verbose_name="Fənnlər", related_name="subject_miqs")

    class Meta:
        verbose_name = "MİQ"
        verbose_name_plural = "MİQlər"

    def __str__(self):
        return self.student.first_name + " " + self.student.last_name

class CivilServiceSubjectModel(models.Model):
    name = models.CharField("Ad", max_length=200)

    class Meta:
        verbose_name = "Fənn"
        verbose_name_plural = "Dövlət qulluğu fənnləri"

    def __str__(self):
        return self.name
       
class CivilServiceModel(models.Model):
    student = models.OneToOneField(StudentModel, verbose_name="Tələbə", on_delete=models.CASCADE, related_name="civilservice")
    subjects = models.ManyToManyField(CivilServiceSubjectModel, verbose_name="Fənnlər", related_name="subject_civilservices")

    class Meta:
        verbose_name = "Dövlət qulluğu"
        verbose_name_plural = "Dövlət qulluqları"

    def __str__(self):
        return self.student.first_name + " " + self.student.last_name
    
class ForeignLanguageModel(models.Model):
    student = models.OneToOneField(StudentModel, verbose_name="Tələbə", on_delete=models.CASCADE, related_name="foreignlanguage")

    class Meta:
        verbose_name = "Xarici dil"
        verbose_name_plural = "Xarici dillər"

    def __str__(self):
        return self.student.first_name + " " + self.student.last_name
    
class ComputerProgramTypeModel(models.Model):
    name = models.CharField("Ad", max_length=200)

    class Meta:
        verbose_name = "Proqram növü"
        verbose_name_plural = "Kompüter Proqram növləri"

    def __str__(self):
        return self.name
    
class ComputerCourseModel(models.Model):
    student = models.OneToOneField(StudentModel, verbose_name="Tələbə", on_delete=models.CASCADE, related_name="computercourse")
    program_types = models.ManyToManyField(ComputerProgramTypeModel, verbose_name="Proqram növləri", related_name="programtypes_computercourses")

    class Meta:
        verbose_name = "Komputer kursu"
        verbose_name_plural = "Komputer kursları"

    def __str__(self):
        return self.student.first_name + " " + self.student.last_name
    
class AccountingModel(models.Model):
    student = models.OneToOneField(StudentModel, verbose_name="Tələbə", on_delete=models.CASCADE, related_name="accounting")

    class Meta:
        verbose_name = "Mühasibatlıq"
        verbose_name_plural = "Mühasibatlıqlar"

    def __str__(self):
        return self.student.first_name + " " + self.student.last_name
    
class HighSchoolClassModel(models.Model):
    name = models.CharField("Ad", max_length=100)

    class Meta:
        verbose_name = "Sinif"
        verbose_name_plural = "Liseylərə hazırlıq sinifləri"

    def __str__(self):
        return self.name
    
class HighSchoolSubjectModel(models.Model):
    name = models.CharField("Ad", max_length=300)

    class Meta:
        verbose_name = "Fənn"
        verbose_name_plural = "Liseylərə hazırlıq fənnləri"

    def __str__(self):
        return self.name
    
class HighSchoolGroupModel(models.Model):
    name = models.CharField("Ad", max_length=200)

    class Meta:
        verbose_name = "Qrup"
        verbose_name_plural = "Liseylərə hazırlıq qrupları"

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

    def __str__(self):
        return self.student.first_name + " " + self.student.last_name
    
class PreSchoolSubjectModel(models.Model):
    name = models.CharField("Ad", max_length=300)

    class Meta:
        verbose_name = "Fənn"
        verbose_name_plural = "Məktəbəqədər hazırlıq fənnləri"

    def __str__(self):
        return self.name

class PreSchoolModel(models.Model):
    student = models.OneToOneField(StudentModel, verbose_name="Tələbə", on_delete=models.CASCADE, related_name="preschool")
    subjects = models.ManyToManyField(PreSchoolSubjectModel, verbose_name="Fənnlər", related_name="subject_preschools")

    class Meta:
        verbose_name = "Məktəbəqədər hazırlıq"
        verbose_name_plural = "Məktəbəqədər hazırlıqlar"

    def __str__(self):
        return self.student.first_name + " " + self.student.last_name
    
class PrimarySchoolClassModel(models.Model):
    name = models.CharField("Ad", max_length=100)

    class Meta:
        verbose_name = "Sinif"
        verbose_name_plural = "İbtidai sinifləri"

    def __str__(self):
        return self.name
    
class PrimarySchoolSubjectModel(models.Model):
    name = models.CharField("Ad", max_length=300)

    class Meta:
        verbose_name = "Fənn"
        verbose_name_plural = "İbtidai fənnləri"

    def __str__(self):
        return self.name
    
class PrimarySchoolGroupModel(models.Model):
    name = models.CharField("Ad", max_length=200)

    class Meta:
        verbose_name = "Qrup"
        verbose_name_plural = "İbtidai qrupları"

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

    def __str__(self):
        return self.student.first_name + " " + self.student.last_name