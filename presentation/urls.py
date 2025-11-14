from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('mvt/', views.mvt, name='mvt'),
    path('orm/', views.orm, name='orm'),
    path('templates/', views.templates_demo, name='templates_demo'),
    path('security/', views.security, name='security'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('api/', views.api_intro, name='api_intro'),
    path('conclusion/', views.conclusion, name='conclusion'),
    path('articles/', views.article_list, name='article_list'),
    path('api/articles/', views.api_articles, name='api_articles'),
    path('api/stats/', views.api_stats, name='api_stats'),
]