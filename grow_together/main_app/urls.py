from django.urls import include, path
from . import views


urlpatterns = [
    path('accounts/signup/', views.signup, name='signup'),
    path('', views.home, name='home'),
    path('match/', views.match, name='match'),
    path('api/<int:user_id>/add_photo/', views.test, name='add_photo'),

]