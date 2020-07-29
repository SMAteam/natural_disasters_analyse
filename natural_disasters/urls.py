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
    # path('migrate_data', views.migrate_data, name='migrate_data'),
]