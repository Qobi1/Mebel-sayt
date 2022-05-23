from rest_framework import serializers

# from app1.models import Category
from app1.models import Category


class CtgSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
