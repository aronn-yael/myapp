from django.urls import path
from . import views

urlpatterns = [
    path('mymodel/', views.my_model_list, name='my_model_list'),
    # Ajouter la route pour la page d'accueil
    # Elle sera accessible à l'URL /myapp/
    path('', views.home_view, name='home'),
]
