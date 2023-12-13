from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name="home"),
    # path('myform', myForm, name='myform'),
    path('news', news, name='news'),
    path('appointment', appointment, name='appointment'),
    path('user_info',user_info,name='user_info')
    # path('users',user,name= "user"),
]
