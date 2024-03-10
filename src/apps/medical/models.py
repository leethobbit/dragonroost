from django.db import models

# Create your models here.

# class Treatment
class Treatment(models.Model):

    name = models.CharField(max_length=80,null=False, unique=True)
    description = models.TextField(blank=True, null=False, default='')
    cost = models.DecimalField(max_digits=6, decimal_places=2, default=5.00)

    class Meta:
        db_table_comment = "Holds information about kinds of treatments."

    def __str__(self):
        return self.name

# class Vaccine
class Vaccine(models.Model):

    name = models.CharField(max_length=80,null=False, unique=True)
    description = models.TextField(blank=True, null=False, default='')
    cost = models.DecimalField(max_digits=6, decimal_places=2, default=5.00)

    class Meta:
        db_table_comment = "Holds information about kinds of vaccines."

    def __str__(self):
        return self.name

# class Diagnosis