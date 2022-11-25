from django.conf.urls import url
from feedback import views

urlpatterns=[
    url('pst/',views.post),
    url('viw/',views.view)
]