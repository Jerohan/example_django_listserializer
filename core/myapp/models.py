from django.db import models
from django.contrib.auth.models import AbstractBaseUser


class Company(models.Model):
    companyid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)

    class Meta:  
        managed = True      
        db_table = 'company'

class Employes(models.Model):
    employeid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)    
    companyid = models.ForeignKey(Company, models.DO_NOTHING, db_column='companyid')
    estatus = models.BooleanField()         # true = activo, false = inactivo

    class Meta:
        managed = True
        db_table = 'employes'
