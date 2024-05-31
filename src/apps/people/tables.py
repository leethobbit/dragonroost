import django_tables2 as tables
from django.utils.html import format_html

from apps.people.models import Person

class PersonListTable(tables.Table):
    first_name = tables.TemplateColumn(
        "<a href=\"{% url 'people:person-detail' record.id %}\">{{record.first_name}}</a>",
    )
    class Meta:
        model = Person
        fields = ("first_name", "last_name", "roles", "phone_number")