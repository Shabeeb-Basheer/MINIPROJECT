from django.conf.urls import url
from facilities import views

urlpatterns=[
    url('pst/',views.post),
    url('viw/',views.view),
    url('user/', views.user),
    url('aprv/(?P<idd>\w+)', views.approv, name='apr'),
    url('rjt/(?P<idd>\w+)', views.rejec, name='re')
]