from django.db import models

# Create your models here.
class TimestampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

        # Can be overrided in models that inherit this model
        ordering = ['-created_at', '-updated_at']