import django_tables2 as tables

from .models import MedicalUpdate


class MedicalUpdateTable(tables.Table):
    title = tables.TemplateColumn(
        """
        <a href=\"{% url 'medical:medical-update-detail' record.id %}\">
        {{record.title}}</a>
        """,
    )

    class Meta:
        model = MedicalUpdate
        fields = ("title", "notes", "q_staff", "date")
        template_name = "tables/bootstrap_htmx.html"
