from api.serializers import PessoaSerializer, TimeSerializer, EventoSerializer, MedalhaSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Pessoa, Time, Evento, Medalha
# from .add_data import *


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def pessoa(request, pk=None):
    if request.method == 'POST':
        pessoa = PessoaSerializer(data=request.data)
        if pessoa.is_valid():
            pessoa.save()
            return Response(status=status.HTTP_200_OK)

        return Response({'message': 'invalid data'})

    try:
        pessoa = Pessoa.objects.get(id=pk)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        if pessoa:
            return Response(PessoaSerializer(pessoa).data)
        return Response(status=status.HTTP_404_NOT_FOUND)

    elif request.method == 'PUT':
        serializer = PessoaSerializer(pessoa, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

    elif request.method == 'DELETE':
        pessoa.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    return Response({'Method': f'invalid {request.method}'})


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def time(request, pk=None):
    if request.method == 'POST':
        time = TimeSerializer(data=request.data)
        if time.is_valid():
            time.save()
        else:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response({'message': 'invalid data'})

    try:
        time = Time.objects.get(id=pk)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        if time:
            return Response(TimeSerializer(time).data)
        return Response(status=status.HTTP_404_NOT_FOUND)

    elif request.method == 'PUT':
        time_serializer = TimeSerializer(time, data=request.data)
        if time_serializer.is_valid():
            time_serializer.save()
            return Response(time_serializer.data)

    elif request.method == 'DELETE':
        time.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    return Response({'Method': f'invalid {request.method}'})


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def evento(request, pk=None):
    if request.method == 'POST':
        evento = EventoSerializer(data=request.data)
        if evento.is_valid():
            evento.save()
        else:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response({'message': 'invalid data'})

    try:
        evento = Evento.objects.get(id=pk)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        if evento:
            return Response(EventoSerializer(evento).data)
        return Response(status=status.HTTP_404_NOT_FOUND)

    elif request.method == 'PUT':
        evento_serializer = EventoSerializer(evento, data=request.data)
        if evento_serializer.is_valid():
            evento_serializer.save()
            return Response(evento_serializer.data)

    elif request.method == 'DELETE':
        evento.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    return Response({'Method': f'invalid {request.method}'})


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def medalha(request, pk=None):
    if request.method == 'POST':
        medalha = MedalhaSerializer(data=request.data)
        if medalha.is_valid():
            medalha.save()
        else:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response({'message': 'invalid data'})

    try:
        medalha = Medalha.objects.get(id=pk)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        if medalha:
            return Response(MedalhaSerializer(medalha).data)
        return Response(status=status.HTTP_404_NOT_FOUND)

    elif request.method == 'PUT':
        medalha_serializer = MedalhaSerializer(medalha, data=request.data)
        if medalha_serializer.is_valid():
            medalha_serializer.save()
            return Response(medalha_serializer.data)

    elif request.method == 'DELETE':
        medalha.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    return Response({'Method': f'invalid {request.method}'})

