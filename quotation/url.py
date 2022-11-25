from django.conf.urls import url
from quotation import views

urlpatterns=[
    url('viw/',views.view),
    url('pst/',views.post),
    url('adv/',views.mm),
    url('f/(?P<idd>\w+)',views.app,name='qe'),
    url('g/(?P<idd>\w+)',views.re,name='qre'),
]