from django.urls import path
from . import views

#urlpatterns = [
 #   path('', views.index, name='index'),
    #path('user/', views.user, name='user')
#]

urlpatterns = [
    path('index/', views.index, name='index'),
    path('trainers/', views.TrainerListView.as_view(), name='trainers'),
]