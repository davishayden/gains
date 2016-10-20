from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<workout_id>[0-9]+)/$', views.workoutDetail, name='workoutDetail')
]