from django.db import models

# Create your models here.
class Packages(models.Model):
    package_id = models.AutoField(primary_key=True)
    package_name = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
    description = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'packages'
