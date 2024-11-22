from django.contrib import admin

from .models import Animal
from .models import MedicalRecord
from .models import Species

# Register your models here.
admin.site.register(Species)
admin.site.register(MedicalRecord)


@admin.register(Animal)
class AnimalAdmin(admin.ModelAdmin):
    list_display = ["name", "starting_weight", "species", "location"]
