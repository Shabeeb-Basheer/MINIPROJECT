from django.conf.urls import url
from temp import views



urlpatterns=[
    url('adm/',views.admin),
    url('usr/',views.user),
    url('frm/',views.form),
]