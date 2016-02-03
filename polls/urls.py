from django.conf.urls import url

from . import views

#urls principaux de l'interface utilisateur
urlpatterns = [
    url(r'^$', views.index_student, name='index_student'),
    url(r'^School/$', views.index_school, name='index_school'),
    url(r'^Results/$', views.results, name='results'),
]