from django.db import models
import os


def flag_image_upload_path(instance, filename):
    path = 'flag/{country}'.format(country=instance.name)
    return os.path.join(path, filename)


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class CountryInfo(BaseModel):
    '''
    Country information model. Due to lots of variation in Language I ignore to create separate table.
    For "timezone" field we can create separate table as a Foreignkey relation to make normalized DB,
    But for the shortage of time and as there is no scope to get thousands of rows data, i'm skipping normalization part.
    '''
    name = models.CharField(max_length=50, null=False, blank=False, db_index=True, unique=True)
    alphacode2 = models.CharField(max_length=3,null=True, blank=True, db_index=True)
    alphacode3 = models.CharField(max_length=4,null=True, blank=True, db_index=True)
    capital = models.CharField(max_length=25,null=True, blank=True)
    population = models.PositiveIntegerField(null=True, blank=True)
    timezone = models.JSONField(blank=True, null=True)
    flag = models.ImageField(upload_to=flag_image_upload_path, blank=True, null=True)
    languages = models.JSONField(blank=True, null=True)
    neighbouring_countries = models.JSONField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Counties"
