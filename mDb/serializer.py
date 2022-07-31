from rest_framework.response import Response
from rest_framework import serializers
from .models import movie_data


class Movies_View_Serializer(serializers.ModelSerializer):

    class Meta:
        model = movie_data
        fields = ('__all__')