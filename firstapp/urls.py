from django.conf.urls import url,patterns
from firstapp.views import *

urlpatterns = [
	url(r'^clothing/',front,name='front'),
	url(r'^chose/',home,name='home'),
	url(r'^home/',homepage,name='homepage'),
	url(r'^placeorder/',createorders,name='orderplace'),
	url(r'^orderplaced/',orderplaced,name='order'),
	url(r'^about/',aboutus,name='aboutus'),
	url(r'^register/',register,name='register'),
	url(r'^tracked/',trackorder,name='track'),
	url(r'^explore/',explore,name='explore'),
]
