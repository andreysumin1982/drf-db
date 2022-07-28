# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
#
class Brand(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'brand'
#
class Model(models.Model):
    id_brand = models.ForeignKey(Brand, models.DO_NOTHING, db_column='id_brand')
    name = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'model'
