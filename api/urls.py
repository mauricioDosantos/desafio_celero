from django.urls import path
from .view import add, update, listing, delete


urlpatterns = [
    path('add', add, name='criar'),
    path('update', update, name='atualizar'),
    path('listing', listing, name='listar'),
    path('delete', delete, name='deletar'),
]