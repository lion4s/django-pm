from django.urls import path

from . import views
from django.urls import path,include
urlpatterns = [
    path('', views.ProjectListViews.as_view(),name='Project_list'),
    path('projects/create', views.ProjrctsCreateViews.as_view(), name='Project_create'),

]
