from django.db import models
from datetime import datetime
from datetime import date
from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils import timezone
from .utils import custom_id

#Jangan lupa register model ke admin site yaa

class UserManager(BaseUserManager):

  def _create_user(self, email, password, is_staff, is_superuser, **extra_fields):
    if not email:
        raise ValueError('Users must have an email address')
    now = timezone.now()
    email = self.normalize_email(email)
    user = self.model(
        email=email,
        is_staff=is_staff, 
        is_active=True,
        is_superuser=is_superuser, 
        last_login=datetime.now(),
        date_joined=date.today(), 
        **extra_fields
    )
    user.set_password(password)
    user.save(using=self._db)
    return user

  def create_user(self, email, password, **extra_fields):
    return self._create_user(email, password, False, False, **extra_fields)

  def create_superuser(self, email, password, **extra_fields):
    user=self._create_user(email, password, True, True, **extra_fields)
    return user

class User(AbstractBaseUser, PermissionsMixin):
    custom_id = models.CharField(primary_key=True, max_length=11, unique=True, default=custom_id)
    email = models.EmailField(max_length=254, unique=True)
    nrp = models.CharField(max_length=10, validators=[RegexValidator(r'^\d{1,10}$')], null=True, blank=True, verbose_name='NRP')
    IMACid =models.CharField(max_length=5, validators=[RegexValidator(r'^\d{1,5}$')]) 
    name = models.CharField(max_length=254, null=True, blank=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    last_login = models.DateTimeField(null=True, blank=True)
    date_joined = models.DateTimeField(null=True, blank=True)
    
    GROUP_CHOICE = (
        ('s', 'Staff'),
        ('m', 'Manager'),
        ('x', 'Member'),
        ('g', 'Guest'),
    )
    
    usergroup = models.CharField(
        max_length=1,
        choices=GROUP_CHOICE,
        blank=True,
        default='g',
        help_text='User Type')
    

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def get_absolute_url(self):
        return "/users/%i/" % (self.pk)

class Instansi(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    INSTANSI_CHOICE = (
        ('i', 'ITS'),
        ('o', 'Non-ITS'),
    )
    JURUSAN_CHOICE = (
        ('oo', 'Non-ITS'),
        ('f', 'Fisika'),
        ('k', 'Kimia'),
        ('m', 'Matematika'),
        ('s', 'Statistika'),
        ('a', 'Aktuaria'),
        ('b', 'Biologi'),
        ('sa', 'Sains Analitik dan Instrumentasi Kimia'),
        ('tm', 'Teknik Mesin'),
        ('tk', 'Teknik Kimia'),
        ('tf', 'Teknik Fisika'),
        ('ti', 'Teknik Sistem dan Industri'),
        ('tm', 'Teknik Material'),
        ('tp', 'Teknik Pangan'),
        ('ts', 'Teknik Sipil'),
        ('ar', 'Arsitektur'),
        ('tl', 'Teknik Lingkungan'),
        ('pw', 'Perencanaan Wilayah dan Kota'),
        ('gm', 'Teknik Geomatika'),
        ('gf', 'Teknik Geofisika'),
        ('tp', 'Teknik Perkapalan'),
        ('sk', 'Teknik Sistem Perkapalan'),
        ('kl', 'Teknik Kelautan'),
        ('la', 'Teknik Transportasi Laut'),
        ('lp', 'Teknik Lepas Pantai'),
        ('ee', 'Teknik Elektro'),
        ('eb', 'Teknik Biomedik'),
        ('ec', 'Teknik Komputer'),
        ('et', 'Teknik Telekomunikasi'),
        ('et', 'Teknologi Kedokteran'),
        ('ei', 'Informatika'),
        ('es', 'Sistem Informasi'),
        ('ex', 'Teknologi Informasi'),
        ('dp', 'Desain Produk'),
        ('di', 'Desain Interior'),
        ('dk', 'Desain Komunikasi Visual'),
        ('mb', 'Manajemen Bisnis'),
        ('sp','Studi Pembangunan'),
        ('4e', 'Teknik Elektro Otomasi'),
        ('4i', 'Teknik Instrumentasi'),
        ('4s', 'Teknik Infrastruktur Sipil'),
        ('4m', 'Teknik Mesin Industri'),
        ('4k', 'Teknik Kimia Industri'),
        ('4s', 'Statistika Bisnis'),
    )

    instansi = models.CharField(
        max_length=1,
        choices=INSTANSI_CHOICE,
        blank=True,
        default='i',
        help_text='Asal Instansi')
    jurusan = models.CharField(max_length=2,
        choices=JURUSAN_CHOICE,
        blank=True,
        default='oo',
        help_text='Asal Jurusan')

class IMACevents(models.Model):
    title = models.CharField(max_length=20, help_text='Masukkan nama event' )
    startregistdate = models.DateField()
    startdate = models.DateTimeField()
    enddate = models.DateTimeField()
    attendee = models.ManyToManyField(User)
    agenda = models.CharField(max_length=1000, help_text='Deskripsi singkat event')

    class Meta:
         verbose_name = "IMAC Event"

class article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    contributor = models.OneToOneField(User,on_delete=models.RESTRICT, default='Anonymous')
    releasedate = models.DateField()

    class Meta:
         verbose_name = "IMAC Article"

#Nama manajer masih ga user friendly di tampilan adminnya, fix soon
class Nama_Manajer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    manajer = models.CharField(max_length=5, null=True, blank=True)

class Divisi(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    DIVISI_CHOICE = (
        ('IR', 'Metallurgy'),
        ('SD', 'Material'),
        ('ER','Mineral'),
        ('RP','Mining'),
        ('WD', 'Extractive'),
        ('CR','Coal'),
        ('MD','Manufacture'),
        ('CC','Excavator'),
        ('FU','Pyrometallurgy'),
        ('SP', 'Blast Furnace'),
    )
    divisi = models.CharField(max_length=2,
        choices=DIVISI_CHOICE,
        blank=True,
        default='oo',
        help_text='Asal Divisi')



