from django.urls import path
from .views import add, update, listing, delete


urlpatterns = [
    path('PessoaList', add, name='criar'),
    path('TimeList', update, name='atualizar'),
    path('EventoList', listing, name='listar'),
    path('MedalhaList', delete, name='deletar'),
]