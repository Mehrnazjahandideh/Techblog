from django.urls import path
from .views import register,reset


urlpatterns = [
       path('',register,name='signup'),
       path('password _reset_confirm',reset,name='password_reset_confirm'),
              # path('logout/',custom_logout, name='logout'),

       
       
]