from django.conf.urls import url
from services import views

urlpatterns=[
    url('pst/',views.post),
    url('viw/',views.view),
    url('userview/',views.user),
    url('app/(?P<idd>\w+)',views.approve,name='aprv'),
    url('rj/(?P<idd>\w+)',views.reject,name='rej')
]