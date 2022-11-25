from django.conf.urls import url
from complaint import views

urlpatterns=[
    url('pst/',views.post_comp),
    url('viw/',views.view),
    url('rply/',views.reply),
    url('b/(?P<idd>\w+)', views.b, name='cm')
]