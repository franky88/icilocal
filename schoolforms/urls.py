from django.conf.urls import url
from . import views

app_name = "schoolform"
urlpatterns = [
    url(r'^$', views.schoolFormList, name="list"),
    # url(r'^details/(?P<pk>[0-9]+)/$', views.instructorDetail, name="detail"),
]