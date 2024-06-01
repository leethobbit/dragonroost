import django_tables2 as tables
from django.utils.html import format_html

from apps.animals.models import Animal, Species


class AnimalImageColumn(tables.Column):
    def render(self, value):
        return format_html(
            '<img src="/media/{url}" height="60px", width="60px"/>', url=value
        )


class CustomNameColumn(tables.Column):
    def render(self, value):
        return format_html(
            """<a href="{% url 'animals:animal-detail' value.id %}">{{ animal.name }}</a>"""
        )


class AnimalHTMxTable(tables.Table):
    animal_photo = AnimalImageColumn("Photo")

    id = tables.TemplateColumn(
        "<a href=\"{% url 'animals:animal-detail' record.id %}\">{{record.animal_tag}}</a>"
    )
    species = tables.TemplateColumn(
        "<a href=\"{% url 'animals:species-detail' record.species.id %}\">{{record.species.name}}</a>"
    )
    location = tables.TemplateColumn(
        "<a href=\"{% url 'business:location-detail' record.location.id %}\">{{record.location.name}}</a>"
    )

    class Meta:
        model = Animal
        fields = (
            "id",
            "animal_photo",
            "name",
            "description",
            "age",
            "donation_fee",
            "species",
            "location",
            "status",
            "intake_date",
        )
        template_name = "tables/_animal-table-htmx.html"


class SpeciesListTable(tables.Table):
    name = tables.TemplateColumn(
        "<a href=\"{% url 'animals:species-detail' record.id %}\">{{record.name}}</a>",
    )

    class Meta:
        model = Species
        fields = ("name", "diet", "class_name", "description")
