# From Two Scoops
from rest_framework import serializers

from .models import Entry

class EntriesSerializer(serializers.ModelSerializer):
	"""docstring for EntrySerializer"""
	entry_date = serializers.DateField(format="%d %B, %Y", input_formats=['%d-%m-%Y', 'iso-8601'])
	class Meta:
			model = Entry
			fields = ('title', 'slug', 'entry_date', 'lat', 'lon', 'zoom_level', 'is_flippable', 'entry_text')

