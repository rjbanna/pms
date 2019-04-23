from django.db import models
import datetime

from company.models import Branch

# Create your models here.

class Designation(models.Model):
    designation = models.CharField(max_length = 255)

    def __str__(self):
        return self.designation

    class Meta:
        verbose_name = "Designation"
        verbose_name_plural = "Designations"


class Employees(models.Model):
    employee_firstname = models.CharField(max_length = 255, name = 'firstname')
    employee_lastname = models.CharField(max_length = 255, name = 'lastname')
    employee_username = models.CharField(max_length = 255, name = 'username')
    employee_password = models.CharField(max_length = 255, name = 'password')
    employee_email = models.EmailField(max_length = 255, unique = True, name = 'email')
    employee_branch = models.ForeignKey(Branch, on_delete = models.CASCADE, name = 'branch')
    employee_designation = models.ForeignKey(Designation, on_delete = models.CASCADE, name = 'designation')
    employee_birth_date = models.DateField(name = 'birthdate')
    employee_joining_date = models.DateField(name = 'joining date')
    employee_salary = models.IntegerField(name = 'salary')
    employee_leaves = models.IntegerField(name = 'leaves')
    employee_photo = models.FileField(null = True, blank = True, name = 'photo')

    def __str__(self):
        return self.employee_firstname + self.employee_lastname

    class Meta:
        verbose_name = "Employee"
        verbose_name_plural = "Employees"
