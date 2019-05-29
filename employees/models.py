from django.db import models
import datetime
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from company.models import Branch
# Create your models here.

class Designation(models.Model):
    designation = models.CharField(max_length = 255)

    class Meta:
        verbose_name = "Designation"
        verbose_name_plural = "Designations"

    def __str__(self):
        return self.designation


class Employee(models.Model):
    username = models.CharField(max_length = 255)
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    email = models.CharField(max_length = 255)
    phone = models.CharField(max_length = 255)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE, default = '')
    designation = models.ForeignKey(Designation, on_delete = models.CASCADE)
    address = models.CharField(max_length = 255)
    birth_date = models.DateField(null=True, blank=True)
    joining_date = models.DateField(null=True, blank=True)
    salary = models.IntegerField(null=True, blank=True)
    leaves = models.IntegerField(default = 1, null=True, blank=True)
    photo = models.FileField(null=True, blank=True)

    class Meta:
        verbose_name = 'Employee'
        verbose_name_plural = 'Employees'

    def __str__(self):
        return self.first_name


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default = None)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE, default = '')
    designation = models.ForeignKey(Designation, on_delete=models.CASCADE, default = '')
    birth_date = models.DateField(null=True, blank=True)
    joining_date = models.DateField(null=True, blank=True)
    salary = models.IntegerField(null=True, blank=True)
    leaves = models.IntegerField(default = 1)
    photo = models.FileField(null=True, blank=True)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"

    def __str__(self):
        return self.user.username


class Client(models.Model):
    name = models.CharField(max_length = 255)
    email = models.CharField(max_length = 255)
    phone = models.IntegerField()
    address = models.CharField(max_length = 255)
    city = models.CharField(max_length = 255)
    state = models.CharField(max_length = 255)
    zipcode = models.CharField(max_length = 255)
    country = models.CharField(max_length = 255)
    active = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Client'
        verbose_name_plural = 'Clients'

    def __str__(self):
        return self.name


class Technology(models.Model):
    technology = models.CharField(max_length = 255)

    class Meta:
        verbose_name = "Technology"
        verbose_name_plural = "Technologies"

    def __str__(self):
        return self.technology


class EmployeeAccess(models.Model):
    employee_designation = models.ForeignKey(Designation, on_delete = models.CASCADE)
    access = models.CharField(max_length = 255)

    class Meta:
        verbose_name = "Employee Access"
        verbose_name_plural = "Employee Access"

    # def __str__(self):
    #     return self.employee_designation


class Interview(models.Model):
    GENDER_CHOICES = (
        ("MALE", "Male"),
        ("FEMALE", "Female"),
    )

    STATUS_CHOICES = (
        ('SCHEDULED', 'Scheduled'),
        ('IN PROGRESS', 'In Progress'),
        ('TAKEN', 'Taken'),
        ('REJECTED', 'Rejected'),
        ('SELECTED', 'Selected'),
    )

    name = models.CharField(max_length = 255)
    email = models.CharField(max_length = 255)
    phone = models.IntegerField()
    address = models.CharField(max_length = 255)
    designation = models.ForeignKey(Designation, on_delete = models.CASCADE)
    experience = models.CharField(max_length = 255)
    location = models.CharField(max_length = 255)
    company = models.CharField(max_length = 255)
    gender = models.CharField(max_length = 255, choices = GENDER_CHOICES, default = "MALE")
    date = models.DateField()
    ctc = models.CharField(max_length = 255)
    ectc = models.CharField(max_length = 255)
    resume = models.FileField()
    status = models.CharField(max_length = 255, choices = STATUS_CHOICES, default = "SCHEDULED")


    class Meta:
        verbose_name = "Interview"
        verbose_name_plural = "Interviews"

    def __str__(self):
        return self.name


class Knowledge(models.Model):
    title = models.CharField(max_length = 255)
    platform = models.ForeignKey(Technology, on_delete = models.CASCADE)
    description = models.CharField(max_length = 1000)
    image = models.FileField(null=True, blank=True)
    sourcecode_file = models.FileField(null=True, blank=True)

    class Meta:
        verbose_name = 'Knowledge Entry'
        verbose_name_plural = 'Knowledge Entry'

    def __str__(self):
        return self.title


class PerformanceQuestion(models.Model):
    question = models.CharField(max_length = 500)

    class Meta:
        verbose_name = 'Performance Question'
        verbose_name_plural = 'Performance Questions'

    def __str__(self):
        return self.question


class Project(models.Model):
    title = models.CharField(max_length = 50)
    description = models.CharField(max_length = 500)
    start_date = models.DateField()
    end_date = models.DateField()
    project_files = models.FileField(null=True, blank=True)
    assigned_to = models.CharField(max_length = 500)

    class Meta:
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'
