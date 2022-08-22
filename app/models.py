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
    position = models.IntegerField('Position', editable=True)
    image = models.FileField(upload_to='images/%Y-%M-%d/',
        null=True,blank=True
    )

    def save(self, *args, **kwargs):
        max_data = PicturesModel.objects.aggregate(Max('position'))
        if max_data['position__max'] >= 0:
            max_value = max_data['position__max'] + 1
        else:
            max_value = 0
        self.position = max_value
        super(PicturesModel, self).save(*args, **kwargs)

        
    def __str__(self):
        return f"{self.title}"

    class Meta:
        '''docstring for meta'''
        verbose_name_plural = "Picture Detail"
        ordering = ("position",)
