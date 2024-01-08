from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.response import Response
from .models import Photo
from usermanagement.models import Person
from .serializer import photoserializer
from rest_framework.parsers import FileUploadParser
from . import views

import jwt

from rest_framework.decorators import APIView
from rest_framework import generics

class ApiPhoto(generics.CreateAPIView):
    queryset = Photo.objects.all()
    serializer_class = photoserializer

class GetPhoto(APIView):
    def post(self,request):
        token=request.data['token']
        try:
            payload=jwt.decode(token,'secret',algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            return Response({"message":"token expired try login in"})
        id=payload['id']
        owner=Person.objects.filter(id=id).first()
        if owner is None:
            return Response({"message":"no user found"})
        else:
            try:
                photo=Photo.objects.filter(owner=owner).last()
                seri=photoserializer(photo)
                return Response({"message":"successfully fetched","photo":seri.data})
            except:
                return Response({"message":"user has no photo"})
            

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name="homepage"),
    path('profilephoto/upload',ApiPhoto.as_view(),name='api'),
    path('profilephoto/get',GetPhoto.as_view(),name='get'),
    path('user/',include('usermanagement.urls')),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
