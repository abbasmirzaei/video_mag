from django.urls import path
from . import views


urlpatterns = [
	path('' ,views.homepage , name='homepage'),
	path('catagory.html/' ,views.catagory , name='catagory'),
	path('contact.html/' ,views.contact , name='contact'),
	path('single-post.html/' ,views.single , name='single-post'),
	path('video-post.html/' ,views.video , name='video-post'),
]
