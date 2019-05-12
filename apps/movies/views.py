from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import mixins
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

from .models import *
from .serializers import *
from .filters import *

class MoviesViewSet(viewsets.ModelViewSet):
    queryset = Movies.objects.all()
    serializer_class = MoviesSerializer
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    filter_class = MoviesFilter
    search_fields = ('name','director','actor')

    def get_serializer_class(self):
        if self.action == "list":
            return MoviesListSerializer
        return MoviesSerializer