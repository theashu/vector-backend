from django.db import models


# ------------------Abstract class for created_at and updated_at feilds------------#
class AbstractTime(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

