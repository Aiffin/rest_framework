from django.conf.urls import url
from app2 import views


urlpatterns = [
url(r'^users/$', views.UserList.as_view()),
url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
]