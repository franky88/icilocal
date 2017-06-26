from django.conf.urls import url
from . import views

app_name = "block"
urlpatterns = [
    url(r'^$', views.blockList, name="list"),
    url(r'^block/(?P<pk>[0-9]+)/$', views.blockDetail, name="detail"),
]