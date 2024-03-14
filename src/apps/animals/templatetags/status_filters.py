from django import template
from django.db.models import Case, Count, FloatField, When

register = template.Library()


@register.filter
def percent_adopted(animals):
    if animals.exists():
        aggregation = animals.aggregate(
            total=Count("id"), done=Count(Case(When(status="ADOPTED", then=1)))
        )

        percent_adopted = (aggregation["done"] / aggregation["total"]) * 100
        return round(percent_adopted, 2)
    else:
        return 0
