from django.conf.urls import url
from availability import views

urlpatterns=[
    url('a/',views.a),
    url('v/',views.v),
    # url('rply/',views.reply),
    url(r'^b/(?P<idd>\w+)', views.book, name='book')
]