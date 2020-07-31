from django.urls import path
from . import views
app_name = 'natural_disasters'
urlpatterns = [
    # path('', views.test, name='index'), #+ 新增一个新的URL
    path('home', views.home, name='home'),
    path('history', views.history, name='history'),
    path('detail', views.detail, name='detail'),
    path('statistical', views.statistical, name='statistical'),

    path('map_', views.map_, name='map_'),
    path('map_2', views.map_2, name='map_2'),
    path('map_3', views.map_3, name='map_3'),

    path('map_1_collect', views.map_1_collect, name='map_1_collect'),
    path('map_2_collect', views.map_2_collect, name='map_2_collect'),
    path('map_3_collect', views.map_3_collect, name='map_3_collect'),
]