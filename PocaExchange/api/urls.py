from django.conf.urls import url
from api import views

urlpatterns = [
    url(r'user/$',views.UserList.as_view()),
    url(r'driftbottle/$',views.DriftBottleList.as_view()),
    url(r'account/login/$',views.AccountLoginView.as_view()),
    url(r'account/logout/$',views.AccountLogoutView.as_view()),
    url(r'account/$',views.AccountDetailView.as_view())
]
