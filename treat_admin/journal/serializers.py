# From Two Scoops
from rest_framework import serializers

from .models import Entry

class EntriesSerializer(serializers.ModelSerializer):
	"""docstring for EntrySerializer"""
	class Meta:
			model = Entry
			fields = ('title', 'slug', 'lat', 'lon')

