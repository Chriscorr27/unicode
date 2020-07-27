from django.urls import path
from . import views
urlpatterns = [
    path('', views.search,name='MovieSearch'),
    path('movie_detail/<str:imdbId>',views.detail,name='MovieDetail'),
    path('<str:search_movie>',views.Movie_search,name='searchedMovie'),

]
