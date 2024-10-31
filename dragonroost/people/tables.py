import django_tables2 as tables

from dragonroost.people.models import Person


class PersonHTMxTable(tables.Table):
    first_name = tables.TemplateColumn(
        """
        <a href=\"{% url 'people:person-detail' record.id %}\">
        {{record.first_name}}</a>
        """,
    )

    class Meta:
        model = Person
        template_name = "tables/bootstrap_htmx.html"
        fields = ("first_name", "last_name", "roles", "phone_number", "notes")
