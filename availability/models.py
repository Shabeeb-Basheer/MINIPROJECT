from django.db import models

# Create your models here.
class Availability(models.Model):
    a_id = models.AutoField(primary_key=True)
    available_date = models.DateField()
    status = models.CharField(max_length=65)

    class Meta:
        managed = False
        db_table = 'availability'
