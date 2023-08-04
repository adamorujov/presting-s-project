from django.db import models
from ckeditor.fields import RichTextField

class SettingsModel(models.Model):
    logo = models.ImageField("Loqo", upload_to="logo/", blank=True, null=True)
    logo_active = models.BooleanField("Status", default=True)
    favicon = models.ImageField("Ikon", upload_to="favicon/", blank=True, null=True)
    favicon_active = models.BooleanField("Status", default=True)
    about_us = RichTextField("Haqqımızda", blank=True, null=True)
    about_active = models.BooleanField("Status", default=True)

    about_page_banner = models.ImageField("Haqqımızda", upload_to="banner_images/", blank=True, null=True)
    about_page_active = models.BooleanField("Haqqımızda", default=True)
    success_page_banner = models.ImageField("Uğurlarımız", upload_to="banner_images/", blank=True, null=True)
    success_page_active = models.BooleanField("Uğurlarımız", default=True)
    service_page_banner = models.ImageField("Xidmətlərimiz", upload_to="banner_images/", blank=True, null=True)
    service_page_active = models.BooleanField("Xidmətlərimiz", default=True)
    news_page_banner = models.ImageField("Xəbərlər", upload_to="banner_images/", blank=True, null=True)
    news_page_active = models.BooleanField("Xəbərlər", default=True)
    gallery_page_banner = models.ImageField("Foto Qalereya", upload_to="banner_images/", blank=True, null=True)
    gallery_page_active = models.BooleanField("Foto Qalereya", default=True)
    video_gallery_page_banner = models.ImageField("Video Qalereya", upload_to="banner_images/", blank=True, null=True)
    video_gallery_page_active = models.BooleanField("Video Qalereya", default=True)
    resume_page_banner = models.ImageField("CV göndər", upload_to="banner_images/", blank=True, null=True)
    resume_page_active = models.BooleanField("CV göndər", default=True)
    contact_page_banner = models.ImageField("Əlaqə", upload_to="banner_images/", blank=True, null=True)
    contact_page_active = models.BooleanField("Əlaqə", default=True)
    edition_page_banner = models.ImageField("Nəşrlərimiz", upload_to="banner_images/", blank=True, null=True)
    edition_page_active = models.BooleanField("Nəşrlərimiz", default=True)
    register_page_banner = models.ImageField("Kursa onlayn qeydiyyat", upload_to="banner_images/", blank=True, null=True)
    register_page_active = models.BooleanField("Kursa onlayn qeydiyyat", default=True)

    class Meta:
        verbose_name = "Parametr"
        verbose_name_plural = "Parametrlər"

    def __str__(self):
        return "Parametrlər"

class BannerModel(models.Model):
    image = models.ImageField("Şəkil", upload_to="banner_images/")
    title = models.CharField("Başlıq", max_length=256)
    link = models.URLField("Link", max_length=2048)
    is_active = models.BooleanField("Status", default=False)

    class Meta:
        verbose_name = "Banner"
        verbose_name_plural = "Bannerlər"

    def __str__(self):
        return self.title

class ContactInformationModel(models.Model):
    email = models.EmailField("Email", max_length=256, blank=True, null=True)
    contact_number = models.CharField("Əlaqə nömrəsi", max_length=256, blank=True, null=True)
    is_active = models.BooleanField("Status", default=False)

    class Meta:
        verbose_name = "Əlaqə məlumatı"
        verbose_name_plural = "Əlaqə məlumatları"
        ordering = ("-id", )

    def __str__(self):
        contact_informations = ContactInformationModel.objects.all()
        return "Əlaqə məlumatı " + str(list(contact_informations).index(self) + 1)

class SocialMediaModel(models.Model):
    name = models.CharField("Ad", max_length=100)
    icon_name = models.CharField("İkon", max_length=100)
    color_code = models.CharField("Rəng kodu", max_length=10, blank=True, null=True)
    link = models.URLField("Link", max_length=2048, blank=True, null=True)
    is_active = models.BooleanField("Status", default=False)

    class Meta:
        verbose_name = "Sosial media"
        verbose_name_plural = "Sosial media hesabları"
        ordering = ("-id", )

    def __str__(self):
        return self.name

