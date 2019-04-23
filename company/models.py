from django.db import models

# Create your models here.
class Branch(models.Model):
    branch_name = models.CharField(max_length = 255)

    def __str__(self):
        return self.branch_name

    class Meta:
        verbose_name = "Branch"
        verbose_name_plural = "Branches"
