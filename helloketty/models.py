# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
# python manage.py inspectdb --database=default > models.py
# python manage.py migrate --database=django_db


from django.db import models


class Bitest(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True )

    class Meta:
        managed = False
        db_table = 'bitest'


class Ha(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'ha'


class Hadhod(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(unique=True, max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hadhod'


class Hell(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    date_field = models.DateField(db_column='date_', blank=True, null=True)  # Field renamed because it ended with '_'.
    date_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hell'


class Product(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    created_at = models.TimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product'


class SalesData(models.Model):
    date = models.DateField()
    product = models.TextField()
    salesperson = models.TextField()
    revenue = models.DecimalField(max_digits=65535, decimal_places=65535)

    class Meta:
        managed = False
        db_table = 'sales_data'


class TestAbsenceDate001(models.Model):
    abdate = models.DateField(blank=True, null=True)
    grade = models.IntegerField(blank=True, null=True)
    student_name = models.CharField(max_length=100, blank=True, null=True)
    department = models.IntegerField(blank=True, null=True)
    branch = models.CharField(max_length=250, blank=True, null=True)
    code = models.IntegerField(blank=True, null=True)
    cls = models.CharField(max_length=50, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'test_absence_date001'


class Testt(models.Model):
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'testt'


class Testtt(models.Model):
    is_paid = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'testtt'


class Users(models.Model):
    username = models.CharField(max_length=50, blank=True, null=True)
    password = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'
