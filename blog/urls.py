from django.conf.urls import url
from blog import views

urlpatterns = [
    url(r'^$', views.post_list),
    url(r'1', views.rid_1),
    url(r'tunacan', views.rid_2),
    url(r'macaroun', views.rid_3),
]
