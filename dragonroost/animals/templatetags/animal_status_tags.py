from django import template
from django.db.models import Count

from dragonroost.animals.models import Animal

register = template.Library()


@register.simple_tag
def status_summary(animals: Animal) -> dict:
    # Group animals by status and count each group
    status_counts = animals.values("status").annotate(count=Count("status")).order_by()

    # Convert the result into a dict: [status: count]
    summary = {item["status"]: item["count"] for item in status_counts}

    return summary  # noqa: RET504
