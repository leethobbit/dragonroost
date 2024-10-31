import django_tables2 as tables

from dragonroost.business.models import Location
from dragonroost.business.models import Meeting


class LocationListTable(tables.Table):
    name = tables.TemplateColumn(
        """
        <a href=\"{% url 'business:location-detail' record.id %}\">
        {{record.name}}</a>
        """,
    )

    class Meta:
        model = Location
        fields = ("name", "description")
        template_name = "tables/bootstrap_htmx.html"


class MeetingListTable(tables.Table):
    title = tables.TemplateColumn(
        """
        <a href=\"{% url 'business:meeting-update' record.id %}\">
        {{record.title}}</a>
        """,
    )

    meeting_url = tables.TemplateColumn(
        """
        <a href=\"{{record.meeting_url}}\" target='_blank'>{{record.meeting_url}}</a>
        """,
    )

    class Meta:
        model = Meeting
        fields = ("title", "date", "meeting_url", "minutes")
        template_name = "tables/bootstrap_htmx.html"
