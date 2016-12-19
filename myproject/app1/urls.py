from django.conf.urls import url
from app1 import views

urlpatterns = [
url(r'^snippets/$',views.SnippetList.as_view()),
url(r'^snippets/(?P<pk>[0-9]+)/$', views.SnippetDetail.as_view()),
]

