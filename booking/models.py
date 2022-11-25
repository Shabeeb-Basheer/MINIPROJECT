from django.db import models
from services.models import Services
from facilities.models import Facilities
from packages.models import Packages
from register_user.models import RegisterUser

# Create your models here.
class Booking(models.Model):
    booking_id = models.AutoField(primary_key=True)
    # user_id = models.IntegerField()
    user=models.ForeignKey(RegisterUser,to_field='user_id', on_delete=models.CASCADE)
    # service_id = models.IntegerField()
    # service = models.ForeignKey(Services, to_field='service_id', on_delete=models.CASCADE)
    # package_id = models.IntegerField()
    package = models.ForeignKey(Packages, to_field='package_id', on_delete=models.CASCADE)
    date = models.CharField(max_length=30)
    status = models.CharField(max_length=30)
    owner_status = models.CharField(max_length=65)
    ac_status = models.CharField(max_length=76)
    time_status = models.CharField(max_length=43)
    no_of_people = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'booking'
