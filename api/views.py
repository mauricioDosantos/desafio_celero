from api.serializers import PessoaSerializer, TimeSerializer, EventoSerializer, MedalhaSerializer
from rest_framework import generics
from .models import Pessoa, Time, Evento, Medalha, PessoaTime, MedalhaPessoa, PessoaEvento


# add, update, delete, listing
class PessoaList(generics.ListCreateAPIView):
    queryset = Pessoa.objects.all()
    serializer_class = PessoaSerializer

    def perform_create(self, serializer):  # todo: ao criar tenho que relacionar a um time existente e evento existente
        serializer.save(user=self.request.user)


class TimeList(generics.ListCreateAPIView):  # todo: criar independente
    queryset = Time.objects.all()
    serializer_class = TimeSerializer


class EventoList(generics.ListCreateAPIView):  # todo: criar independente
    queryset = Evento.objects.all()
    serializer_class = EventoSerializer


class MedalhaList(generics.ListCreateAPIView):  # todo: criar independente
    queryset = Medalha.objects.all()
    serializer_class = MedalhaSerializer


def add():
    pass

def update():
    pass

def delete():
    pass

def listing():
    pass