from django.urls import path
from . import views
urlpatterns = [
    path('', views.userApi,name='inputUser'),
    
]
