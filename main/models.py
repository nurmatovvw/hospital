from django.db import models
# from django.db.models.fields.related import ForeignKey
from django.urls import reverse

# Create your models here.
class Hospital(models.Model):
    photo = models.ImageField(upload_to = 'main', null=True, blank=True)
    name = models.CharField('Название',max_length=100) 
    REGION = [
        ('Osh', 'Ошская'),
        ('Chui', 'Чуйская'),
        ('IK', 'Иссык-Кульская'),
        ('Talas', 'Таласская'),
        ('Naryn', 'Нарынская'),
        ('DjA', 'Джалал-Абадская'),
        ('Batken', 'Баткенская'), ]
    region = models.CharField('Область',max_length=9,choices=REGION,default="Osh",)
    ocpo = models.CharField('ОКПО',max_length=4,unique=True)
    gov = models.BooleanField('Государственное',default=False)
    doctors = models.OneToOneField('MainDoctor',on_delete=models.PROTECT,verbose_name='ГлавВрач')
    maxn = models.IntegerField(verbose_name='Макс.количество сотрудников',default=100)


    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Больница'
        verbose_name_plural = 'Больницы'


class MainDoctor(models.Model):
    name = models.CharField('ФИО',max_length=100)
    pin = models.CharField('ПИН',max_length=14)
    birthdate = models.DateField('Дата рождения')
    phone = models.CharField('Номер телефона',max_length=10)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'ГлавВрач'
        verbose_name_plural = 'ГлавВрачи'


class Nurses(models.Model):
    name = models.CharField('ФИО', max_length=255)
    pin = models.CharField('ПИН', max_length=4)
    birthdate = models.DateField('Дата рождения')
    phone = models.CharField('Номер телефона', max_length=10)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Медсестра'
        verbose_name_plural = 'Медсестры'
        
    def get_absolute_url(self):
        return reverse('index') 

class Doctor(models.Model):
    POSITION = [
        ('therapist', 'Терапевт'),
        ('surgeon', 'Хирург')
    ]

    position = models.CharField('Терапевт/Хирург', max_length=255, choices=POSITION, default='therapist',)
    name = models.CharField('ФИО', max_length=255)
    pin = models.CharField('ПИН', max_length=4)
    birthdate = models.DateField('Дата рождения')
    phone = models.CharField('Номер телефона', max_length=10)
    hospital = models.ForeignKey('Hospital', on_delete=models.PROTECT, verbose_name='Больница', default=1)
    nurse = models.ForeignKey('Nurses', on_delete=models.PROTECT, verbose_name='Медсестра')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Лечащий врач'
        verbose_name_plural = 'Лечащие врачи'

    def get_absolute_url(self):
        return reverse('index')
    
class Patients(models.Model):
    name = models.CharField('ФИО', max_length=255)
    pin = models.CharField('ПИН', max_length=4)
    birthdate = models.DateField('Дата рождения')
    phone = models.CharField('Номер телефона', max_length=10)
    reason = models.CharField('Причина обращения в больницу', max_length=255)
    hospital = models.ForeignKey('Hospital', on_delete=models.PROTECT, verbose_name='Больница')
    doctor = models.ForeignKey('Doctor', on_delete=models.PROTECT, verbose_name='Лечащий врач', related_name='counts')
    nurse = models.ForeignKey('Nurses', on_delete=models.PROTECT, verbose_name='Медсестра')



    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Пациент'
        verbose_name_plural = 'Пациенты'

    def get_absolute_url(self):
        return reverse('index') 
