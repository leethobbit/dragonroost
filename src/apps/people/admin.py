from django.contrib import admin

from .models import Person, Role

# Register your models here.
admin.site.register(Person)
admin.site.register(Role)