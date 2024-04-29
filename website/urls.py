
from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('logout/', views.logout_user, name='logout'),
    path('login/', views.login_user, name='login'),
    path('register/', views.register_user, name='register'),
    path('delete_trajet/<int:pk>', views.delete_trajet, name='delete_trajet'),
    path('add_trajet/', views.add_trajet, name='add_trajet')
]
