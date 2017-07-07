from django.conf.urls import url
from blog import views

urlpatterns = [
    url(r'^$', views.home),
    url(r'1', views.rid_1),
    url(r'tunacan', views.rid_2),
    url(r'macaroun', views.rid_3),
    url(r'chapstick', views.rid_4),
    url(r'pycharm', views.rid_5),
    url(r'mcqueen', views.rid_6),
    url(r'malfacila', views.rid_7),

]
