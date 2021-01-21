from rest_framework import serializers
from .models import Pessoa, Time, Evento, Medalha, PessoaTime, PessoaEvento, MedalhaPessoa


class PessoaSerializer(serializers.ModelSerializer):
    team = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    event = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    medal = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Pessoa
        fields = ['id', 'name', 'sex', 'age', 'height', 'weight', 'team', 'event', 'medal']


"""
class MedalhaPessoa(models.Model):
    id_pessoa_fk = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    id_medalha_fk = models.ForeignKey(Medalha, on_delete=models.CASCADE)


class PessoaEvento(models.Model):
    id_pessoa_fk = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    id_evento_fk = models.ForeignKey(Evento, on_delete=models.CASCADE)


class PessoaTimeSerializer(serializers.Serializer):
    serializers.PrimaryKeyRelatedField()

    id_pessoa_fk = serializers.PrimaryKeyRelatedField(many=True,)
    id_time_fk = serializers.ForeignKey(Time)

class PessoaEventoSerializer(serializers.Serializer):
class MedalhaPessoaSerializer(serializers.Serializer):

"""


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