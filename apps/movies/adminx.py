# _*_ coding: utf-8 _*_
__author__ = 'Ctrl'
__date__ = '006 18/07/06 上午 09:36:15'

import xadmin
from .models import *

class MoviesAdmin(object):
    list_display = ["name", "director","type","time","grade"]
    search_fields = ['name', ]
    list_filter = ["name", "director","type","time","grade"]

class StillsAdmin(object):
    list_display = ["movieid", "imgurl"]


class ActorsAdmin(object):
    list_display = ["movieid", "name","act"]

xadmin.site.register(Movies,MoviesAdmin)
xadmin.site.register(Stills,StillsAdmin)
xadmin.site.register(Actors,ActorsAdmin)