from django.conf.urls import url
from packages import views

urlpatterns=[
    url('pst/',views.post),
    url('viw/',views.view),
    url('uview/', views.user),
    url('c/(?P<idd>\w+)', views.appr, name='de'),
    url('d/(?P<idd>\w+)', views.rej, name='fe'),
]