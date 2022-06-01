from django.db import models

# Create your models here.


class User(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birth_date = models.DateField()
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    zip_code = models.PositiveIntegerField(null=True)
    landline = models.CharField(max_length=50)
    cellular_phone = models.CharField(max_length=50)
    is_covid_19_infected = models.BooleanField()
    have_diabetes = models.BooleanField()
    have_cardio_problems = models.BooleanField()
    have_allergies = models.BooleanField()
    have_other_medical_conditions = models.CharField(max_length=512, null=True)
