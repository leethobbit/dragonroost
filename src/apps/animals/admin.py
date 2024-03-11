from django.contrib import admin

from .models import Animal, Species, Status


# Register your models here.
class AnimalAdmin(admin.ModelAdmin):
    """
    This customized admin view makes reviewing things in the site easier - make more of these!
    """
    list_display = ('name', 'description', 'status', 'species', 'age', 'donation_fee')
    list_filter = ('status',)

admin.site.register(Animal, AnimalAdmin)
admin.site.register(Species)
admin.site.register(Status)