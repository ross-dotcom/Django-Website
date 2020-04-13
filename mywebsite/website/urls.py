from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('projects/', views.ProjectsPageView.as_view(), name='projects'),
]