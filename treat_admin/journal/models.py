from django.db import models
import datetime

class Entry(models.Model):
    slug = models.SlugField('short name', max_length=48, unique=True)
    title = models.CharField(max_length=64)
    entry_date = models.DateField()
    ordinal = models.IntegerField('sequence in day', null=True, blank=True)
    lat = models.FloatField('latitude')
    lon = models.FloatField('longitude')
    zoom_level = models.IntegerField(default=10)
    is_flippable = models.BooleanField('Allow image flip', default=False)
    entry_text = models.TextField(blank=True, default='')
    interpret_blurb = models.TextField(blank=True, default='')
    interpret_more = models.TextField(blank=True, default='')

    class Meta:
        ordering = ['entry_date', 'ordinal']
