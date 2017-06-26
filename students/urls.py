from django.conf.urls import url
from . import views

app_name = "student"
urlpatterns = [
    url(r'^$', views.studentList, name="list"),
    url(r'^add/$', views.studentAdd, name="add"),
    url(r'^details/(?P<pk>[0-9]+)/$', views.studentDetail, name="detail"),
]