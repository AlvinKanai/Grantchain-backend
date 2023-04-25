from rest_framework import serializers
from .models import Grant

class GrantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grant
        fields =('title', 'website', 'bounties', 'forum', 'twitter', 'grant_details', 'project_category', 'grant_type', 'main_photo', 'is_published', 'date_added', 'slug')

class GrantDetailSerializer(serializers.Serializer):
    class Meta:
        model = Grant
        fields = '__all__'
        lookup_field = 'slug'