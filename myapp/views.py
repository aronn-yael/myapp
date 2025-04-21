from django.shortcuts import render
from .models import MyModel

# Vue pour la liste des modèles
def my_model_list(request):
    MyModel.objects.create(name="Objet de test") # Note: Creating an object on every request might not be intended long-term
    objects = MyModel.objects.all()  # Récupérer tous les objets MyModel # pylint: disable=no-member
    return render(request, 'myapp/my_model_list.html', {'objects': objects})

# Nouvelle vue pour la page d'accueil
def home_view(request):
    """
    Vue simple pour afficher la page d'accueil.
    """
    # Vous pouvez ajouter du contexte ici si nécessaire
    context = {}
    # Correction: Utiliser le chemin correct relatif au répertoire templates de l'app
    return render(request, 'myapp/home.html', context)
