from django.contrib import admin

from .models import Animal
from .models import Breed
from .models import MedicalRecord
from .models import Species

# Register your models here.
admin.site.register(Species)
admin.site.register(MedicalRecord)
admin.site.register(Breed)


@admin.register(Animal)
class AnimalAdmin(admin.ModelAdmin):
    list_display = ["name", "starting_weight", "species", "location"]
