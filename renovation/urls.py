from django.conf.urls import patterns, url
from renovation import views

urlpatterns = patterns('',
	url(r'^$',views.index, name='index'),
	url(r'^list$',views.list, name='list'),
	url(r'^scene/(?P<scene_id>\d+)/$',views.scene_info, name='scene_info')
		
	
)