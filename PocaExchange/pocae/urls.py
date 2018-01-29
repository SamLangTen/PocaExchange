from django.conf.urls import url
from pocae import views

urlpatterns = [
    url(r'user/$',views.UserList.as_view()),
    url(r'driftbottle/$',views.DriftBottleList.as_view())
]
