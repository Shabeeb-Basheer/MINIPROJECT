from django.db import models

# Create your models here.
class RegisterUser(models.Model):
    user_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    age = models.CharField(max_length=30)
    gender = models.CharField(max_length=30)
    address = models.CharField(max_length=30)
    place = models.CharField(max_length=30)
    mobile_number = models.IntegerField()
    email = models.CharField(max_length=30)
    password = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'register_user'
