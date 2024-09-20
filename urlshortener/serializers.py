from rest_framework.serializers import ModelSerializer
from .models import *


class UrlSerializer(ModelSerializer):
    class Meta:
        model = URL
        fields = '__all__'
        read_only_fields = ['key', 'short_url']
