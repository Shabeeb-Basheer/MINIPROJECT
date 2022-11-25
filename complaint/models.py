from django.db import models
from register_user.models import RegisterUser
# Create your models here.
class Complaint(models.Model):
    complaint_id = models.AutoField(primary_key=True)
    # user_id = models.IntegerField()
    user = models.ForeignKey(RegisterUser, to_field='user_id', on_delete=models.CASCADE)
    complaint = models.CharField(max_length=50)
    reply = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'complaint'
