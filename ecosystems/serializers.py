from rest_framework import serializers
from .models import Ecosystem


class EcosystemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ecosystem
        fields = '__all__'