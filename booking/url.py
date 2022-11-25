from django.conf.urls import url
from booking import views

urlpatterns=[
    url('pst/',views.post_book),
    url('viw/',views.view),
    url('manage/', views.user),
    url('cancel/(?P<idd>\w+)', views.can, name='ca'),
    url('approve/(?P<idd>\w+)', views.aprve, name='acc'),
    url('re/(?P<idd>\w+)', views.rejct, name='reject'),
    url('quo/(?P<idd>\w+)', views.quation, name='quo'),
]