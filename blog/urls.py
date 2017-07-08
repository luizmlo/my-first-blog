from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
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
    url(r'iamscared', views.rid_8),
    url(r'youarenotalone', views.rid_9),
    url(r'youcanthide', views.rid_10),
    url(r'heisfollowingyou', views.rid_final),
    url(r'retarded', views.retarded),
    url(r'second_stage', views.second_stage),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
