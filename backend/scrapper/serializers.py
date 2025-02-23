from rest_framework import serializers
from .models import ScrappedModel

class ScrapeSerializer(serializers.ModelSerializer):
  class Meta:
    model = ScrappedModel
    fields = '__all__'

class ScrapeRequestSerializer(serializers.Serializer):
  url = serializers.URLField()