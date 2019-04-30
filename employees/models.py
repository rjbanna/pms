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
