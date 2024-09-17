from rest_framework.serializers import ModelSerializer
from .models import Ad

class Adserializer(ModelSerializer):
    class Meta:
        model = Ad
        fields = '__all__'