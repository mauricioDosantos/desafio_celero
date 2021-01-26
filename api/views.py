from api.serializers import PessoaSerializer, TimeSerializer, EventoSerializer, MedalhaSerializer
from rest_framework import generics
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Pessoa, Time, Evento, Medalha
# from .add_data import *


# add, update, delete, listing
class PessoaList(generics.ListCreateAPIView):
    queryset = Pessoa.objects.all()
    serializer_class = PessoaSerializer


@api_view(['PUT', 'DELETE'])
def pessoa(request, pk):
    try:
        pessoa = Pessoa.objects.get(id=pk)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = PessoaSerializer(pessoa, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

    elif request.method == 'DELETE':
        pessoa.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    return Response({'Method': f'{request.method}'})


class TimeList(generics.ListCreateAPIView):  # todo: criar independente
    queryset = Time.objects.all()
    serializer_class = TimeSerializer


class EventoList(generics.ListCreateAPIView):  # todo: criar independente
    queryset = Evento.objects.all()
    serializer_class = EventoSerializer


class MedalhaList(generics.ListCreateAPIView):  # todo: criar independente
    queryset = Medalha.objects.all()
    serializer_class = MedalhaSerializer
