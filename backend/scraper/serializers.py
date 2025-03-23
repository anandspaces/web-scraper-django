from rest_framework import serializers
from .models import ScrapedModel

class ScrapeSerializer(serializers.ModelSerializer):
  class Meta:
    model = ScrapedModel
    fields = '__all__'

class ScrapeRequestSerializer(serializers.Serializer):
  url = serializers.URLField()