from rest_framework import serializers
from .models import Pessoa, Time, Evento, Medalha


class PessoaSerializer(serializers.ModelSerializer):
    class Meta:  # todo: tenho que fazer algo no modelo pessoa para reconhecer as outras classes, algum Meta
        model = Pessoa
        fields = ['id', 'name', 'sex', 'age', 'height', 'weight', 'id_time', 'id_evento', 'id_medalha']


class TimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Time
        fields = '__all__'


class EventoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evento
        fields = '__all__'


class MedalhaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medalha
        fields = '__all__'