class NewsModel(models.Model):
    title = models.CharField("Başlıq", max_length=256)
    image = models.ImageField("Şəkil", upload_to="news_images/", blank=True, null=True)
    pub_date = models.DateField("Tarix", blank=True, null=True)
    content = RichTextField("Məzmun", blank=True, null=True)
    is_active = models.BooleanField("Status", default=False)

    class Meta:
        verbose_name = "Xəbər"
        verbose_name_plural = "Xəbərlər"
        ordering = ("-id", )

    def __str__(self):
        return self.title

class VideoGalleryModel(models.Model):
    video_link = models.URLField("Video linki", max_length=2048)
    is_active = models.BooleanField("Status", default=False)

    class Meta:
        verbose_name = "Video"
        verbose_name_plural = "Video Qalereya"
        ordering = ("-id", )

    def __str__(self):
        return self.video_link[:150] + "..."

class PhotoGalleryModel(models.Model):
    title = models.CharField("Başlıq", max_length=528)
    image = models.ImageField("Şəkil", upload_to="photo_gallery_images/")
    is_active = models.BooleanField("Status", default=False)

    class Meta:
        verbose_name = "Foto Qalereya"
        verbose_name_plural = "Foto Qalereya"
        ordering = ("-id",)

    def __str__(self):
        return self.title

class PhotoGalleryItem(models.Model):
    title = models.CharField("Başlıq", max_length=528)
    image = models.ImageField("Şəkil", upload_to="photo_gallery_item_images/")
    photo_gallery = models.ForeignKey(PhotoGalleryModel, on_delete=models.CASCADE, related_name="photo_gallery_items")
    is_active = models.BooleanField("Status", default=False)

    class Meta:
        verbose_name = "Foto"
        verbose_name_plural = "Fotolar"
        ordering = ("-id",)

    def __str__(self):
        return self.title

class TeacherModel(models.Model):
    name = models.CharField("Ad", max_length=100)
    image = models.ImageField("Şəkil", upload_to="teacher_images/", blank=True, null=True)
    surname = models.CharField("Soyad", max_length=100)
    profession = models.CharField("Sahə", max_length=100, blank=True, null=True)
    mission = models.CharField("Vəzifə", max_length=100, blank=True, null=True)
    about = models.TextField("Haqqında", blank=True, null=True)
    is_active = models.BooleanField("Status", default=False)

    class Meta:
        verbose_name = "Müəllim"
        verbose_name_plural = "Müəllimlər"
        ordering = ("-id", )

    def __str__(self):
        return self.name + " " + self.surname

class SubscribeModel(models.Model):
    pass

class ServiceModel(models.Model):
    title = models.CharField("Başlıq", max_length=256)
    image = models.ImageField("Şəkil", upload_to="service_images/")
    content = RichTextField("Məzmun", blank=True, null=True)
    is_active = models.BooleanField("Status", default=False)

    class Meta:
        verbose_name = "Xidmət"
        verbose_name_plural = "Xidmətlər"
        ordering = ("-id",)

    def __str__(self):
        return self.title


class BranchModel(models.Model):
    name = models.CharField("Ad", max_length=256)
    website = models.URLField("Vebsayt", max_length=2048, blank=True, null=True)
    email = models.EmailField("Email", max_length=256, blank=True, null=True)
    address = models.TextField("Ünvan", blank=True, null=True)
    is_active = models.BooleanField("Status", default=False)

    class Meta:
        verbose_name = "Filial"
        verbose_name_plural = "Filiallar"
        ordering = ("-id",)

    def __str__(self):
        return self.name

class BranchContactNumberModel(models.Model):
    phone_number = models.CharField("Əlaqə nömrəsi", max_length=50)
    branch = models.ForeignKey(BranchModel, on_delete=models.CASCADE, related_name="contact_numbers")
    is_active = models.BooleanField("Status", default=False)

    class Meta:
        verbose_name = "Filial əlaqə nömrəsi"
        verbose_name_plural = "Filial əlaqə nömrələri"
        ordering = ("-id",)

    def __str__(self):
        return self.phone_number

class SuccessModel(models.Model):
    title = models.TextField("Başlıq")
    is_active = models.BooleanField("Status", default=False)

    class Meta:
        verbose_name = "Uğur"
        verbose_name_plural = "Uğurlar"
        ordering = ("-id",)

    def __str__(self):
        return self.title

