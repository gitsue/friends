from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
	url(r'^addfriend/(?P<user_id>\d+)$',views.addfriend, name="addfriend"),
    url(r'^removefriend/(?P<friend_id>\d+)$',views.removefriend, name="removefriend"),
    url(r'^user/(?P<user_id>\d+)$',views.profilepage, name="profilepage"),    
]
