from django.conf.urls import url
from pocae import views

urlpatterns = [
    url(r'user/$',views.UserList.as_view())
]
