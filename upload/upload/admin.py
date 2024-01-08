from django.contrib import admin
from .models import Photo
from usermanagement.models import Person
admin.site.register(Photo)
admin.site.register(Person)