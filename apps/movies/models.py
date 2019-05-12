from django.db import models

# Create your models here.
from datetime import datetime

from django.db import models

class Movies(models.Model):
    """电影"""
    name = models.CharField(default="", max_length=30, verbose_name="电影名", help_text="电影名")
    cover = models.CharField(default="", max_length=400, verbose_name="封面url", help_text="封面url")
    director = models.CharField(default="", max_length=500, verbose_name="导演", help_text="导演")
    actor = models.CharField(default="", max_length=500, verbose_name="主演", help_text="主演")
    type = models.CharField(default="", max_length=50, verbose_name="类型", help_text="类型")
    #country = models.CharField(default="", max_length=50, verbose_name="国家/地区", help_text="国家/地区")
    time = models.CharField(default="", max_length=20, verbose_name="片长(分钟)", help_text="片长")
    grade = models.CharField(default="0.0", max_length=5,verbose_name="评分", help_text="评分")
    desc = models.CharField(default="", max_length=1000, verbose_name="剧情简介", help_text="剧情简介")

    class Meta:
        verbose_name = "电影详情"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Stills(models.Model):
    """剧照"""
    movieid = models.ForeignKey(Movies,on_delete=models.CASCADE,related_name="stills",null=True,blank=True,verbose_name="电影")
    imgurl = models.CharField(default="", max_length=600, verbose_name="剧照url", help_text="剧照url")

    class Meta:
        verbose_name = "电影剧照"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.movieid.name+'剧照'


class Actors(models.Model):
    """剧照"""
    movieid = models.ForeignKey(Movies,on_delete=models.CASCADE,related_name="actors",null=True,blank=True,verbose_name="电影")
    imgurl = models.CharField(default="", max_length=600, verbose_name="演员照片url", help_text="演员照片url")
    name = models.CharField(default="", max_length=100, verbose_name="演员名", help_text="演员名")
    act = models.CharField(default="", max_length=100, verbose_name="饰演角色", help_text="饰演角色")


    class Meta:
        verbose_name = "电影主演"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.movieid.name+'主演'



