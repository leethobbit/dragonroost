from django.db import models


class AnimalQuerySet(models.QuerySet):
    def get_available_animals(self):
        return self.filter(status="AVAILABLE")

    def get_animals_needing_medical_attention(self):
        """
        Return a QuerySet of Animal objects that need medical attention,
        i.e. where the status is "MEDICAL_HOLD".
        """

        return self.filter(status="QUARANTINE")
