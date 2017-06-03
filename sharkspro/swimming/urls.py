from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^home/$', views.home, name='home'),
	url(r'^accomplishments/$', views.accomplishments, name='accomplishments'),
	url(r'^about/$', views.about, name='about'),
	url(r'^safetymeasures/$', views.safetymeasures, name='safetymeasures'),
	url(r'^contact/$', views.contact, name='contact'),
	url(r'^reviews/$', views.reviews, name = 'reviews'),
	url(r'^gallery/$', views.gallery, name = 'gallery'),
]
