from django.db import models

# Create your models here.
class Quotation(models.Model):
    quotation_id = models.AutoField(primary_key=True)
    quotation_name = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
    user_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'quotation'
