"""MovieRecommend2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
import xadmin
from rest_framework.documentation import include_docs_urls
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views
from rest_framework_jwt.views import obtain_jwt_token
from django.views.static import serve

from movies.views import *

router = DefaultRouter()
router.register(r'movies', MoviesViewSet,base_name="movies")


urlpatterns = [
    path('xadmin/', xadmin.site.urls),
    #路由配置
    url(r'^', include(router.urls)),

    # path('goods/',goods_list,name="goods-lists"),
    path('docs/',include_docs_urls(title='电影推荐')),
    url(r'^api-auth/', include('rest_framework.urls')),
    #drf自带的token认证模式
    url(r'^api-token-auth/', views.obtain_auth_token),#token的url
    #jwt的认证接口
    url(r'^login/', obtain_jwt_token),
]
