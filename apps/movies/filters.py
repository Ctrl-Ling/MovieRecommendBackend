# _*_ coding: utf-8 _*_
__author__ = 'Ctrl'
__date__ = '006 18/07/06 下午 03:42:21'

from django.db.models import Q
import django_filters
from .models import *


class MoviesFilter(django_filters.rest_framework.FilterSet):
    #电影分类过滤
    type = django_filters.CharFilter(name='type', lookup_expr='icontains')

    class Meta:
        model = Movies
        fields = ['type',]