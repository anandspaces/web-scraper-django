from rest_framework import serializers
from .models import ScrappedModel

class ScrappedSerializer(serializers.ModelSerializer):
  class Meta:
    model = ScrappedModel
    fields = '__all__'