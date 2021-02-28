from django.db import models
import os
from urllib.request import urlopen
from tempfile import NamedTemporaryFile
from django.core.files import File
from django.contrib.postgres.fields import ArrayField


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
    name = models.CharField(max_length=80, null=False, blank=False, db_index=True, unique=True)
    alphacode2 = models.CharField(max_length=3,null=True, blank=True, db_index=True, unique=True)
    alphacode3 = models.CharField(max_length=4,null=True, blank=True, db_index=True, unique=True)
    capital = models.CharField(max_length=25,null=True, blank=True)
    population = models.PositiveIntegerField(null=True, blank=True)
    timezones = ArrayField(ArrayField(models.CharField(max_length=20, blank=True)),size=1,)
    flag_url = models.URLField(blank=True, null=True)
    flag = models.FileField(upload_to='flag', blank=True, null=True)
    languages = models.JSONField(blank=True, null=True)
    neighbouring_countries = ArrayField(ArrayField(models.CharField(max_length=5, blank=True)),size=1,)

    def save(self, *args, **kwargs):
        try:
            if self.flag_url and not self.flag:
                img_temp = NamedTemporaryFile(delete=True)
                img_temp.write(urlopen(self.flag_url).read())
                img_temp.flush()
                file_extention = self.flag_url.split('.')[-1] if self.flag_url.split('.')[-1] else 'svg'
                self.flag.save(f"{self.name}.{file_extention}", File(img_temp))  # alphacode2 can be null thats why using name
            super(CountryInfo, self).save(*args, **kwargs)
        except Exception as ex:
            pass

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Counties"
