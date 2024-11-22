from django.contrib import admin

from .models import Person
from .models import Role


# Register your models here.
@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ["name", "description"]


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name", "notes"]
