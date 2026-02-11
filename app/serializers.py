from rest_framework import serializers
from .models import Content

class ContentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Content
        fields = ['id', 'title', 'category', 'created_at']
        read_only_fields = ['id', 'created_at']

    def validate_title(self,value):
        if len(value) < 5:
            raise serializers.ValidationError("Title must be at least 5 characters long.")
        return value
    
    def validate_category(self,value):
        valid_categories = [choice[0] for choice in Content.CATEGORY_CHOICES]
        if value not in valid_categories:
            raise serializers.ValidationError(
                f"Invalid Category. Must be one of: {', '.join(valid_categories)}"
            )
        return value
