from django.conf.urls import url
from angels import views

urlpatterns = [
    url(r'^home/$', views.home, name='home'),
]
