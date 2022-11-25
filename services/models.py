from django.db import models

# Create your models here.
class Services(models.Model):
    service_id = models.AutoField(primary_key=True)
    service_name = models.CharField(max_length=30)
    description = models.CharField(max_length=50)
    status = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'services'
