from rest_framework import serializers
from .models import Post, Category


class PostListSerializer(serializers.ModelSerializer):
    class Meta():
        model = Post
        fields = '__all__'

    def to_representation(self, instance):
        return {
            'id': instance.id,
            'title': instance.title,
            'description': instance.description,
            'created': instance.created,
            'category':instance.category.name
        }


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

class CategoryListSerializer(serializers.ModelSerializer):
    class Meta():
        model = Category
        fields = '__all__'
