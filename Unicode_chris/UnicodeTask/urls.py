from django.urls import path
from . import views
urlpatterns = [
    path('', views.home,name='home'),
    path('task2/<int:a>/<int:b>',views.task2,name='task2'),
    path('task',views.task1,name='task'),
]
