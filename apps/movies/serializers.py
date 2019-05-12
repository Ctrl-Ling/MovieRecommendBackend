# _*_ coding: utf-8 _*_
__author__ = 'Ctrl'
__date__ = '006 18/07/06 上午 09:35:52'

from rest_framework import serializers
from .models import *


class MoviesStillsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stills
        fields = ("imgurl",)


class MoviesActorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actors
        fields = ("imgurl","name","act")


class MoviesSerializer(serializers.ModelSerializer):
    stills = MoviesStillsSerializer(many=True)
    actors = MoviesActorsSerializer(many=True)

    class Meta:
        model = Movies
        fields = "__all__"


class MoviesListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movies
        fields = ("id","cover","name","grade")

