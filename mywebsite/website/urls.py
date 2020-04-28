from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('about/', views.AboutPageView.as_view(), name='about'),
    path('projects/', views.ProjectsPageView.as_view(), name='projects'),
    path('wiki/', views.WikiPageView.as_view(), name='wiki'),
    path('blog/', views.BlogPageView.as_view(), name='blog'),
    path('contact/', views.ContactPageView.as_view(), name='contact'),
]