from django.urls import path
from . import views


urlpatterns=[
    
    path('', views.say_hello, name='home-page'),
    path('login', views.login_page, name='login'),
    path('signup', views.signup_page, name='signup')
]