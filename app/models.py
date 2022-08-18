from django.db import models


# ------------------Abstract class for created_at and updated_at feilds------------#
class AbstractTime(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class PicturesModel(AbstractTime):
    title = models.CharField(
        "Title", max_length=256
    )
    type = models.CharField(
        "Type", max_length=256
    )
    position = models.IntegerField("Position")
    image = models.FileField(upload_to='images/%Y-%M-%d/',
        null=True,blank=True
    )

    def __str__(self):
        return f"{self.title}"

    class Meta:
        '''docstring for meta'''
        verbose_name_plural = "Picture Detail"
        ordering = ("position",)
