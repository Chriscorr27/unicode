from django.urls import path
from . import views
urlpatterns = [
    path('', views.search,name='MovieSearch'),
    path('<str:imdbId>',views.detail,name='MovieDetail'),
]
