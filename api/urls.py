from django.urls import path
from .views import PessoaList, TimeList, EventoList, MedalhaList, pessoa


urlpatterns = [
    path('PessoaList/', PessoaList.as_view(), name='criar'),
    path('PessoaList/<int:pk>', pessoa, name='update'),
    path('TimeList/', TimeList.as_view(), name='atualizar'),
    path('EventoList/', EventoList.as_view(), name='listar'),
    path('MedalhaList/', MedalhaList.as_view(), name='deletar'),
]