class SuccessItemModel(models.Model):
    name = models.CharField("Ad soyad", max_length=128, blank=True, null=True)
    image = models.ImageField("Şəkil", upload_to="success_images/", blank=True, null=True)
    item = models.TextField("Məzmun")
    success = models.ForeignKey(SuccessModel, on_delete=models.CASCADE, related_name="success_items")
    is_active = models.BooleanField("Status", default=False)

    class Meta:
        verbose_name = "Uğur məzmunu"
        verbose_name_plural = "Uğur məzmunları"
        ordering = ("-id",)

    def __str__(self):
        return self.name

class ResumeModel(models.Model):
    # personal info
    vacancy_name = models.CharField("Müraciət edilən vakansiyanın adı", max_length=528)
    full_name = models.CharField("Soyad, ad, ata adı", max_length=528)
    email = models.EmailField("Email", max_length=256)
    birthdate = models.CharField("Doğum tarixi", max_length=256)
    subject = models.CharField("Tədris etmək istənilən fənn", max_length=528)
    home_phone = models.CharField("Ev telefon nömrəsi", max_length=50)
    mobile_phone = models.CharField("Mobil nömrə", max_length=50)
    address = models.CharField("Ünvan", max_length=528)
    

    # work experience
    work_start_end_time1 = models.CharField("İşlədiyi başlanğıc və son tarixlər 1", max_length=528, blank=True, null=True)
    company_name1 = models.CharField("Şirkətin adı, ünvanı və fəaliyyət göstərdiyi sahə 1", max_length=2048, blank=True, null=True)
    duty1 = models.CharField("Vəzifə və əsas öhdəliklər 1", max_length=2048, blank=True, null=True)
    leaving_reason1 = models.CharField("Tərk etmə səbəbi 1", max_length=2048, blank=True, null=True)

    work_start_end_time2 = models.CharField("İşlədiyi başlanğıc və son tarixlər 2", max_length=528, blank=True, null=True)
    company_name2 = models.CharField("Şirkətin adı, ünvanı və fəaliyyət göstərdiyi sahə 2", max_length=2048, blank=True, null=True)
    duty2 = models.CharField("Vəzifə və əsas öhdəliklər 2", max_length=2048, blank=True, null=True)
    leaving_reason2 = models.CharField("Tərk etmə səbəbi 2", max_length=2048, blank=True, null=True)

    work_start_end_time3 = models.CharField("İşlədiyi başlanğıc və son tarixlər 3", max_length=528, blank=True, null=True)
    company_name3 = models.CharField("Şirkətin adı, ünvanı və fəaliyyət göstərdiyi sahə 3", max_length=2048, blank=True, null=True)
    duty3 = models.CharField("Vəzifə və əsas öhdəliklər 3", max_length=2048, blank=True, null=True)
    leaving_reason3 = models.CharField("Tərk etmə səbəbi 3", max_length=2048, blank=True, null=True)

    # education
    ed_start_end_time1 = models.CharField("Təhsil aldığı başlanğıc və son tarix 1", max_length=528, blank=True, null=True)
    university1 = models.CharField("Universitet 1", max_length=528, blank=True, null=True)
    speciality1 = models.CharField("İxtisas və dərəcə 1", max_length=528, blank=True, null=True)
    result1 = models.CharField("Nəticə/Qiymət ortalaması 1", max_length=528, blank=True, null=True)

    ed_start_end_time2 = models.CharField("Təhsil aldığı başlanğıc və son tarix 2", max_length=528, blank=True, null=True)
    university2 = models.CharField("Universitet 2", max_length=528, blank=True, null=True)
    speciality2 = models.CharField("İxtisas və dərəcə 2", max_length=528, blank=True, null=True)
    result2 = models.CharField("Nəticə/Qiymət ortalaması 2", max_length=528, blank=True, null=True)

    ed_start_end_time3 = models.CharField("Təhsil aldığı başlanğıc və son tarix 3", max_length=528, blank=True, null=True)
    university3 = models.CharField("Universitet 3", max_length=528, blank=True, null=True)
    speciality3 = models.CharField("İxtisas və dərəcə 3", max_length=528, blank=True, null=True)
    result3 = models.CharField("Nəticə/Qiymət ortalaması 3", max_length=50, blank=True, null=True)

    # certificates, trainings, seminars
    ce_start_end_time1 = models.CharField("İştirak tarixi: başlanğıc və son tarix 1", max_length=528, blank=True, null=True)
    qualification1 = models.CharField("Kvalifikasiya 1", max_length=528, blank=True, null=True)
    place1 = models.CharField("Keçirildiyi məkan 1", max_length=528, blank=True, null=True)
    success1 = models.CharField("Əldə etdiyi nailiyyət 1", max_length=528, blank=True, null=True)

    ce_start_end_time2 = models.CharField("İştirak tarixi: başlanğıc və son tarix 2", max_length=528, blank=True, null=True)
    qualification2 = models.CharField("Kvalifikasiya 2", max_length=528, blank=True, null=True)
    place2 = models.CharField("Keçirildiyi məkan 2", max_length=528, blank=True, null=True)
    success2 = models.CharField("Əldə etdiyi nailiyyət 2", max_length=528, blank=True, null=True)

    ce_start_end_time3 = models.CharField("İştirak tarixi: başlanğıc və son tarix 3", max_length=528, blank=True, null=True)
    qualification3 = models.CharField("Kvalifikasiya 3", max_length=528, blank=True, null=True)
    place3 = models.CharField("Keçirildiyi məkan 3", max_length=528, blank=True, null=True)
    success3 = models.CharField("Əldə etdiyi nailiyyət 3", max_length=528, blank=True, null=True)

    # other successes
    other_successes = models.TextField("Digər nailiyyətlər", blank=True, null=True)

    # references
    reference_full_name1 = models.CharField("Soyad, adı, ata adı 1", max_length=528, blank=True, null=True)
    phone_number1 = models.CharField("Mobil nömrə 1", max_length=50, blank=True, null=True)
    relation1 = models.CharField("Əlaqə 1", max_length=528, blank=True, null=True)

    reference_full_name2 = models.CharField("Soyad, adı, ata adı 2", max_length=528, blank=True, null=True)
    phone_number2 = models.CharField("Mobil nömrə 2", max_length=50, blank=True, null=True)
    relation2 = models.CharField("Əlaqə 2", max_length=528, blank=True, null=True)

    class Meta:
        verbose_name = "CV"
        verbose_name_plural = "CVlər"
        ordering = ("-id",)

    def __str__(self):
        return self.full_name

