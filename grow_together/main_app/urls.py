from django.urls import include, path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('api/<int:user_id>/add_photo/', views.test, name='add_photo'),
    path('accounts/signup/', views.signup, name='signup'),
    path('match/', views.match, name='match'),
    path('match/<int:user_id>/', views.upload, name='upload')

]