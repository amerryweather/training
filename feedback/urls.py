from django.conf.urls import patterns, url
from feedback import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^add_feedback/', views.add_feedback, name='add_feedback'),
    url(r'^add/(?P<model_name>\w+)/?$', 'tekextensions.views.add_new_model'),
)
