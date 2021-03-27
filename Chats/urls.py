from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('new_user/', views.new_user, name='new_user'),
    path('error/', views.error, name='error'),
]
