from django.urls import path
from . import views

app_name = 'basic_app'

urlpatterns = [
    path('base/', views.base, name='base'),
    path('register/', views.register, name='register'),
    path('user_login/', views.user_login, name='user_login'),
]