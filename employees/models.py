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

#
# class Employee(models.Model):
#     username = models.CharField(max_length = 255)
#     password = models.PasswordField()
#     firstname = models.CharField(max_length = 255)
#     lastname = models.CharField(max_length = 255)
#     email = models.CharField(max_length = 255)
#     branch = models.ForeignKey(Branch, on_delete=models.CASCADE, default = '')
#     designation = models.ForeignKey(Designation, on_delete=models.CASCADE, default = '')
#     phone = models.IntegerField()
#     address = models.CharField(max_length = 255)
#     city = models.CharField(max_length = 255)
#     state = models.CharField(max_length = 255)
#     zipcode = models.CharField(max_length = 255)
#     country = models.CharField(max_length = 255)
#     active = models.BooleanField(default=True)
#
#     class Meta:
#         verbose_name = 'Client'
#         verbose_name_plural = 'Clients'
#
#     def __str__(self):
#         return self.name
