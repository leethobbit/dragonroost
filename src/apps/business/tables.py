import django_tables2 as tables
from django.utils.html import format_html

from apps.business.models import Location, Meeting

class LocationListTable(tables.Table):
    name = tables.TemplateColumn(
        "<a href=\"{% url 'business:location-detail' record.id %}\">{{record.name}}</a>",
    )
    class Meta:
        model = Location
        fields = ("name", "description")

class MeetingListTable(tables.Table):
    title = tables.TemplateColumn(
        "<a href=\"{% url 'business:meeting-detail' record.id %}\">{{record.title}}</a>",
    )
    class Meta:
        model = Meeting
        fields = ("title", "date", "minutes")