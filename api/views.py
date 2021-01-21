from api.serializers import PessoaSerializer, TimeSerializer, EventoSerializer
from rest_framework import generics
from .models import Pessoa, Time, Evento, PessoaTime, MedalhaPessoa, PessoaEvento


# add, update, delete, listing
class PessoaList(generics.ListCreateAPIView):
    queryset = Pessoa.objects.all()
    serializer_class = PessoaSerializer

    def perform_create(self, serializer):  # todo: ao criar tenho que relacionar a um time existente no bd
        serializer.save(user=self.request.user)


class TimeList(generics.ListCreateAPIView):  # todo: ao criar o time posso relacionalo a um ou mais eventos
    queryset = Time.objects.all()
    serializer_class = TimeSerializer


class EventoList(generics.ListCreateAPIView):  # todo: primeiro criar os eventos
    queryset = Evento.objects.all()
    serializer_class = TimeSerializer


def add():
    pass

def update():
    pass

def delete():
    pass

def listing():
    pass