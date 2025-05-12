from .models import reminder
from rest_framework import serializers

class RemSerializer(serializers.ModelSerializer):
    class Meta:
        model = reminder
        fields = ['id', 'rem_type', 'message', 'rem_date']