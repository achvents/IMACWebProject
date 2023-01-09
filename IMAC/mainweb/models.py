from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime
from datetime import date
from django.conf import settings
from django.core.validators import RegexValidator

class member(AbstractUser):
    id = models.CharField(primary_key=True, max_length=10, validators=[RegexValidator(r'^\d{1,10}$')]) #nrp
    password = models.CharField(max_length=100)
    last_login = models.DateTimeField(default=datetime.now)
    is_superuser = models.BooleanField(null=False) 
    username = models.CharField(max_length=100, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    is_staff = models.BooleanField(null=False)
    is_active = models.BooleanField(default=True, null=False)
    date_joined = models.DateField(default=datetime.now)

class IMACevents(models.Model):
    title = models.CharField(max_length=20, help_text='Masukkan nama event' )
    startregistdate = models.DateField()
    startdate = models.DateTimeField()
    enddate = models.DateTimeField()
    attendee = models.ManyToManyField(settings.AUTH_USER_MODEL,)
    agenda = models.CharField(max_length=1000, help_text='Deskripsi singkat event')

    class Meta:
         verbose_name = "IMAC Event"

class article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    contributor = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,null=True)
    releasedate = models.DateField()

    class Meta:
         verbose_name = "IMAC Article"

