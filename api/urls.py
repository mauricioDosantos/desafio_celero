from django.urls import path
from .views import pessoa, time, evento, medalha


"""
    Rotas da API.
"""


urlpatterns = [
    path('PessoaList/', pessoa, name='pessoa'),
    path('PessoaList/<int:pk>', pessoa, name='pessoa-id'),

    path('TimeList/', time, name='time'),
    path('TimeList/<int:pk>', time, name='time-id'),

    path('EventoList/', evento, name='evento'),
    path('EventoList/<int:pk>', evento, name='evento-id'),

    path('MedalhaList/', medalha, name='medalha'),
    path('MedalhaList/<int:pk>', medalha, name='medalha-id'),
]