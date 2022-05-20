from django.urls import include, path
from . import views


urlpatterns = [
    path('accounts/signup/', views.signup, name='signup'),
    path('', views.home, name='home'),
    path('match/', views.match, name='match')
]