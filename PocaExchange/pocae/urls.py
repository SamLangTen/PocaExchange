from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'pairs/$', views.pcpair_list)
]
