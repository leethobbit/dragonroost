import django_tables2 as tables
from django.utils.html import format_html

from dragonroost_ng.animals.models import Animal
from dragonroost_ng.animals.models import Species


def get_status_attr(record):
    """
    Returns a different styling based on the animal status.
    """
    status = record.status
    match status:
        case "ADOPTED":
            return "bg-secondary"
        case "PENDING":
            return "bg-info"
        case "ADOPTABLE":
            return "bg-success"
        case "MEDICAL_HOLD":
            return "bg-warning"
        case _:
            return "bg-secondary"


class AnimalImageColumn(tables.Column):
    def render(self, value):
        return format_html(
            '<img src="/media/{url}" height="60px", width="60px"/>',
            url=value,
        )


class CustomNameColumn(tables.Column):
    def render(self, value):
        return format_html(
            """
            <a href="{% url 'animals:animal-detail' value.id %}">{{ animal.name }}</a>
            """,
        )


class AnimalHTMxTable(tables.Table):
    animal_photo = AnimalImageColumn("Photo")

    id = tables.TemplateColumn(
        """
        <a href=\"{% url 'animals:animal-detail' record.id %}\">
        {{record.animal_tag}}
        </a>
        """,
    )
    species = tables.TemplateColumn(
        """
        <a href=\"{% url 'animals:species-detail' record.species.id %}\">
        {{record.species.name}}
        </a>
        """,
    )
    location = tables.TemplateColumn(
        """<a href=\"{% url 'business:location_detail' record.location.id %}\">
        {{record.location.name}}
        </a>
        """,
    )

    status = tables.Column(
        attrs={"td": {"class": get_status_attr}},
        verbose_name="Status",
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
        template_name = "tables/bootstrap_htmx.html"


class SpeciesListTable(tables.Table):
    name = tables.TemplateColumn(
        """
        <a href=\"{% url 'animals:species-detail' record.id %}\">{{record.name}}</a>
        """,
    )

    class Meta:
        model = Species
        fields = ("name", "diet", "class_name", "description")
