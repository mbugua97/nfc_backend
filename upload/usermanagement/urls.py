from django.urls import path
from .views import GetPerson,Deleteuser,UpdateUser,LoginUser
urlpatterns=[
    path('register',GetPerson.as_view(),name='getpostperson'),
    path('deregister',Deleteuser.as_view(),name='deleteuser'),
    path('update',UpdateUser.as_view(),name="updateuser"),
    path('login',LoginUser.as_view(),name='loginuser')
]