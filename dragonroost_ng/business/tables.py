import django_tables2 as tables

from dragonroost_ng.business.models import Location
from dragonroost_ng.business.models import Meeting


class LocationListTable(tables.Table):
    name = tables.TemplateColumn(
        """
        <a href=\"{% url 'business:location_detail' record.id %}\">
        {{record.name}}</a>
        """,
    )

    class Meta:
        model = Location
        fields = ("name", "description")


class MeetingListTable(tables.Table):
    title = tables.TemplateColumn(
        """
        <a href=\"{% url 'business:meeting_update' record.id %}\">
        {{record.title}}</a>
        """,
    )

    class Meta:
        model = Meeting
        fields = ("title", "date", "minutes")
