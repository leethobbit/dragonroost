from django.contrib import admin

from .models import Feedback
from .models import Location
from .models import Meeting

# Register your models here.
admin.site.register(Location)
admin.site.register(Meeting)


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ["name", "email_address", "feedback_type", "feedback"]