class ContactModel(models.Model):
    name = models.CharField("Ad", max_length=100)
    email = models.EmailField("Email", max_length=256)
    subject = models.CharField("Mövzu", max_length=256)
    message = models.TextField("Mesaj")

    class Meta:
        verbose_name = "Mesaj"
        verbose_name_plural = "Mesajlar"
        ordering = ("-id",)

    def __str__(self):
        return self.name

class OnlineRegister(models.Model):
    full_name = models.CharField("Ad, soyad", max_length=100)
    email = models.EmailField("Email", max_length=256)
    mobile_number = models.CharField("Mobil nömrə", max_length=50)
    school = models.CharField("Təhsil aldığı məktəb", max_length=528)
    university = models.CharField("Bitirdiyi universitet", max_length=528)
    speciality = models.CharField("İxtisas", max_length=528)
    identity_card_number = models.CharField("Şəxsiyyət vəsiqəsinin nömrəsi", max_length=50, blank=True, null=True)
    point = models.CharField("Qəbul balı", max_length=100)

    class Meta:
        verbose_name = "Kursa onlayn qeydiyyat"
        verbose_name_plural = "Kursa onlayn qeydiyyatlar"
        ordering = ("-id",)

    def __str__(self):
        return self.full_name

class EditionModel(models.Model):
    title = models.CharField("Başlıq", max_length=2048)
    image = models.ImageField("Şəkil", upload_to="edition_images/", blank=True, null=True)
    content = models.TextField("Məzmun", blank=True, null=True)
    is_active = models.BooleanField("Status", default=False)

    class Meta:
        verbose_name = "Nəşr"
        verbose_name_plural = "Nəşrlərimiz"
        ordering = ("-id",)

    def __str__(self):
        return self.title