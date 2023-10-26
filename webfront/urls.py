from django.urls import path
from .views import home, login, connexion


urlpatterns = [
    path('', home, name='index'),
    path('login', login, name='login'),
    path('connexion', connexion, name='connexion'),
]