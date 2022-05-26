from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'), # we want the user to be directed at the login page (django magic)
    path('accounts/signup/', views.signup, name='signup'),
    # path('match/', views.match, name='match'),
    path('match/<int:user_id>/', views.upload, name='upload'),
    path('myplants/<int:user_id>/', views.myplants, name='myplants'),
    path('matchedplants/<int:user_id>/', views.matchedplant, name='matchedplant'),
    path('myplants/<int:user_id>/delete', views.deletematch, name='deletematch')
]