from enum import Enum
from statistics import mode

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
from IncredibleBondsAPI import settings
"""
https://simpleisbetterthancomplex.com/tutorial/2018/01/18/how-to-implement-multiple-user-types-with-django.html
"""
# Create your models here.


class Profile(AbstractUser):
    blood_groups = (
        (1, 'A+'),
        (2, 'A-'),
        (3, 'B+'),
        (4, 'B-'),
        (5, 'O+'),
        (6, 'O-'),
        (7, 'AB+'),
        (8, 'AB-'),
        (9, 'Bombay Group')
    )
    is_doctor = models.BooleanField(default=False)
    is_patient = models.BooleanField(default=False)
    is_parent = models.BooleanField(default=False)
    gender = models.CharField(max_length=6, choices=(("Male","Male"),("Female","Female")))
    blood_group = models.IntegerField(default=1, choices=blood_groups)
    date_of_birth = models.DateField(default=timezone.now)
    phone_Number = models.CharField(max_length=15)
    state = models.CharField(max_length=20)
    district = models.CharField(max_length=20)
    city = models.CharField(max_length=40)


class FactorDeficiencies(Enum):
    Factor_I = 1,
    Factor_II = 2,
    Factor_V = 5,
    Factor_VII = 7,
    Factor_VIII = 8,
    Factor_IX = 9,
    Factor_X = 10,
    Factor_XI = 11,
    Factor_XII = 12,
    Factor_XIII = 13,
    Von_Willebrand = 100,


class Severity(models.Model):
    Name = models.CharField(max_length=20)
    Max_Factor_Level = models.IntegerField()
    Min_Factor_Level = models.IntegerField()


class FactorManufacture(models.Model):
    Name = models.CharField(max_length=100)
    Url = models.CharField(max_length=400)


class Hemophilia(models.Model):
    Name = models.CharField(max_length=20)
    Other_Names = models.TextField(default=None)
    Factor_Deficiency = models.IntegerField(unique=True)
    Description = models.TextField(max_length=400,default=None)
    Diagnosis = models.TextField(default=None)
    Treatment = models.TextField(default=None)
    Symptoms = models.TextField(default=None)
    Dosage_denominator = models.IntegerField(default=1)

    def __unicode__(self):
        return self.Name

    def __str__(self):
        return self.Name


class Patient(models.Model):
    user = models.OneToOneField(Profile, on_delete=models.CASCADE)
    factor = models.ForeignKey(Hemophilia, on_delete=models.CASCADE)
    weight = models.IntegerField()
    factor_level = models.DecimalField(decimal_places=2, max_digits=10)
    inhibitor_Status = models.BooleanField()
    family_History = models.BooleanField()

    def __unicode__(self):
        return self.user.get_full_name()

    def __str__(self):
        return self.user.get_full_name()


class Doctor(models.Model):
    user = models.OneToOneField(Profile, on_delete=models.CASCADE)
    specialt = models.CharField(max_length=30)

    def __unicode__(self):
        return self.user.get_full_name()

    def __str__(self):
        return self.user.get_full_name()


class Parent(models.Model):
    user = models.OneToOneField(Profile, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, default=None)
    relation_Ship = models.IntegerField(blank=False, choices=((1, "Father"), (2, "Mother"), (3, "Guardian")))

    def __unicode__(self):
        return self.user.get_full_name()

    def __str__(self):
        return self.user.get_full_name()


class Hospital(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=30)
    district = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=20)
    latitude = models.DecimalField(decimal_places=20, max_digits=25)
    longitude = models.DecimalField(decimal_places=20, max_digits=25)


class InfusionLog(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    factor_manufacture = models.ForeignKey(FactorManufacture, on_delete=models.CASCADE)
    batch_number = models.CharField(max_length=15)
    date = models.DateTimeField(auto_now=True)
    reason = models.CharField(max_length=100)
    place_of_bleeding = models.CharField(max_length=30)
    units = models.IntegerField()
    photo = models.ImageField()


class BleedLog(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
