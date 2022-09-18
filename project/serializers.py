from rest_framework import serializers
from .models import Project

#nos permite llamar un modelo especifico
class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        #fields = '__all__'
        fields = ('id', 'title', 'description', 'technology', 'create_at')
        read_only_fields = ('create_at',)
        